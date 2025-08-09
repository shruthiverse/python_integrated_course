
---

### Code Sample for Day 8
Below is a single Python file (`Day8_Samples_001.py`) with five sample programs tailored to Module 8: Web Development (Days 36-40), focusing on Day 8's topics of Django and Flask basics and developing dynamic web applications. Note that this requires running with a development server and assumes a basic setup.

```python
# Day8_Samples_001.py
# Program 1: Basic Flask Application
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Day 8 - Flask Basics!"

if __name__ == "__main__":
    app.run(debug=True)

# Program 2: Flask Route with Parameter
@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}! This is a dynamic route."

# Program 3: Simple Django Project Setup (Conceptual)
# Note: Run these commands in terminal: django-admin startproject myproject && cd myproject && python manage.py runserver
print("Django setup: Please run 'django-admin startproject myproject' in terminal.")

# Program 4: Flask with HTML Template (Basic)
from flask import render_template

@app.route('/template')
def template():
    return render_template('day8_template.html')  # Requires a templates folder with day8_template.html

# Program 5: Flask with User Input
from flask import request

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        return f"Thank you, {name}!"
    return '<form method="POST"><input name="name"><input type="submit"></form>'