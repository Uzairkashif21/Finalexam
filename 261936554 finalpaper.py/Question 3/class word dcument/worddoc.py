class wordDocument(document):
    def open(self):
        print(f"open worddocument:{self.file_name}")

    def read(self):
        print(f"read worddocument:{self.file_name}")

    def save(self):
        print(f"save worddocument:{self.file_name}")
        
