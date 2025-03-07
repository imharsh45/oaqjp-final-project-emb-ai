import unittest  # Import unittest for writing unit tests
from EmotionDetection.emotion_detection import emotion_detector  # Import the function to test

class TestEmotionDetection(unittest.TestCase):
    """Unit tests for the emotion_detector function."""

    def test_joy(self):
        response = emotion_detector("I am glad this happened")
        self.assertEqual(response["dominant_emotion"], "joy")

    def test_anger(self):
        response = emotion_detector("I am really mad about this")
        self.assertEqual(response["dominant_emotion"], "anger")

    def test_disgust(self):
        response = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(response["dominant_emotion"], "disgust")

    def test_sadness(self):
        response = emotion_detector("I am so sad about this")
        self.assertEqual(response["dominant_emotion"], "sadness")

    def test_fear(self):
        response = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(response["dominant_emotion"], "fear")

# Run the unit tests
if __name__ == '__main__':
    unittest.main()
