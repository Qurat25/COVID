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

    names = ['E-11/4', 'Street 1, E-11/4', 'Street 11, E-11/4', 'F-6', 'School Road F-6/1', 'Street 39, F-6/1', 'Street 18, F-6/2', 
             'Street 1, F-6/3', 'Street 19, F-6/3', 'Street 32, F-7/1', 'Street 40, F-7/1', 'Street 27, F-8/1', 'Street 31, F-8/1', 
             'Street 35, F-8/1', 'Street 36, F-8/1', 'Street 37, F-8/1', 'Street 38, F-8/1', 'Street 42, F-8/1', 'Street 44, F-8/1', 
             'Street 5, F-8/3', 'Street 6, F-8/3', 'Street 10, F-8/3', 'Street 11, F-8/3', 'Street 17, F-8/3', 'Street 17, F-10/2',
             'Street 18, F-10/2', 'Street 50, F-10/4', 'Street 52, F-10/4', 'Street 53, F-10/4',
             'Street 55, F-10/4', 'F-11/1', 'Street 69, F-11/1', 'Street 16, F-11/2', 'Street 21, F-11/2', 'Street 23, F-11/2', 
             'Street 28, F-11/2', 'F-11/2', 'Street 46, F-11/3', 'Street 53, F-11/3', 'G-5/1', 'Street 40, G-6/1', 'Street 48, G-6/1', 
             'Street 12, G-6/2', 'Street 23, G-6/2', 'Street 35, G-6/2', 'G-6/2', 'Street 13, G-6/4', 'Street 52, G-6/4', 'Street 56, G-6/4', 
             'Street 59, G-6/4', 'Street 62, G-6/4', 'Street 79, G-6/4', 'Street 80, G-6/4', 'Street 10, G-7/2', 'Street 24, G-7/2',
             'Street 34, G-7/2', 'Street 40, G-7/2', 'Street 56, G-7/2', 'G-7/2', 'G-9/1', 'Street 26, G-9/1', 'Street 34, G-9/1',
             'Street 41, G-9/1', 'Street 52, G-9/1', 'Street 74, G-9/1', 'G-9/2', 'Street 1, G-9/2', 'G-9/3', 'Street 2, G-9/3',
             'Street 10, G-9/3', 'Street 68, G-9/3', 'Street 70, G-9/3', 'Street 74, G-9/3', 'Street 75, G-9/3', 'Street 77, G-9/3',
             'Street 56, G-9/4', 'Street 62, G-9/4', 'Street 66, G-9/4', 'Street 67, G-9/4', 'G-10/2', 'Street 14, G-10/2', 'Street 20, G-10/2',
             'Street 30, G-10/2', 'G-10/3', 'Street 52, G-10/3', 'Street 53, G-10/3', 'Street 69, G-10/3', 'Street 70, G-10/3',
             'Street 38, G-10/4', 'Street 44, G-10/4', 'Street 45, G-10/4' 'Street 46, G-10/4', 'Street 47, G-10/4', 'Street 48, G-10/4',
             'Sawan Road, G-10/4', 'G-10/4', 'G-11/1', 'Street 33, G-11/2', 'Street 42, G-11/2', 'Street 43, G-11/2', 'Street 44, G-11/2',
             'Street 46, G-11/2', 'Street 71, G-11/2', 'G-11/3', 'Street 30, G-13/2', 'Street 32, G-13/2', 'Street 33, G-13/2', 'Street 34, G-13/2',
             'Street 45, G-13/2', 'Street 47, G-13/2', 'Street 48, G-13/2', 'Street 49, G-13/2', 'I-8 Markaz', 'Street 15, I-8/1', 'Street 25, I-8/2',
             'Street 29, I-8/2', 'Street 57, I-8/2', 'Street 58, I-8/2', 'I-8/3', 'Street 78, I-8/3', 'I-8/4', 'Street 85, I-8/4', 'Street 91, I-8/4',
             'Street 92, I-8/4', 'Street 95, I-8/4', 'Street 96, I-8/4', 'Street 35, I-9/4', 'I-10 Markaz', 'I-10', 'I-10/1', 'I-10/2', 'I-10/3',
             'I-10/4', 'DHA Phase II', 'Chak Shahzad', 'Bhara Kahu', 'Soan Gardens', 'NIH Colony', 'Bani Gala', 'Shahzad Town', 'Blue Area']

    # Loop over the array of names
    for name in names:
        coordinates = get_latitude_longitude(name + ', Islamabad, Islamabad Capital Territory, Pakistan')

        if coordinates:
            latitude, longitude = coordinates
            db.insert_one({"name": name, "latitude": latitude, "longitude": longitude})
        else:
            print("Failed to retrieve coordinates.")

    # coordinates = get_latitude_longitude('Street 23, Rawal Town, Islamabad, Islamabad Capital Territory, Pakistan')

    # if coordinates:
    #     latitude, longitude = coordinates
    #     db.insert_one({"name": 'Street 13, Qurtaba Town, Khanna', "latitude": latitude, "longitude": longitude})
    # else:
    #     print("Failed to retrieve coordinates.")

    db.insert_one({"name": 'Street 5, E-7', "latitude": 33.73194676130276, "longitude": 73.05245366975277})
    db.insert_one({"name": 'Street 15, E-7', "latitude": 33.72683144316864, "longitude": 73.04916788251758})
    db.insert_one({"name": 'Street 9, E-11/2', "latitude": 33.698972479041274, "longitude": 72.9679396640595})
    db.insert_one({"name": 'Street 2, E-11/4', "latitude": 33.70118588704021, "longitude": 72.98445814640664})
    db.insert_one({"name": 'Street 6, E-11/4', "latitude": 33.698888112344186, "longitude": 72.9848676545271})
    db.insert_one({"name": 'Street 53, F-6/4', "latitude": 33.72743936552043, "longitude": 73.08441734714417})
    db.insert_one({"name": 'Street 52, F-11/2', "latitude": 33.68740021641307, "longitude": 72.99460447161437})
    db.insert_one({"name": 'Street 30, G-6/1', "latitude": 33.71291803772815, "longitude": 73.08302325235887})
    db.insert_one({"name": 'Street 39, G-6/1', "latitude": 33.71129865384658, "longitude": 73.08447972392793})
    db.insert_one({"name": 'Street 92, G-6/1', "latitude": 33.714586905438736, "longitude": 73.08763978318423})
    db.insert_one({"name": 'Street 104, G-6/1', "latitude": 33.70975008317992, "longitude": 73.08808753786181})
    db.insert_one({"name": 'Street 8, G-6/2', "latitude": 33.717162509775065, "longitude": 73.08742532528768})
    db.insert_one({"name": 'Street 54, G-7/2', "latitude": 33.70508967510921, "longitude": 73.0660481914141})
    db.insert_one({"name": 'Street 58, G-7/2', "latitude": 33.70452317908572, "longitude": 73.06793622490365})
    db.insert_one({"name": 'Street 8, G-9/3', "latitude": 33.6901136647583, "longitude": 73.03437800775795})
    db.insert_one({"name": 'Street 122, G-9/3', "latitude": 33.69405111724624, "longitude": 73.03482585285575})
    db.insert_one({"name": 'Street 123, G-9/3', "latitude": 33.69424740937908, "longitude": 73.03585677159117})
    db.insert_one({"name": 'Street 125, G-9/3', "latitude": 33.69570070006114, "longitude": 73.03686587282621})
    db.insert_one({"name": 'Street 126, G-9/3', "latitude": 33.696067084440735, "longitude": 73.03676969602037})
    db.insert_one({"name": 'Street 85, G-9/4', "latitude": 33.68341158934146, "longitude": 73.03867207806721})
    db.insert_one({"name": 'Street 89, G-9/4', "latitude": 33.6853675170186, "longitude": 73.0400109676153})
    db.insert_one({"name": 'Street 91, G-9/4', "latitude": 33.68624079271245, "longitude": 73.03856422292927})
    db.insert_one({"name": 'Street 93, G-9/4', "latitude": 33.685290047664445, "longitude": 73.04242078726756})
    db.insert_one({"name": 'Street 96, G-9/4', "latitude": 33.68614278446608, "longitude": 73.04139580747916})
    db.insert_one({"name": 'Street 98, G-9/4', "latitude": 33.687933205346575, "longitude": 73.04352150775817})
    db.insert_one({"name": 'Street 99, G-9/4', "latitude": 33.68829640118481, "longitude": 73.04325084973559})
    db.insert_one({"name": 'Street 100, G-9/4', "latitude": 33.68730885688465, "longitude": 73.04183450351105})
    db.insert_one({"name": 'Street 111, G-9/4', "latitude": 33.68801491263485, "longitude": 73.03603457674872})
    db.insert_one({"name": 'Street 24A, G-10/2', "latitude": 33.67765738003551, "longitude": 73.00876432385041})
    db.insert_one({"name": 'Street 25A, G-10/2', "latitude": 33.676364639058306, "longitude": 73.00651079182165})
    db.insert_one({"name": 'Street 15, G-11/2', "latitude": 33.66492622221961, "longitude": 72.99230944606865})
    db.insert_one({"name": 'Street 18, G-11/2', "latitude": 33.66488666481684, "longitude": 72.99307634526852})
    db.insert_one({"name": 'Street 21, G-11/2', "latitude": 33.66619139252533, "longitude": 72.9939749476943})
    db.insert_one({"name": 'Street 74, G-13/2', "latitude": 33.647232759640616, "longitude": 72.95554289294756})
    db.insert_one({"name": 'Street 19A, G-15/1', "latitude": 33.62675273278685, "longitude": 72.92632903544781})
    db.insert_one({"name": 'Rimsha Colony, H-9', "latitude": 33.66929351817044, "longitude": 73.03370726682321})
    db.insert_one({"name": 'Street 49, I-8/2', "latitude": 33.67006840503741, "longitude": 73.06838007706982})
    db.insert_one({"name": 'Street 59, I-8/3', "latitude": 33.675461481002266, "longitude": 73.07311416060607})
    db.insert_one({"name": 'Street 77, I-8/3', "latitude": 33.67054372368746, "longitude": 73.07853480943523})
    db.insert_one({"name": 'Street 1, I-8/4', "latitude": 33.662433317746085, "longitude": 73.07251451438094})
    db.insert_one({"name": 'Street 5, I-8/4', "latitude": 33.65914089094039, "longitude": 73.06871431444775})
    db.insert_one({"name": 'Street 86, I-8/4', "latitude": 33.664698181024974, "longitude": 73.07928480465924})
    db.insert_one({"name": 'Street 109, I-8/4', "latitude": 33.66491337045483, "longitude": 73.07329786051716})
    db.insert_one({"name": 'Street 28, I-9/4', "latitude": 33.66766020754094, "longitude": 73.06763318691269})
    db.insert_one({"name": 'Street 34, I-9/4', "latitude": 33.655208476639835, "longitude": 73.05925200827805})
    db.insert_one({"name": 'Street 55, I-10/1', "latitude": 33.64286346532094, "longitude": 73.034801230864})
    db.insert_one({"name": 'Street 56, I-10/1', "latitude": 33.641395033041725, "longitude": 73.03302267943313})
    db.insert_one({"name": 'Street 57, I-10/1', "latitude": 33.64172237322724, "longitude": 73.03380171436461})
    db.insert_one({"name": 'Street 58, I-10/1', "latitude": 33.64145009969358, "longitude": 73.03397809963029})
    db.insert_one({"name": 'Street 61, I-10/1', "latitude": 33.6394575825844, "longitude": 73.03436377605766})
    db.insert_one({"name": 'Street 64, I-10/1', "latitude": 33.638907534412624, "longitude": 73.03540373777575})
    db.insert_one({"name": 'Street 65, I-10/1', "latitude": 33.639085654129, "longitude": 73.03616556746971})
    db.insert_one({"name": 'Street 66, I-10/1', "latitude": 33.63806143042809, "longitude": 73.03488365435338})
    db.insert_one({"name": 'Street 67, I-10/1', "latitude": 33.638461996754735, "longitude": 73.03626309950727})
    db.insert_one({"name": 'Street 71, I-10/1', "latitude": 33.640583506897656, "longitude": 73.03926957449453})
    db.insert_one({"name": 'Street 80, I-10/1', "latitude": 33.64301221282821, "longitude": 73.03890752170831})
    db.insert_one({"name": 'Street 81, I-10/1', "latitude": 33.64332349370921, "longitude": 73.03868805331543})
    db.insert_one({"name": 'Street 82, I-10/1', "latitude": 33.642929279580244, "longitude": 73.03693154951021})
    db.insert_one({"name": 'Street 83, I-10/1', "latitude": 33.64305347499918, "longitude": 73.03663824125141})
    db.insert_one({"name": 'Street 90, I-10/1', "latitude": 33.64547257856954, "longitude": 73.0401507507062})
    db.insert_one({"name": 'Street 3, I-10/2', "latitude": 33.65100393642437, "longitude": 73.02731174977598})
    db.insert_one({"name": 'Street 9, I-10/2', "latitude": 33.65016589722377, "longitude": 73.02723254993751})
    db.insert_one({"name": 'Street 12, I-10/2', "latitude": 33.65007378002574, "longitude": 73.03078165405987})
    db.insert_one({"name": 'Street 17, I-10/2', "latitude": 33.648680798875816, "longitude": 73.02983145860527})
    db.insert_one({"name": 'Street 32, I-10/2', "latitude": 33.64649658568653, "longitude": 73.0330499181866})
    db.insert_one({"name": 'Street 33, I-10/2', "latitude": 33.64637120347896, "longitude": 73.03377286664103})
    db.insert_one({"name": 'Street 26, I-10/4', "latitude": 33.645818157402545, "longitude": 73.04821609137613})
    db.insert_one({"name": 'Street 31-A, I-10/4', "latitude": 33.649171407782504, "longitude": 73.04751742564922})
    db.insert_one({"name": 'Street 31-C, I-10/4', "latitude": 33.648739057670014, "longitude": 73.04842046988004})
    db.insert_one({"name": 'Street 98, I-10/4', "latitude": 33.64499175058977, "longitude": 73.04233255286941})
    db.insert_one({"name": 'Street 107, I-10/4', "latitude": 33.64577000673686, "longitude": 73.04676229740322})
    db.insert_one({"name": 'Street 112, I-10/4', "latitude": 33.64644085164581, "longitude": 73.0419404504331})
    db.insert_one({"name": 'Street 15, River Garden', "latitude": 33.55137728596128, "longitude": 73.16281824541139})
    db.insert_one({"name": 'Street 2, Sector A, DHA Phase II', "latitude": 33.53299935894244, "longitude": 73.13355764978154})
    db.insert_one({"name": 'Street 4, Sector A, DHA Phase II', "latitude": 33.53410506390739, "longitude": 73.13113115975271})
    db.insert_one({"name": 'Street 11, Sector A, DHA Phase II', "latitude": 33.52758452282328, "longitude": 73.14302754405185})
    db.insert_one({"name": 'Lane 5, Sector G, DHA Phase II', "latitude": 33.52676183820734, "longitude": 73.17120862544681})
    db.insert_one({"name": 'Street 8, Sector G, DHA Phase II', "latitude": 33.52853986872813, "longitude": 73.17588596570612})
    db.insert_one({"name": 'Street 12, Sector G, DHA Phase II', "latitude": 33.530873035697574, "longitude": 73.17238854068673})
    db.insert_one({"name": 'Street 13, Sector G, DHA Phase II', "latitude": 33.53142896473399, "longitude": 73.17216588861577})
    db.insert_one({"name": 'Kot Hathial, Bhara Kahu', "latitude": 33.74822197595511, "longitude": 73.17465845954484})
    db.insert_one({"name": 'Street 10, Kashmiri Mohalla', "latitude": 33.72442943030805, "longitude": 73.17282500943742})
    db.insert_one({"name": 'Street 13, Qurtaba Town, Khanna', "latitude": 33.62570314503199, "longitude": 73.12175538075583})
    db.insert_one({"name": 'Lohi Bhair', "latitude": 33.58151326856965, "longitude": 73.16337612368093})
    db.insert_one({"name": 'Chatta Bakhtawar', "latitude": 33.66741190479868, "longitude": 73.15454726783626})
    db.insert_one({"name": 'Street 13-C, National Police Foundation', "latitude": 33.69508633926081, "longitude": 72.98389985438584})
    db.insert_one({"name": 'Street 23, Rawal Town', "latitude": 33.68695507803006, "longitude": 73.11764570845358})

    print('seeders end')

# seed_data()

CORS(app)
	
# Running app
if __name__ == '__main__':
	seed_data()