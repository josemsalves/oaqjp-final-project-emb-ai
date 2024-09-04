''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the sentiment_analyzer function from the package created: TODO
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector
#Initiate the flask app : TODO
app = Flask("Sentiment Analyzer")
@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    # Obtenha o texto da requisição
    data = request.json
    text = data.get('text', '')

    # Use a função emotion_detector para processar o texto
    result = emotion_detector(text)

    # Formate a resposta da forma solicitada
    response_text = (
        f"Para a declaração dada, a resposta do sistema é "
        f"'raiva': {result['anger']}, "
        f"'nojo': {result['disgust']}, "
        f"'medo': {result['fear']}, "
        f"'alegria': {result['joy']} e "
        f"'tristeza': {result['sadness']}. "
        f"A emoção dominante é {result['dominant_emotion']}."
    )

    # Retorne a resposta como JSON
    return jsonify({
        "anger": result['anger'], 
        "disgust": result['disgust'], 
        "fear": result['fear'], 
        "joy": result['joy'], 
        "sadness": result['sadness'], 
        "dominant_emotion": result['dominant_emotion'],
        "response_text": response_text
    })

if __name__ == '__main__':
    app.run(host='localhost', port=5001)