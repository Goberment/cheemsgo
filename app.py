from flask import Flask, jsonify, request
from entities.trip import Trip 


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"succes": True, "message": "Helo world"}), 200

@app.route('/trips', methods=["GET"])
def get_all_trips():
    trips = Trip.get_all()
    return jsonify(trips), 200

@app.route('/trip/<int:trip_id>', methods=['GET'])
def get_single_trip(trip_id):
    trip = Trip.get_by_id(trip_id)
    return jsonify(trip), 200

@app.route('/trip', methods=['POST'])
def save_trip():
    data = request.json
    trip = Trip(name=data['name'], city=data['city'], latitude=data['latitude'], longitude=data['longitude'])
    id = trip.save()
    success = id is not None
    return jsonify(success), 201

@app.route('/trip/<int:trip_id>', methods=['PUT'])
def update_trip(trip_id):
    data = request.json
    trip = Trip(
        name=data['name'],
        city=data['city'],
        latitude=data['latitude'],
        longitude=data['longitude']
    )
    rows = trip.update(trip_id)
    return jsonify({"updated": rows > 0}), 200


@app.route('/trip/<int:trip_id>', methods=['DELETE'])
def delete_trip(trip_id):
    rows = Trip.delete(trip_id)
    return jsonify({"deleted": rows > 0}), 200


if __name__ == "__main__":
    app.run(host = ('0.0.0.0'), port=5000)
from flask import Flask, jsonify, request
from entities.trip import Trip 


