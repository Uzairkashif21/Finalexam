class exceldocument(document):
    def open(self):
        print(f"Open exceldocument:{self.file_name}")

    def read(self):
        print(f"read exceldocument:{self.file_name}")

    def save(self):
        print(f"save exceldocument:{self.file_name}")
