from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [{'id': 1, 'name': 'Do homework'}]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'todos': tasks})


@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    task = {
        'id': len(tasks) + 1,
        'name': request.json['name'],
    }
    tasks.append(task)
    return jsonify({'task': task}), 201



@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):

    task = None
    for t in tasks:
        if t['id'] == task_id:
            task = t
    return jsonify({'task': task})




