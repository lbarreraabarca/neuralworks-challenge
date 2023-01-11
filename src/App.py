from sys import prefix
from flask import Flask
from com.data.factory.controllers.TripEventController import tripEventController

if __name__ == '__main__':
    PORT = 8080
    app = Flask(__name__)
    app.register_blueprint(tripEventController, url_prefix='/api/v1')
    app.run(host='127.0.0.1', port=PORT, debug=True)
