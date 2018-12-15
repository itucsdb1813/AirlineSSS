import psycopg2 as dbapi2
from flask import redirect, url_for, request, session, flash
from general import RenderTemplate, refreshUserData, ifAdmin
#from tickets import create_tickets
from forms import formSendPost
from werkzeug.utils import secure_filename
import datetime

dsn = """user='ddzwibxvysqwgx' password='9e0edae8756536ffdba78314ebde69e2d019e58a2c05dfbad508b5eb657ac9e7'
         host='ec2-54-247-101-205.eu-west-1.compute.amazonaws.com' port=5432 dbname='d8o6dthnk5anke'"""

#Enes
def adm_sendpost():
    refreshUserData()
    if ifAdmin():
        form = formSendPost()
        if request.method == 'POST':
            if form.validate_on_submit():
                connection = dbapi2.connect(dsn)
                cursor = connection.cursor()
                image = form.image.data
                filename = secure_filename(image.filename)
                statement = """INSERT INTO uploads (filename, data) VALUES (%s, %s)
                            """
                cursor.execute(statement, (filename, dbapi2.Binary(image.read())))
                connection.commit()
                statement = """SELECT MAX(id) FROM uploads
                            """
                cursor.execute(statement, (filename, dbapi2.Binary(image.read())))
                id = cursor.fetchone()
                _Datetime = datetime.datetime.now()
                poster = session['Username']
                content = form.content.data
                title = form.title.data
                date = _Datetime.strftime("%d/%m/%Y")
                time = _Datetime.strftime("%H:%M")
                statement = """INSERT INTO posts (poster, content, date, time, title, image) VALUES (%s, %s, TO_DATE(%s, 'DD/MM/YYYY'), %s, %s, %s)
                            """
                cursor.execute(statement, (poster, content, date, time, title, id))
                connection.commit()
                flash('You have succesfully posted an entry.')
                return redirect(url_for('news'))
            for key in form.errors:
                flash(form.errors[key][0])

        return RenderTemplate('adm_sendpost.html', adminActive='active', form=form)
    else:
        return redirect(url_for('errorpage', message = 'Not Authorized!'))

#Enes
def adm_pymreqs():
    refreshUserData()
    if ifAdmin():
        if request.method == 'GET':
            try:
                connection = dbapi2.connect(dsn)
                cursor = connection.cursor()
                statement = """SELECT paymentid, username, amount FROM payments WHERE approved = '0'
                                ORDER BY paymentid ASC
                """
                cursor.execute(statement)
                payments = cursor.fetchall()
                return RenderTemplate('adm_pymreqs.html', payments = payments, adminActive='active')
            except dbapi2.DatabaseError:
                connection.rollback()
                return "Hata!"
            finally:
                connection.close()
            return RenderTemplate('adm_pymreqs.html', adminActive='active')
        elif request.method == 'POST':
            try:
                for key in request.form.keys():
                    pymId = key[3:]
                    if request.form[key]:

                        connection = dbapi2.connect(dsn)
                        cursor = connection.cursor()
                        statement = """UPDATE payments SET approved = %s, approved_by = %s WHERE paymentid = %s
                        """
                        cursor.execute(statement, ('1', session['Username'], pymId))

                        ##statement = """SELECT amount FROM payments WHERE paymentid = %s
                        ##"""
                        ##cursor.execute(statement, (pymId))
                        ##amount = cursor.fetchone()

                        statement = """UPDATE person
                                        SET balance = t1.balance + t2.amount
                                        FROM person as t1
                                        INNER JOIN payments as t2 ON t2.username = t1.username
                                        WHERE t2.paymentid = %s
                                          AND person.username = t2.username;
                        """ % pymId
                        cursor.execute(statement)
                        connection.commit()
                flash('Approved requests')
                return redirect(url_for('adm_pymreqs'))
            except dbapi2.DatabaseError as e:
                connection.rollback()
                return str(e)
            finally:
                connection.close()

#Enes
def deleteuser(username):
    if ifAdmin():
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """DELETE FROM users WHERE username = '%s'
            """ % username
            cursor.execute(statement)
            statement = """DELETE FROM person WHERE username = '%s'
            """ % username
            cursor.execute(statement)
            connection.commit()
            flash('You have succesfully deleted a user.')
            return RenderTemplate('adm_users.html', adminActive='active')
        except dbapi2.DatabaseError:
            connection.rollback()
            return "Hata!"
        finally:
            connection.close()
    else:
        return redirect(url_for('errorpage', message = 'Not Authorized!'))

#Enes
def adminpage():
    if ifAdmin():
        return RenderTemplate('adminpage.html', adminActive='active')
    else:
        return redirect(url_for('errorpage', message = 'You are not authorized!'))

#Enes
def adm_users():
    if ifAdmin():
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            username = session['Username']
            statement = """SELECT * FROM person WHERE username <> '%s'
            """ % username
            cursor.execute(statement)
            rows = cursor.fetchall()
            return RenderTemplate('adm_users.html', userlist = rows, adminActive='active')
        except dbapi2.DatabaseError as e:
            connection.rollback()
            return e
        finally:
            connection.close()
    else:
        return redirect(url_for('errorpage', message = 'You are not authorized!'))

#Enes
def updateuser(username):
    if ifAdmin():
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            statement = """SELECT * FROM person WHERE username = '%s'
            """ % username
            cursor.execute(statement)
            row = cursor.fetchone()
            return RenderTemplate('adm_updateuser.html', user = row, adminActive='active')
        except dbapi2.DatabaseError as e:
            connection.rollback()
            return e
        finally:
            connection.close()
    else:
        return redirect(url_for('errorpage', message = 'You are not authorized!'))

#Enes
def adm_updateuser(username):
    if ifAdmin():
        try:
            form_dict = request.form
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()

            statement = """UPDATE person SET
            """
            set_text = ""
            if 'fname_cb' in form_dict and form_dict['fname_cb']:
                set_text += ("fullname = '%s'" % form_dict['fullname']) + ','
            if 'mail_cb' in form_dict and form_dict['mail_cb']:
                set_text += ("emailaddress = '%s'" % form_dict['mail']) + ','
            if 'role_cb' in form_dict and form_dict['role_cb']:
                set_text += ("userrole = '%s'" % form_dict['role']) + ','
            if 'balance_cb' in form_dict and form_dict['balance_cb']:
                set_text += ("balance = '%s'" % form_dict['balance']) + ','
            if len(set_text) > 0:
                set_text = set_text[:-1]
                statement += set_text
                statement += " WHERE username = '%s'" % username
            else:
                return redirect(url_for('adm_users'))
            cursor.execute(statement)
            connection.commit()
            flash('You have succesfully updated a user.')
            return redirect(url_for('adm_users'))
        except dbapi2.DatabaseError as e:
            connection.rollback()
            return e
        finally:
            connection.close()
    else:
        return redirect(url_for('errorpage', message = 'You are not authorized!'))

#Enes
def adm_fabrika_ayarlari():
    if ifAdmin():
        try:
            connection = dbapi2.connect(dsn)
            cursor = connection.cursor()
            INIT_STATEMENTS = [ """DROP TABLE tickets"""
            , """DROP TABLE flights"""
            , """DROP TABLE airports"""
            , """DROP TABLE cities"""
            , """DROP TABLE planes"""
            , """DROP TABLE posts"""
            , """DROP TABLE payments"""
            , """DROP TABLE person"""
            , """DROP TABLE uploads"""
            , """DROP TABLE users""" ]
            for statement in INIT_STATEMENTS:
                cursor.execute(statement)
            connection.commit()

            return redirect(url_for('adminpage'))
        except dbapi2.DatabaseError as e:
            connection.rollback()
            return str(e)
        finally:
            connection.close()

    else:
        return redirect(url_for('errorpage', message='Not Authorized!'))
