from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

# Import configuration values
from config import DEBUG, MONGO_URI, MONGO_DB

# Initializing flask app
app = Flask(__name__)
app.config['DEBUG'] = DEBUG

# Configure MongoDB
app.config['MONGO_URI'] = MONGO_URI
app.config['MONGO_DBNAME'] = MONGO_DB
mongo = PyMongo(app)

CORS(app)
	
# Running app
if __name__ == '__main__':
	app.run()