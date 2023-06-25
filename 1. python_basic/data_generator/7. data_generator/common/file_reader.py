class FileReader:
    def __init__(self):
        self.file_name = "" 
           
    def file_to_list(self, file_name):
        result = None
        with open(file_name, "r", encoding='utf-8') as file: #mode - r(read), w(write), a(append)
            result =  file.read().split(', ')
        return result