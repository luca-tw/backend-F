from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "This is Home Page"


@app.route("/hello")
def hello():
    return "Hello World! "


if __name__ == "__main__":
    app.run()
