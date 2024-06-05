class documentFactory:
    def create_document(doc_type, file_name,file_size,content):
        if doc_type == "word":
            return wordDocument(file_name,file_size,content)
        elif doc_type == "pdf":
            return pdfDocument(file_name,file_size,content)
        elif doc_type == "excel":
            return excelDocument(file_name,file_size,content)
        else:
             error(f"Unknown document type: {doc_type}")
