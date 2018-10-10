from flask import Flask, redirect, url_for, request, render_template
import psycopg2 as dbapi2


app = Flask(__name__)
##app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://ddzwibxvysqwgx:9e0edae8756536ffdba78314ebde69e2d019e58a2c05dfbad508b5eb657ac9e7@ec2-54-247-101-205.eu-west-1.compute.amazonaws.com:5432/d8o6dthnk5anke'
##app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:itucspw@localhost:65530/itucsdb'
app.debug = True
##db = SQLAlchemy(app)


dsn = """user='ddzwibxvysqwgx' password='9e0edae8756536ffdba78314ebde69e2d019e58a2c05dfbad508b5eb657ac9e7'
         host='ec2-54-247-101-205.eu-west-1.compute.amazonaws.com' port=5432 dbname='d8o6dthnk5anke'"""

@app.route("/")
def index():
    try:
        connection = dbapi2.connect(dsn)
        cursor = connection.cursor()
        statement = """SELECT f."FlightID", air."AirportName", air."City", x."PlaneModel" From public."Flights" as f
            inner join public."Planes" as x on x."PlaneID" = f."PlaneID"
            inner join public."Airports" as air on air."AirportID" = f."DestinationID"
        """
        cursor.execute(statement)

    except dbapi2.DatabaseError:
        connection.rollback()
        return "Hata!"
    finally:
        connection.close()
    return render_template('main.html', flights = cursor)


if __name__ == "__main__":
    app.run()
