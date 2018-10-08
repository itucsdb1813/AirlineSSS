from flask import Flask


app = Flask(__name__)


@app.route("/")
def home_page():
    return "Ana Sayfa"

@app.route("/secondpage")
def second_page():
    return "İkinci Sayfa"


if __name__ == "__main__":
    app.run()
