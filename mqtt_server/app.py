from dotenv import load_dotenv

from mqtt_server.factory import create_mqtt_app

load_dotenv()

mqtt = create_mqtt_app()
mqtt.run()
