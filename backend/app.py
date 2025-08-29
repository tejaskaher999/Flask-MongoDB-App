import os
from flask import Flask, request, jsonify
import pymongo
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = pymongo.MongoClient(MONGO_URI)
db = client.Cluster

collection = db['form_data']

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.json)
    name = form_data.get('name')

    collection.insert_one(form_data)

    return "Data Submitted Successfully!"

@app.route('/view', methods=['GET'])
def get_data():
    data = list(collection.find())
    
    for item in data:
        item['_id'] = str(item['_id'])

    return jsonify(data)

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.json.get('itemName')
    item_desc = request.json.get('itemDescription')
    # Save to MongoDB
    collection.insert_one({"name": item_name, "description": item_desc})
    return jsonify({"status": "success"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)
