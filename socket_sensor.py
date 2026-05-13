import socket
import random
import time

# Use the IP of the machine running edge_device.py
SERVER_IP = "127.0.0.1" 
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, PORT))

print(f"Connected to Edge Device at {SERVER_IP}")

while True:
    temperature = round(random.uniform(20, 35), 2)
    humidity = round(random.uniform(40, 80), 2)
    light = round(random.uniform(100, 1000), 2)

    # Format as a single string to send over the socket
    message = f"{temperature},{humidity},{light}"
    client.send(message.encode())

    print("Sent to Edge:", message)
    time.sleep(5)