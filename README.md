# What is this?

This project was created as a way for me to refresh my knowledge on python, as well as to showcase the things I've
learned about how SCADAs work thus far.

# The "Architecture"

This project is made up of 3 main components:

- The Flask app
- The Modbus server
- The MQTT listening process

![architecture.png](readme_assets%2Farchitecture.png)

# The Flask App

This is the bulk of the functionality. It contains a REST API that mainly stores Device/Tag associations, as well as
their respective configurations for things like a Device's network configuration or the different communication protocol
configurations associated with a Tag.

The Flask app runs on the default port of 5000.

# The Modbus server

This is a very simple modbus server, mainly meant to serve a simple store of values that are read/written to via Modbus.
It runs on localhost:8502

# The MQTT listening process

This process is responsible for subscribing to each Device's MQTT topic, and parsing/handling the message. Each message
is assumed to be JSON, and all invalid JSON will be ignored. It checks the keys on the JSON object and against a
matching Tag's MQTT configuration and performs a Modbus write on the Tag's Modbus configuration.
