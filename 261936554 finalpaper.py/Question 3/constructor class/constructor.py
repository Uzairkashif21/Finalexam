word_doc = documentfactory.create_document("word", "uzair.docx", "19MB", "Word content")
pdf_doc = documentFactory.create_document("pdf", "uzair.pdf", "9MB", "PDF content")
excel_doc = documentFactory.create_document("excel", "uzair.excel", "5MB", "Excel content")


#word
word_doc.open()
word_doc.read()
word_doc.save()

#pdf
pdf_doc.open()
pdf_doc.read()
pdf_doc.save()

#excel 
excel_doc.open()
excel_doc.read()
excel_doc.save()
