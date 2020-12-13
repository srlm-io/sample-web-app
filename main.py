
from flask import Flask

app = Flask(__name__)

counter = 0


@app.route("/")
def counter_route():
    global counter
    counter += 1
    return 'Counter {}'.format(counter)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
