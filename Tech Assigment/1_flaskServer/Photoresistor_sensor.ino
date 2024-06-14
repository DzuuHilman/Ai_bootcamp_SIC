#include <WiFi.h>
#include <HTTPClient.h>   // Connect esp to http
#include <NTPClient.h>    // synchronize time between esp and real world(NTP server)
#include <WiFiUdp.h>      // help processing NTP

#define photoResistor 34
#define LED 22
const int sensorThreshold = 500;
int sensor_value;
String ledCondition;
String timestamp;

// NTP Setup
WiFiUDP ntpUDP;
NTPClient timeClient(ntpUDP, "time.google.com", 7 * 3600, 60000);   //NTP URL, UTC time (second), interval time

// WiFi Credential
const char* ssid = "Hey hey";
const char* password = "aingmaung";
  
// Server adress 
const char* serverName = "http://192.168.179.107:5000/led_sensor/data";    // Don't forget to change to corresponding IP 

// Wifi Setup
void wifiSetup(){
  // Connection attempt
  WiFi.begin(ssid, password);
  Serial.print("Connecting to WiFi...");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(1000);
  }
  Serial.println("Connected to WiFi!");

}
void checkSensorData(){
  Serial.print("Sensor value = ");
  Serial.println(sensor_value);
}
void checkTimestampValue(){
  Serial.print("Timestamp = ");
  Serial.println(timestamp);
}

void setup() {
  Serial.begin(115200);
  wifiSetup();        //Initialize WiFi
  timeClient.begin(); //Initialize timestamp

  pinMode(LED, OUTPUT);
  pinMode(photoResistor, INPUT);
  Serial.println("Photoresistor start!");
}

void loop() {
  // Receive data from sensor
  sensor_value = analogRead(photoResistor);
  if (sensor_value < sensorThreshold) {
    ledCondition = "ON";
    digitalWrite(LED, HIGH);
    //checkSensorData();
  }
  else {
    ledCondition = "OFF";
    digitalWrite(LED, LOW);
    //checkSensorData();
  }

  // Config timestamp 
  timeClient.update();
  timestamp = timeClient.getFormattedTime();
  //checkTimestampValue();

  // Check WiFi
  if (WiFi.status() == WL_CONNECTED){
    HTTPClient http;

    if (isnan(sensor_value)){
      Serial.println("Failed to read sensor data...");
      return;
    }
  

    // Activate HTTP connection
    http.begin(serverName);
    http.addHeader("Content-Type", "application/json");

    // Create JSON data
     String httpRequestData = "{\"timestamp\":\"" + String(timestamp) + "\", \"sensor_value\":" + sensor_value + ", \"ledCondition\":\"" + String(ledCondition)  + "\"}";

    // Send JSON data to server
    int httpResponseCode = http.POST(httpRequestData);
    Serial.println("Sending data...");

    //Check response. If httpResponseCode < 0, there's internal connection problem 
    if (httpResponseCode > 0){    
      String serverResponse = http.getString();
      Serial.print("HTTP Response code is ");
      Serial.println(httpResponseCode);
      Serial.print("Body data sent: ");
      Serial.println(serverResponse);
      Serial.println("Data has been sent!");
    }
    else {
    Serial.print("Failed to POST data. Error code: ");
    Serial.println(httpResponseCode);
    }

    // End HTTP connection
    http.end();
  }
  else {
    Serial.println("WiFi disconnected.");
  }

  delay(10000);
}
