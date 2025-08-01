from flask import Flask, request, jsonify
from emotion_app.emotion_detector import emotion_predictor

app = Flask(__name__)

@app.route("/emotion", methods=["POST"])
def detect_emotion():
    data = request.get_json()
    text = data.get("text", "") if data else ""
    result, status = emotion_predictor(text)
    return jsonify(result), status

if __name__ == "__main__":
    app.run(debug=True)
