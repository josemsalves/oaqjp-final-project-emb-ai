import requests
import json
def emotion_detector(text_to_analyse):
    # URL da API de análise de sentimentos
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Construindo o payload da requisição no formato esperado
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Cabeçalho personalizado especificando o ID do modelo para o serviço de análise de sentimentos
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    try:
        # Enviando uma requisição POST para a API de análise de sentimentos
        response = requests.post(url, json=myobj, headers=headers)
        
        # Verifica se a requisição foi bem-sucedida
        response.raise_for_status()
        
        # Parseando a resposta JSON da API
        formatted_response = response.json()
        
        # Extraindo as pontuações das emoções do JSON da resposta
        anger_score = formatted_response.get('anger', 0.0)
        disgust_score = formatted_response.get('disgust', 0.0)
        fear_score = formatted_response.get('fear', 0.0)
        joy_score = formatted_response.get('joy', 0.0)
        sadness_score = formatted_response.get('sadness', 0.0)
        
        # Calculando a emoção dominante
        scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        
        dominant_emotion = max(scores, key=scores.get)
        
        # Criando o formato de saída desejado
        result = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
        
        return result

    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP: {http_err}")
        return None
    except Exception as err:
        print(f"Outro erro: {err}")
        return None

# Exemplo de uso
result = emotion_detector("I am feeling great today!")
print(result)