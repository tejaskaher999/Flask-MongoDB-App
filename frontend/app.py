from flask import Flask, render_template, request, jsonify
from datetime import datetime
import requests

BACKEND_URL = 'http://127.0.0.1:9000'

app = Flask(__name__)

@app.route('/')
def home():
    day_time = datetime.today().strftime("%d/%m/%Y, %H:%M:%S")
    day_of_week = datetime.today().strftime("%A")

    return render_template('index.html', day_time=day_time, day_of_week=day_of_week)

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)
    requests.post(BACKEND_URL + '/submit', json=form_data)
    return "Data Submitted Successfully!"

@app.route('/get-data', methods=['GET'])
def get_data():
    response = requests.get(BACKEND_URL + '/view')
    data = response.json()
    return data

@app.route('/submit-todo', methods=['POST'])
def submit_todo():
    form_data = dict(request.form)
    requests.post(BACKEND_URL + '/submit-todo', json=form_data)
    return "Data Submitted Successfully!"

@app.route('/todo')
def todo():
    
    return render_template('todo.html')

@app.route('/get-todos', methods=['GET'])
def get_todos():
    response = requests.get(BACKEND_URL + '/view-todos')
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

