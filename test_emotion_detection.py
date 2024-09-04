import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_happy_statement(self):
        text = "Estou feliz que isso aconteceu"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_angry_statement(self):
        text = "Estou realmente bravo com isso"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgust_statement(self):
        text = "Fiquei enojado só de ouvir sobre isso"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sad_statement(self):
        text = "Estou tão triste com isso"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_fear_statement(self):
        text = "Estou com muito medo que isso aconteça"
        result = emotion_detector(text)
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()