from flask import Flask, request, jsonify
from models import Todo

app = Flask(__name__)

# Lista de tareas (simulación de una base de datos)
todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.json
    todo = Todo(done=data['done'], label=data['label'])
    todos.append(todo)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position >= 0 and position < len(todos):
        del todos[position]
        return jsonify(todos)
    else:
        return jsonify({"error": "Todo not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)