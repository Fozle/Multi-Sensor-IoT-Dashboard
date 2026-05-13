# Multi-Sensor IoT Dashboard Extension

## Description
This project demonstrates a multi-stage IoT telemetry pipeline. It features a simulated sensor node sending data over a TCP socket, an edge device that acts as a gateway to the MQTT protocol, and a live Grafana dashboard for real-time monitoring.

## System Architecture
*   **Sensor Node (Python):** Simulates real-time data for Temperature, Humidity, and Light.
*   **Edge Device (Python):** Receives raw socket data, parses it, and publishes it to three distinct MQTT topics.
*   **MQTT Broker:** Uses the public EMQX broker (`broker.emqx.io`).
*   **Grafana Dashboard:** Visualizes the streams using Time Series and Gauge panels.

## Sensors and Data Map
| Sensor | Range | MQTT Topic | Unit |
| :--- | :--- | :--- | :--- |
| Temperature | 20 - 35 | `savonia/iot/temperature` | Celsius (°C) |
| Humidity | 40 - 80 | `savonia/iot/humidity` | Percent (%) |
| Light | 100 - 1000 | `savonia/iot/light` | lux |

## Dashboard Layout
The dashboard is designed for at-a-glance monitoring with a 4-panel configuration:
1.  **Temperature Graph:** Historical trend of thermal data.
2.  **Humidity Gauge:** Real-time percentage display.
3.  **Light Gauge:** Real-time intensity display (0-1000 lux).
4.  **Status Panel:** Large numeric readout of the current temperature.

## Reflection Question
**Why do we separate each sensor into a different MQTT topic?**

Separating sensors into individual topics provides **scalability** and **efficiency**. It allows different clients to subscribe only to the data they need. For example, a low-power mobile device might only need to monitor the "Light" level; by using separate topics, it doesn't have to waste battery or bandwidth downloading and parsing Temperature and Humidity data. This structure also makes debugging easier and allows for granular security permissions.

## How to Run
1.  **Launch the Edge Device:**
    `python edge_device.py`
2.  **Launch the Sensor Node:**
    `python socket_sensor.py`
3.  **Monitor:**
    Open your Grafana instance and ensure the MQTT data source is connected to `broker.emqx.io:1883`.<img width="960" height="540" alt="Screenshot_2" src="https://github.com/user-attachments/assets/87d7e7f3-2737-461f-a7aa-0ccd9a4e8d8b" />
<img width="960" height="514" alt="Screenshot_4" src="https://github.com/user-attachments/assets/36bdc728-b35e-4b95-85b5-e4d5d5632aba" />
<img width="960" height="540" alt="Screenshot_1" src="https://github.com/user-attachments/assets/0a5b26ca-5713-43ac-a69f-1a54dbd3a145" />
