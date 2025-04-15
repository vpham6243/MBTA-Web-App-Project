from flask import Flask
import mbta_helper

print(mbta_helper.find_stop_near("Boston Common"))


app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)
