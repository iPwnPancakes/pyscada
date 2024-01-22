from typing import Callable

from paho.mqtt.client import MQTTMessage


class Router:
    def __init__(self):
        self.routes = {}

    def register(self, route: str, callback: Callable[[MQTTMessage], None]) -> None:
        if route not in self.routes:
            self.routes[route] = []

        self.routes[route].append(callback)

    def subscribed_to_route(self, route: str) -> bool:
        return route in self.routes

    def route(self, message: MQTTMessage) -> None:
        if message.topic in self.routes:
            for callback in self.routes[message.topic]:
                callback(message)
