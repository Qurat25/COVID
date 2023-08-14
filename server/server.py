from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask_cors import CORS
from bson import json_util, ObjectId

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

@app.route('/api/addDate', methods=['POST'])
def addDate():
    data = request.json  # Get the JSON data from the POST request
    
    try:
        # Access the "Date" collection
        date_collection = mongo.db.date
            
        # Convert location IDs to ObjectIds if necessary
        location_ids = [ObjectId(location_id) for location_id in data["location"]]
            
        # Replace the location IDs with the array of ObjectIds
        data["location"] = location_ids
                
        # Insert the data into the "Date" collection
        inserted_id = date_collection.insert_one(data).inserted_id
                
        response_data = {"message": "Data submitted successfully", "inserted_id": str(inserted_id)}
        return jsonify(response_data), 200

    except Exception as e:
        response_data = {"message": "Error submitting data", "error": str(e)}
        return jsonify(response_data), 500
	
# Running app
if __name__ == '__main__':
	app.run()