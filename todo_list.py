from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
tasks = []  # In-memory list to store tasks

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.json
    task = data.get("task")
    if task:
        tasks.append(task)
        return jsonify({"message": "Task added"}), 201
    return jsonify({"error": "No task provided"}), 400

@app.route("/tasks/<int:index>", methods=["DELETE"])
def delete_task(index):
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        return jsonify({"message": f"Deleted task: {removed}"})
    return jsonify({"error": "Invalid task index"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
    