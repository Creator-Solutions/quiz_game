import json

from lib.stream_processor import StreamProcessor


class Main(object):
    QUESTIONS_PATH = "./data/question_and_answers.json"  # Global property for json file path

    def __init__(self) -> None:
        self.processor = StreamProcessor(self.QUESTIONS_PATH)
        self.data = []
        self.question_count = 1
        self.option_count = 1
        self.answers = []

    """
     Main run method -> Handles all logic for game
     :param None
     :return None
    """
    def run(self):
        self.data = self.processor.get_contents()

        # Initial Loop over the JSON data
        for question in self.data:
            print(self.question_count, ".", question['question'])
            self.option_count = 1
            for option in question['options']:
                print('\t', self.option_count, option)
                self.option_count += 1

            # Prompt user for answer
            # validate answer based on data provided
            answer = input("Enter your answer: ")
            if answer == question['correct_answer']:
                self.answers.append(answer)
                self.question_count += 1
            else:
                self.question_count += 1

        # Create another loop and display correct and incorrect answers
        print("=================Results=================\n")

        for question in self.data:
            print(self.question_count, ".", question['question'])
            self.option_count = 1
            for option in question['options']:
                if not option == question['correct_answer']:
                    print('\t', self.option_count, option, ' x')
                    self.option_count += 1
                else:
                    print('\t', self.option_count, option, ' \u2713')
                    self.option_count += 1

        # Calculate user's mark based on correct answers
        marks = f"{len(self.answers)}/10"
        print(f"Your Total mark: {marks}")


if __name__ == "__main__":
    main = Main()
    main.run()
