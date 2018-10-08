from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/main", methods = ['GET', 'POST'])
def main():
    if request.method == 'POST':
        userName = request.form['nm']
        return redirect(url_for('redirectUser', name = userName))
    else:
        userName = request.args.get('nm')
        return redirect(url_for('redirectUser', name = userName))

@app.route("/secondpage/<int:ID>/")
def second_page(ID):
    return "Ikinci Sayfa %d" % ID

@app.route("/user/<name>/")
def redirectUser(name):
    if name == 'admin':
        return redirect(url_for('adminPage'))
    else:
        return redirect(url_for('userPage', userName = name))

@app.route("/admin_page/")
def adminPage():
    return "Welcome Admin!"

@app.route("/user_page/<userName>/")
def userPage(userName):
    return "Welcome %s" % userName


if __name__ == "__main__":
    app.run()
