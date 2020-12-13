from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

counter = 0


class Greeting (Resource):
    def get(self):
        global counter
        counter += 1
        return {"message": "Hello Flask API World! Count: {}".format(counter)}


api.add_resource(Greeting, '/')  # Route_1

if __name__ == '__main__':
    app.run('0.0.0.0', '8080')
