from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api = Api(app, version='1.0', title='TodoMVC API',
          description='A simple TodoMVC API',
          )

ns = api.namespace('todo', description='TODO operations')

task_model = api.model('Task', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'name': fields.String(required=True, description='The task details')
})


class TaskDAO(object):
    def __init__(self):
        self.counter = 0
        self.tasks = []

    def get(self, task_id):
        for t in self.tasks:
            if t['id'] == task_id:
                return t
        api.abort(404, "Task {} doesn't exist".format(id))

    def create(self, data):
        task = {
            'id': self.counter + 1,
            'name': data['name'],
        }

        self.tasks.append(task)
        self.counter = self.counter + 1
        return task

DAO = TaskDAO()
DAO.create({'name': 'Do homework'})
DAO.create({'name': 'Watch TV'})

@ns.route('/')
class TodoList(Resource):
    @ns.doc('list_tasks')
    @ns.marshal_list_with(task_model)
    def get(self):
        return DAO.tasks

    @ns.doc('create_task')
    @ns.expect(task_model)
    @ns.marshal_with(task_model, code=201)
    def post(self):
        return DAO.create(api.payload), 201

