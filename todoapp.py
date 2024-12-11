#Stephon Kumar

from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

# Global list to store To-Do items
todo_list = []

@app.route('/')
def home():
    """Main controller to display the To-Do list and input form."""
    return render_template('index.html', todo_list=todo_list)

@app.route('/submit', methods=['POST'])
def submit():
    """Controller to handle new To-Do item submissions."""
    task = request.form.get('task')
    email = request.form.get('email')
    priority = request.form.get('priority')

    # Data validation
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):  # Simple email regex
        return redirect(url_for('home', error="Invalid email address"))
    if priority not in ['Low', 'Medium', 'High']:
        return redirect(url_for('home', error="Invalid priority level"))

    # Append valid item to the list
    todo_list.append({
        'task': task,
        'email': email,
        'priority': priority
    })
    return redirect(url_for('home'))

@app.route('/clear', methods=['POST'])
def clear():
    """Controller to clear all To-Do items."""
    global todo_list
    todo_list = []  # Reset list to empty
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
