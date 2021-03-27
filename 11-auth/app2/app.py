from flask import Flask, request, jsonify
from flask_restx import Resource, Api
from flask_basicauth import BasicAuth

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'user1'
app.config['BASIC_AUTH_PASSWORD'] = 'abcxyz'
api = Api(app)
basic_auth = BasicAuth(app)

tasks = [{'id': 1, 'name': 'Do homework'}]

class TodoList(Resource):
    @basic_auth.required
    def get(self):
        return jsonify({'tasks': tasks})

    @basic_auth.required
    def post(self):
        task = {
            'id': len(tasks) + 1,
            'name': api.payload['name'],
        }
        tasks.append(task)
        return api.payload, 201

api.add_resource(TodoList,'/todo')