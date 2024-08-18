'''
Написати структуру класів, яка буде представляти роботу з файлами. Вона має працювати з файлами, які і
читаються і записуються і працювати з файлами, які будуть лише читатись
'''

# class FileOperations:
#     def __init__(self, file_path: str) -> None:
#         self.file_path = file_path

#     def write(self, data: str):
#         with open(self.file_path, 'w') as f:
#             f.write(data)

#     def read(self):
#         with open(self.file_path, 'r') as f:
#             return f.read()
        

# class FileReadOnlyOperations(FileOperations):
#     def write(self, data: str):
#         raise TypeError

class FileWriteOperations:
    
    def write(self, file_path, data: str):
        with open(file_path, 'w') as f:
            f.write(data)


class FileReadOperations:

    def read(self, file_path):
        with open(file_path, 'r') as f:
            return f.read()
        

class FileOperations(FileReadOperations, FileWriteOperations):
    pass
