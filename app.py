from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/v1.0/predict", methods=["GET"])
def prediction():
    try:
        a = float(request.args.get("a", 0))
    except (ValueError, TypeError):
        a = 0

    try:
        b = float(request.args.get("b", 0))
    except (ValueError, TypeError):
        b = 0

    suma = a + b
    prediction = 1 if suma > 5.8 else 0

    return jsonify({
        "prediction": prediction,
        "features": {
            "a": a,
            "b": b,
            "suma": suma
        }
    })

if __name__ == '__main__':
    app.run()
