from flask import Flask, jsonify, request

from converter import celsius_to_fahrenheit, miles_to_km
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/convert/temperature")
def convert_temperature():
    raw = request.args.get("celsius")
    if not raw:
        return jsonify(error="missing required parameter: celsius"), 400
    try:
        celsius = float(raw)
    except ValueError:
        return jsonify(error=f"celsius must be a number, got '{raw}'"), 400
    return jsonify(celsius=celsius, fahrenheit=celsius_to_fahrenheit(celsius))


@app.route("/convert/distance")
def convert_distance():
    raw = request.args.get("miles")
    if not raw:
        return jsonify(error="missing required parameter: miles"), 400
    try:
        miles = float(raw)
    except ValueError:
        return jsonify(error=f"miles must be a number, got '{raw}"), 400
    return jsonify(miles=miles, km=miles_to_km(miles))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)