from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# List to store tasks (in-memory, not persistent across app restarts)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['GET'])
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    if 0 <= task_id < len(tasks):
        if request.method == 'POST':
            # Update the task
            tasks[task_id] = request.form.get('task')
            return redirect(url_for('index'))
        return render_template('edit.html', task=tasks[task_id], task_id=task_id)
    return redirect(url_for('index'))  # Redirect if task_id is invalid

@app.route('/view/<int:task_id>', methods=['GET'])
def view_task(task_id):
    if 0 <= task_id < len(tasks):
        return render_template('view.html', task=tasks[task_id])
    return redirect(url_for('index'))  # Redirect if task_id is invalid

if __name__ == "__main__":
    app.run(debug=True)
