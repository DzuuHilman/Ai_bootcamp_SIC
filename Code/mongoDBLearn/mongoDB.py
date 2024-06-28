from flask import Flask, request, jsonify
from dotenv import load_dotenv          # For securing mongoDB URI
import pymongo
import os

# Securing mongoDB URI
load_dotenv()
MONGO_URI = os.getenv("SIC_LEARN_MONGO_URI")


app = Flask(__name__)

client = pymongo.MongoClient(MONGO_URI)
database = client['SIClearn']
sensorCollection = database['/sensor1/LEDSensor/all']

sensorData1 = {
        "Timestamp": "16:40:00",
        "Sensor value": 500,
        "LED condition": "ON"
    }
sensorData2 = {
        "Timestamp": "16:41:00",
        "Sensor value": 600,
        "LED condition": "OFF"
    }

# result = sensorCollection.insert_many([sensorData1, sensorData2])       # upload to mongoDB
# print(result.inserted_ids)                                              # show insert ID in terminal

# show current data in mongoDB
for x in sensorCollection.find():
    print (x)


@app.route('/sensor1', methods=['POST'])
def postSensorData():
    data = request.json
    try:
        sensorCollection.insert_one(data)
        return jsonify({"message":"Data received!", "data": data}), 201
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

@app.route('/sensor1', methods=['GET'])
def getSensorData():
    try:
        tempSensorData = list(sensorCollection.find({},{"_id":0}))
        return jsonify(tempSensorData), 200
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

@app.route('/sensor1', methods=['DELETE'])
def deleteSensorData():
    try: 
        sensorCollection.delete_many({})
        return jsonify({"message":"All sensor data has been deleted"}), 201
    except Exception as e:
        return jsonify({"Error": str(e)}), 500
    
@app.route('/')
def landingPage():
    return "Landing page. Go to root /led_sensor/data"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)




