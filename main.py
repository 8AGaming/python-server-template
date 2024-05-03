from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route("/addData", methods=["POST"])
def addData():
    try:
        new_data = request.json  # Use request.json to directly parse JSON
        print(new_data)
        generate_folders_json(new_data)
        # porter_stemmer(new_data)
        # Add your processing logic here

        return jsonify({"success": True, "message": "Data received successfully"})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)})


if __name__ == "__main__":
    app.run(port=5000)
