from docx import Document


doc = Document("./files/040326_Nicolas_Aires_Curriculo_Backend_ATS.docx")

for p in doc.paragraphs:
    print(p.text)
