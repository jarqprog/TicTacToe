import os


class FileManager():

    DATA_DIRECTORY = "data"

    def __init__(self, file_name):
        current_dir = os.getcwd()
        file_dir = os.path.join(current_dir, self.DATA_DIRECTORY)
        self.file_name = os.path.join(file_dir, file_name)

    def set_file_name(self, file_name):
        self.file_name = file_name

    def get_file_name(self):
        return self.file_name

    def import_data(self):
        with open(self.file_name, "r") as myfile:
            imported_data = myfile.read()
            return imported_data.split("\n")

    def export_data(self, data_collection):
        with open(self.file_name, "w") as myfile:
            for line in data_collection:
                myfile.write(line)
