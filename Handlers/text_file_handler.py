from ContentModerationWithPython.Handlers.base_handler import BaseHandler

class TxtFileHandler(BaseHandler):
    def __init__(self, file_path):
        self.file_path = file_path

    def get_data(self):
        with open(self.file_path, 'r') as file:
            return file.read()

    def set_data(self, data):
        self.file_path = self.file_path.replace(".","_out.")
        with open(self.file_path, 'w') as file:
            for item in data:
                file.write(item + '\n')
