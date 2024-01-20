from flask import Flask, jsonify

app = Flask(__name__)

airport_database = {
    "OTHH": {"Name": "Hamad International Airport", "Location": "Doha"},
    "OOMS": {"Name": "Muscat International Airport", "Location": "Muscat"},
    "VNKT": {"Name": "Tribhuwan International Airport", "Location": "Kathmandu"},
    "OMDB": {"Name": "Dubai International Airport", "Location": "Dubai"},
    "VTBS": {"Name": "Suvarnabhumi Airport", "Location": "Bangkok"},
    "WADD": {"Name": "Ngurah Rai International Airport", "Location": "Bali"}


}

@app.route('/airport/<icao_code>', methods=['GET'])
def get_airport(icao_code):
    airport = airport_database.get(icao_code)
    if airport is not None:
        return jsonify({"ICAO": icao_code, **airport})
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)