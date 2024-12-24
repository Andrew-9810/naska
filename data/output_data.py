import json


class ReadeFile:
    def __init__(self, file):
        self.file = file
        self.read_file()
        self.data = {}


    def read_file(self):
        with open(self.file, "r") as read_file:
            self.data = json.load(read_file)


    def writer_file(self):
        with open(self.file, 'w') as outfile:
            json.dump(self.data, outfile)

