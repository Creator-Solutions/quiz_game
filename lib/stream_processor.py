import json


class StreamProcessor(object):
    def __init__(self, path) -> None:
        self.path = path
        self.data = []

    """
     Checks path of file
     For debugging purposes
     :param None
     :return str
    """
    def get_path(self) -> str:
        return self.path

    """
     Reads json data from file
     :param None
     :return List
    """
    def get_contents(self):
        with open(self.path, 'r') as json_file:
            self.data = json.load(json_file)

        return self.data

