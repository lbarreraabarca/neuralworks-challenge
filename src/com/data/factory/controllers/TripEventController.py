from flask import Blueprint, request
from com.data.factory.services.TripEventService import TripEventService

tripEventController = Blueprint('TripEventController', __name__)

@tripEventController.route('/trip-event/insert', methods=['POST'])
def insert():
    service = TripEventService()
    return service.insert(request.get_json())

@tripEventController.route('/trip-event/trip-per-week', methods=['POST'])
def getTripPerWeek():
    service = TripEventService()
    return service.getTripPerWeek(request.get_json())
