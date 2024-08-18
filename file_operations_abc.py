from abc import ABC, abstractmethod

# class FileOperations(ABC):

#     @abstractmethod
#     def write(self, data: str):
#         pass

#     @abstractmethod
#     def read(self):
#         pass


# class FileReadOnlyOperations(FileOperations):
#     def write(self, data: str):
#         raise TypeError

class FileWriteOperations(ABC):
    
    @abstractmethod
    def write(self, file_path, data: str):
        pass


class FileReadOperations(ABC):

    @abstractmethod
    def read(self, file_path):
        pass
        

class FileOperations(FileReadOperations, FileWriteOperations):
    pass
