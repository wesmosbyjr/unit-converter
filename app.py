from flask import Flask, jsonify, request

from converter import celsius_to_fahrenheit, miles_to_km

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/convert/temperature")
def convert_temperature():
    celsius = float(request.args.get("celsius"))
    return jsonify(celsius=celsius, fahrenheit=celsius_to_fahrenheit(celsius))


@app.route("/convert/distance")
def convert_distance():
    miles = float(request.args.get("miles"))
    return jsonify(miles=miles, km=miles_to_km(miles))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)