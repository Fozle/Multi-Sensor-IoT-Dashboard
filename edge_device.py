import socket
import paho.mqtt.client as mqtt

HOST = "0.0.0.0" # Listen on all network interfaces
PORT = 5000
BROKER = "broker.emqx.io"

# Setup MQTT
mqtt_client = mqtt.Client()
mqtt_client.connect(BROKER, 1883)

# Setup Socket Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print(f"Edge Device listening on port {PORT}...")
conn, addr = server.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break

    # Decode and split the "temp,hum,light" string
    message = data.decode()
    try:
        temp, hum, light = message.split(",")
        
        # Publish to three distinct topics
        mqtt_client.publish("savonia/iot/temperature", temp)
        mqtt_client.publish("savonia/iot/humidity", hum)
        mqtt_client.publish("savonia/iot/light", light)

        print(f"Forwarded to MQTT: Temp={temp}, Hum={hum}, Light={light}")
    except ValueError:
        print("Received malformed data")