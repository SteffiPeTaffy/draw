#include <WiFiManager.h>
#include <PubSubClient.h>
#include <Adafruit_GFX.h>
#include <Adafruit_NeoMatrix.h>
#include <Adafruit_NeoPixel.h>
#include <HTTPUpdate.h>

#define PIN 4

const char* MQTT_SERVER = "broker.emqx.io";
const uint16_t MQTT_PORT = 1883;

Adafruit_NeoMatrix matrix = Adafruit_NeoMatrix(16, 16, PIN,
  NEO_MATRIX_TOP     + NEO_MATRIX_LEFT +
  NEO_MATRIX_COLUMNS + NEO_MATRIX_ZIGZAG,
  NEO_GRB            + NEO_KHZ800);

WiFiClient wifiClient;
PubSubClient mqttClient(wifiClient);
String clientId;

const char DRAW_TOPIC[] = "lieblingswelt/draw";
const char  CONNECT_TOPIC[] = "lieblingswelt/draw/connect";
const char UPDATE_TOPIC[] = "lieblingswelt/draw/update";

uint8_t data[16][16][3] = {0};

void startWifi() {
  Serial.println("Connecting Wifi");

  WiFiManager wifiManager;
  wifiManager.setDebugOutput(false);
  wifiManager.setEnableConfigPortal(false);
  wifiManager.setTimeout(0);
  uint8_t i = 0;
  while(!wifiManager.autoConnect("draw", "drawdraw") && i++ < 3) {
    Serial.println("Retry autoConnect");
    WiFi.disconnect();
    WiFi.mode(WIFI_OFF);
  }
  if(!WiFi.isConnected()) {
    wifiManager.setEnableConfigPortal(true);
    wifiManager.autoConnect("draw", "drawdraw");
  }

  Serial.print("WiFi connected with IP: "); Serial.println(WiFi.localIP());
}

void setup() {
  Serial.begin(115200);

  matrix.begin();
  matrix.setBrightness(30);
  matrix.setRotation(1);
  matrix.fill(0);
  matrix.show();

  startWifi();

  String clientId = "ESP32Client-";
  clientId += String(random(0xffff), HEX);

  mqttClient.setServer(MQTT_SERVER, MQTT_PORT);
  mqttClient.setCallback(callback);
}

void sync() {
  Serial.print("Sync: ");
  uint8_t payload[5];
  for(uint8_t x = 0; x < matrix.width(); x++) {
    for(uint8_t y = 0; y < matrix.height(); y++) {
      if(data[x][y][0] == 0 && data[x][y][1] == 0 && data[x][y][2] == 0) {
        Serial.print(".");
        continue;
      }
      payload[0] = x;
      payload[1] = y;
      payload[2] = data[x][y][0];
      payload[3] = data[x][y][1];
      payload[4] = data[x][y][2];
      mqttClient.publish(DRAW_TOPIC, payload, sizeof(payload));
      Serial.print(",");
    }
  }
  Serial.println();
}

void callback(char* topic, byte* message, unsigned int length) {
  Serial.print("Message arrived on topic: ");
  Serial.println(topic);

  if (strcmp(topic, DRAW_TOPIC) == 0) {
    if(length != 5) {
      Serial.print("Wrong msg size: ");
      Serial.println(length);
      return;
    }
    
    uint8_t x = message[0];
    uint8_t y = message[1];
    uint16_t color = matrix.Color(message[2], message[3], message[4]);

    if(x >= matrix.width() || y >= matrix.height()) {
      Serial.printf("Invalid coordinates %d,%d\n", x, y);
      return;
    }

    data[x][y][0] = message[2];
    data[x][y][1] = message[3];
    data[x][y][2] = message[4];

    matrix.drawPixel(x, y, color);
    matrix.show();
  } else if (strcmp(topic, CONNECT_TOPIC) == 0) {
    sync();
  } else if (strcmp(topic, UPDATE_TOPIC) == 0) {
    update(message);
  } else {
    Serial.print("Wrong topic?! ");
    Serial.println(topic);
  }
}

void reconnect() {
  while (!mqttClient.connected()) {
    Serial.print("Attempting MQTT connection...");
    if (mqttClient.connect(clientId.c_str())) {
      Serial.println("connected");
      mqttClient.subscribe(DRAW_TOPIC);
      mqttClient.subscribe(CONNECT_TOPIC);
      mqttClient.subscribe(UPDATE_TOPIC);
      sync();
    } else {
      Serial.print("failed, rc=");
      Serial.print(mqttClient.state());
      Serial.println(" try again in 5 seconds");
      delay(5000);
    }
  }
}

void update(byte* message) {
    Serial.printf("update to: %s\n", message);
    t_httpUpdate_return ret = httpUpdate.update(wifiClient, "https://github.com/SteffiPeTaffy/draw/releases/latest/download/firmware.bin");

    switch (ret) {
      case HTTP_UPDATE_FAILED:
        Serial.printf("HTTP_UPDATE_FAILED Error (%d): %s\n", httpUpdate.getLastError(), httpUpdate.getLastErrorString().c_str());
        break;

      case HTTP_UPDATE_NO_UPDATES:
        Serial.println("HTTP_UPDATE_NO_UPDATES");
        break;

      case HTTP_UPDATE_OK:
        Serial.println("HTTP_UPDATE_OK");
        break;
    }
}

void loop() {
  if (!mqttClient.connected()) {
    reconnect();
  }
  mqttClient.loop();
}