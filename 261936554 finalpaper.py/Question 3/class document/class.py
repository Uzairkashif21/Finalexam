from abc import ABC, abstractmethod

class document(ABC):
    def __init__(self, file_name, file_size, content):
        self.file_name = file_name
        self.file_size = file_size
        self.content = content

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def read(self):
        pass
    @abstractmethod
    def save(self):
        pass
