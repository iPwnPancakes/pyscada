from flask_app.lib.mqtt.Router import Router

routes = Router()
routes.register('test', lambda message: print(message.topic + " " + str(message.payload)))
