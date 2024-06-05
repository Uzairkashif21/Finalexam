class pdfDocument(document):
    def open(self):
        print(f"open pdfdocument:{self.file_name}")

    def read(self):
        print(f"read pdfdocument:{self.file_name}")

    def save(self):
        print(f"save pdfdocument:{self.file_name}")
