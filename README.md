# What is this?

This project was created as a way for me to refresh my knowledge on python, as well as to showcase the things I've
learned about how SCADAs work thus far.

# The "Architecture"

This project is made up of 3 main components:

- The Flask app
- The Modbus server
- The MQTT listening process

![architecture.png](readme_assets%2Farchitecture.png)

## The Flask App

This is the bulk of the functionality. It contains a REST API that mainly stores Device/Tag associations, as well as
their respective configurations for things like a Device's network configuration or the different communication protocol
configurations associated with a Tag.

The Flask app runs on the default port of 5000.

## The Modbus server

This is a very simple modbus server, mainly meant to serve a simple store of values that are read/written to via Modbus.
It runs on localhost:8502

## The MQTT listening process

This process is responsible for subscribing to each Device's MQTT topic, and parsing/handling the message. Each message
is assumed to be JSON, and all invalid JSON will be ignored. It checks the keys on the JSON object and against a
matching Tag's MQTT configuration and performs a Modbus write on the Tag's Modbus configuration.

# How do I start this thing?

## Flask App

Make sure you have a SQLite database initialized:

```bash
touch ./flask_app/instance/db.sqlite
```

Copy the example .env file and fill it out:

```bash
cp ./flask_app/.env.example ./flask_app/.env
```

Start it by running:

```bash
source venv/bin/activate && cd flask_app && flask run
```

## Modbus App

To start the Modbus app:

```bash
source venv/bin/activate && cd modbus_server && python3 ./server.py 
```

## MQTT Listener App

Make sure that you have Mosquitto installed on your local machine, here is the command for linux:

```bash
sudo apt-get install mosquitto
```

Copy the example .env file and fill it out:

```bash
cp ./mqtt_server/.env.example ./mqtt_server/.env
```

To start the MQTT app:

```bash
source venv/bin/activate && cd mqtt_server && python3 ./app.py
```
