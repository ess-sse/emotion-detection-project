from emotion_app.emotion_detector import emotion_predictor

def test_emotion_predictor():
    result, status = emotion_predictor("I am so happy today!")
    assert status == 200
    assert result["emotion"] == "joy"
    assert "anger" in result
