from flask import Flask, request, jsonify

app = Flask(__name__)

database = [
    {
        "Timestamp": "16:40:00",
        "Sensor value": 500,
        "LED condition": "ON"
    }
]

@app.route('/sensor1', methods=['POST'])
def postSensorData():
    data = request.json
    timestamp = data.get("timestamp")
    sensor_value = data.get("sensor_value")
    ledCondition = data.get("ledCondition")
    database.append(
        {"Timestamp": timestamp, 
         "Sensor value": sensor_value,
         "LED condition": ledCondition}
        )
    print("Data received!")
    
    return jsonify({"message":"Data received!", "timestamp": timestamp, "sensor_value": sensor_value, "ledCondition": ledCondition})

@app.route('/sensor1', methods=['GET'])
def getSensorData():
    print("Data exported sucsessfully!")
    return jsonify(database)

@app.route('/')
def landingPage():
    return "Landing page. Go to root /led_sensor/data"
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

