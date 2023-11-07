import unittest

from lib.stream_processor import StreamProcessor


class Main(unittest.TestCase):
    QUESTIONS_PATH = "../data/question_and_answers.json"  # Global property for json file path

    def test_data(self):
        processor = StreamProcessor(self.QUESTIONS_PATH)
        data = processor.get_contents()
        self.assertGreater(len(data), 0)


if __name__ == '__main__':
    unittest.main()
