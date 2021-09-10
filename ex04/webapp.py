from flask import Flask

from flask import Flask
app = Flask(__name__)

print(__name__)

app = Flask(__name__)


@app.route("/hello")
def hello():
    return "Hello World!"


@app.route("/bye")
def bye():
    return "Bye !!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3500)
