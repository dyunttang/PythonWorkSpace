from flask import Flask
from flask.templating import render_template
import movie_api as ma

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", movies=ma.callMovieApi())
    # Spring 에서는 @Controller 라고 하면 return 되는 애가 File 이 되지만, Python 에서는 render_template 라는 Function 을 써야된다
    # Data 를 return 하고 싶으면 여기서  문자를 return 하면 된다 return type 이 없기 때문이다.
    # Data code 를 던져보자. Python code 를 적어야한다.


if __name__ == "__main__":
    app.run(debug=True)
