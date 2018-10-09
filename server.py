from flask import Flask, redirect, url_for, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:itucspw@localhost/itucsdb'
db = SQLAlchemy(app)

_Dictionary = {
    "SelimK" : "aslan123",
    "admin"  : "admin"
}

@app.route("/")
def index():
    return render_template('main.html')

@app.route("/main", methods = ['GET', 'POST'])
def main():
    if request.method == 'POST':
        userName = request.form['nm']
        userPass = request.form['pw']
        if userName in _Dictionary:
            if userPass == _Dictionary[userName]:
                return redirect(url_for('redirectUser', name = userName))
    else:
        userName = request.args.get('nm')
        return redirect(url_for('redirectUser', name = userName))

@app.route("/user/<name>/")
def redirectUser(name):
    if name == 'admin':
        return redirect(url_for('adminPage'))
    else:
        return redirect(url_for('userPage', userName = name))

@app.route("/admin_page/")
def adminPage():
    return render_template('hello.html', name = 'Admin')

@app.route("/user_page/<userName>/")
def userPage(userName):
    return render_template('hello.html', name = userName)


if __name__ == "__main__":
    app.run()
