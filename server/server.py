from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson import json_util

# Import configuration values
from config import DEBUG, MONGO_URI, MONGO_DB

# Initializing flask app
app = Flask(__name__)
app.config['DEBUG'] = DEBUG

# Configure MongoDB
app.config['MONGO_URI']='mongodb://localhost:27017/covid'
mongo = PyMongo(app)

CORS(app)

@app.route('/api/getAllData', methods=['GET'])
def get_all_data():
    collection = mongo.db.locations # Replace 'collection_name' with the name of your collection
    cursor = collection.find()
    data = json_util.dumps(list(cursor))  # Use json_util to serialize MongoDB data types
    return data
	
# Running app
if __name__ == '__main__':
	app.run()