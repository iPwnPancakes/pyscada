import os

from mqtt_server.lib.mqtt.Client import Client
from mqtt_server.routes.mqtt.device import routes as mqtt_device_routes


def create_mqtt_app() -> Client:
    mqtt_client = Client(
        host=os.environ['MQTT_HOST'],
        port=int(os.environ['MQTT_PORT']),
    )

    mqtt_client.register_routes(mqtt_device_routes)

    return mqtt_client
