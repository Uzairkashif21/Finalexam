

































































from abc import ABC, abstractmethod

class Document(ABC):
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
Word Document Class
python
Copy code
class WordDocument(Document):
    def open(self):
        print(f"Opening Word document: {self.file_name}")

    def read(self):
        print(f"Reading Word document: {self.file_name}")

    def save(self):
        print(f"Saving Word document: {self.file_name}")
PDF Document Class
python
Copy code
class PDFDocument(Document):
    def open(self):
        print(f"Opening PDF document: {self.file_name}")

    def read(self):
        print(f"Reading PDF document: {self.file_name}")

    def save(self):
        print(f"Saving PDF document: {self.file_name}")
Excel Document Class
python
Copy code
class ExcelDocument(Document):
    def open(self):
        print(f"Opening Excel document: {self.file_name}")

    def read(self):
        print(f"Reading Excel document: {self.file_name}")

    def save(self):
        print(f"Saving Excel document: {self.file_name}")
DocumentFactory Class
python
Copy code
class DocumentFactory:
    @staticmethod
    def create_document(doc_type, file_name, file_size, content):
        if doc_type == "word":
            return WordDocument(file_name, file_size, content)
        elif doc_type == "pdf":
            return PDFDocument(file_name, file_size, content)
        elif doc_type == "excel":
            return ExcelDocument(file_name, file_size, content)
        else:
            raise ValueError(f"Unknown document type: {doc_type}")
Example Script
python
Copy code
# Example script demonstrating the creation and handling of different documents

# Creating documents using the DocumentFactory
word_doc = DocumentFactory.create_document("word", "document1.docx", "15MB", "Word content")
pdf_doc = DocumentFactory.create_document("pdf", "document2.pdf", "10MB", "PDF content")
excel_doc = DocumentFactory.create_document("excel", "document3.xlsx", "20MB", "Excel content")

# Handling Word Document
word_doc.open()
word_doc.read()
word_doc.save()

# Handling PDF Document
pdf_doc.open()
pdf_doc.read()
pdf_doc.save()

# Handling Excel Document
excel_doc.open()
excel_doc.read()
excel_doc.save()
Summary
