def emotion_predictor(text_to_analyze):
    if not text_to_analyze.strip():
        return {"error": "Input text cannot be empty"}, 400

    # Dummy prediction (normally you'd call Watson API here)
    return {
        "emotion": "joy",
        "anger": 0.1,
        "joy": 0.7,
        "sadness": 0.05,
        "fear": 0.1,
        "disgust": 0.05
    }, 200
