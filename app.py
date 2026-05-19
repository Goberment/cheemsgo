from flask import Flask, jsonify, request
from entities.trip import Trip 


app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"succes": True, "message": "Helo world"}), 200

@app.route('/trips', methods=["GET"])
def get_all():
    try:
        trips = Trip.get_all()
        return jsonify(trips), 200
    except Exception as ex:
        return jsonify({"success": False, "message": str(ex)}), 500


@app.route('/trip/<int:trip_id>', methods=['GET'])
def get_one(trip_id):
    try:
        trip = Trip.get_one(trip_id)
        if trip is None:
            return jsonify({"error": "Trip no encontrado"}), 404
        return jsonify(trip), 200
    except Exception as ex:
        return jsonify({"success": False, "message": str(ex)}), 500

@app.route('/trip', methods=['POST'])
def save_trip():
    try:
        data = request.json
        if not data:
            return jsonify({"success": False, "message": "Datos no proporcionados"}), 400
        
        trip = Trip(name=data['name'], city=data['city'], latitude=data['latitude'], longitude=data['longitude'])
        id = trip.save()
        success = id is not None
        return jsonify(success), 201
    except Exception as ex:
        return jsonify({"success": False, "message": str(ex)}), 500

@app.route('/trip/<int:trip_id>', methods=['PUT'])
def update_trip(trip_id):
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No se recibieron datos"}), 400
 
        trip = Trip(
            name=data['name'],
            city=data['city'],
            latitude=data['latitude'],
            longitude=data['longitude']
        )
        rows = trip.update(trip_id)
        if rows == 0:
            return jsonify({"error": "Trip no encontrado"}), 404
        return jsonify({"success": True, "updated": rows}), 200
 
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500


@app.route('/trip/<int:trip_id>', methods=['DELETE'])
def delete_trip(trip_id):
    try:
        rows = Trip.delete(trip_id)
        if rows == 0:
            return jsonify({"error": "Trip no encontrado"}), 404
        return jsonify({"success": True, "deleted": rows}), 200
    except Exception as ex:
        return jsonify({"error": str(ex)}), 500
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
 
