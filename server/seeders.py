from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from geopy.geocoders import Nominatim

def get_latitude_longitude(location):
    print(location)
    geolocator = Nominatim(user_agent="geocoder")
    location_data = geolocator.geocode(location)
    
    if location_data:
        latitude = location_data.latitude
        longitude = location_data.longitude
        return latitude, longitude
    else:
        return None

# Example usage
# address = "1600 Amphitheatre Parkway, Mountain View, CA"
# coordinates = get_latitude_longitude(address)

# if coordinates:
#     latitude, longitude = coordinates
#     print("Latitude:", latitude)
#     print("Longitude:", longitude)
# else:
#     print("Failed to retrieve coordinates.")


# Initializing flask app
app = Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost:27017/covid'
mongo = PyMongo(app)

def seed_data():
    print('seeders start')
    db = mongo.db.locations
    # Delete all documents in the "locations" collection
    db.delete_many({})

    names = ['E-11/4', 'Street 1, E-11/4', 'Street 11, E-11/4', 'F-6', 'School Road F-6/1', 'Street 39, F-6/1', 'Street 18, F-6/2', 'Street 1, F-6/3', 'Street 19, F-6/3']

    # Loop over the array of names
    for name in names:
        coordinates = get_latitude_longitude(name + ', Islamabad, Islamabad Capital Territory, Pakistan')

        if coordinates:
            latitude, longitude = coordinates
            db.insert_one({"name": name, "latitude": latitude, "longitude": longitude})
        else:
            print("Failed to retrieve coordinates.")

    db.insert_one({"name": 'Street 5, E-7', "latitude": 33.73194676130276, "longitude": 73.05245366975277})
    db.insert_one({"name": 'Street 15, E-7', "latitude": 33.72683144316864, "longitude": 73.04916788251758})
    db.insert_one({"name": 'Street 9, E-11/2', "latitude": 33.698972479041274, "longitude": 72.9679396640595})
    db.insert_one({"name": 'Street 2, E-11/4', "latitude": 33.70118588704021, "longitude": 72.98445814640664})
    db.insert_one({"name": 'Street 6, E-11/4', "latitude": 33.698888112344186, "longitude": 72.9848676545271})

    print('seeders end')

# seed_data()

CORS(app)
	
# Running app
if __name__ == '__main__':
	seed_data()