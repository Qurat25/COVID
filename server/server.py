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

@app.route('/api/getAllLocations', methods=['GET'])
def getAllLocations():
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

        # Convert polygon IDs to ObjectIds if necessary
        polygon_ids = [ObjectId(polygon_id) for polygon_id in data["polygon"]]
            
        # Replace the location IDs with the array of ObjectIds
        data["polygon"] = polygon_ids
                
        # Insert the data into the "Date" collection
        inserted_id = date_collection.insert_one(data).inserted_id
                
        response_data = {"message": "Data submitted successfully", "inserted_id": str(inserted_id)}
        return jsonify(response_data), 200

    except Exception as e:
        response_data = {"message": "Error submitting data", "error": str(e)}
        return jsonify(response_data), 500
    
@app.route('/api/getAllDates', methods=['GET'])
def getAllDates():
    collection = mongo.db.date # Replace 'collection_name' with the name of your collection
    cursor = collection.find()
    data = json_util.dumps(list(cursor))  # Use json_util to serialize MongoDB data types
    return data

@app.route('/api/getLocationByDate', methods=['GET'])
def getLocationByDate():
    collection = mongo.db.date # Replace 'collection_name' with the name of your collection
    filterDate = request.args.get('filterDate')
    # Construct the query filter
    query = {'date': filterDate}
    
    # Perform a lookup to populate the 'location' array
    cursor = collection.aggregate([
        {'$match': query},
        {'$lookup': {
            'from': 'locations',  # Replace 'locations' with the actual name of the referenced collection
            'localField': 'location',
            'foreignField': '_id',
            'as': 'populated_location'
        }},
        {'$project': {
            '_id': 0,
            'date': 1,
            'populated_location': 1
        }}
    ])
    data = json_util.dumps(list(cursor))  # Use json_util to serialize MongoDB data types
    return data

@app.route('/api/getPolygonByDate', methods=['GET'])
def getPolygonByDate():
    collection = mongo.db.date # Replace 'collection_name' with the name of your collection
    filterDate = request.args.get('filterDate')
    # Construct the query filter
    query = {'date': filterDate}
    
    # Perform a lookup to populate the 'location' array
    cursor = collection.aggregate([
        {'$match': query},
        {'$lookup': {
            'from': 'polygon',  # Replace 'locations' with the actual name of the referenced collection
            'localField': 'polygon',
            'foreignField': '_id',
            'as': 'populated_polygon'
        }},
        {'$project': {
            '_id': 0,
            'date': 1,
            'populated_polygon': 1
        }}
    ])
    data = json_util.dumps(list(cursor))  # Use json_util to serialize MongoDB data types
    return data

@app.route('/api/getAllPolygons', methods=['GET'])
def getAllPolygons():
    collection = mongo.db.polygon # Replace 'collection_name' with the name of your collection
    cursor = collection.find()
    data = json_util.dumps(list(cursor))  # Use json_util to serialize MongoDB data types
    return data
	
# Running app
if __name__ == '__main__':
	app.run()