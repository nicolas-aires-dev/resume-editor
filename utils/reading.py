from docx import Document


#Abre documento
doc = Document('./files/Seu_curriculo_aqui.docx')

#Acessa propriedades principais
props = doc.core_properties

#Lê metadados atuais
print(15*'#', 'Os Metadados do arquivo são:', 15*'#')
print(f"Titulo: {props.title}")
print(f"Autor: {props.author}")
print(f"Palavras-chave: {props.keywords}")
print(f"Descrição: {props.comments}")
print(f"Categoria: {props.category}")
