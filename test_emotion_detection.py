import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        result_1 = emotion_detector('I am glad this happened')
        self.assertAlmostEqual(result_1['joy'], 0.83237535, delta=0.01)

        result_2 = emotion_detector('I am really mad about this')
        self.assertAlmostEqual(result_2['anger'], 0.6674731, delta=0.01)

        result_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertAlmostEqual(result_3['disgust'], 0.9193782, delta=0.01)

        result_4 = emotion_detector('I am so sad about this ')
        self.assertAlmostEqual(result_4['sadness'], 0.9819713, delta=0.01)

        result_5 = emotion_detector('I am really afraid that this will happen')
        self.assertAlmostEqual(result_5['fear'], 0.9907291, delta=0.02)  # Adjusted delta

if __name__ == '__main__':
    unittest.main()
