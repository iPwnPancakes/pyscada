from typing import List, Dict, Callable

import paho.mqtt.client as mqtt
from paho.mqtt.client import MQTTMessage

from flask_app.lib.mqtt.Router import Router


class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.routers: List[Router] = []
        self.routes: Dict[str, List[Callable[[MQTTMessage], None]]] = {}

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code " + str(rc))
        for router in self.routers:
            for route in router.routes:
                self.routes[route] = router.routes[route]
                client.subscribe(route)

    def on_message(self, client, userdata, msg):
        for router in self.routers:
            if router.subscribed_to_route(msg.topic):
                router.route(msg)

    def register_routes(self, router: Router):
        self.routers.append(router)

    def run(self):
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.connect_async(self.host, self.port, 60)
        client.loop_start()
