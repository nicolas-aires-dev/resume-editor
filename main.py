from docx import Document


#Abre documento
doc = Document('Seu_Documento_Aqui.docx')

#Acessa propriedades principais
props = doc.core_properties

#Ler metadados atuais
print(15*'#', 'Antes', 15*'#')
print(f"Titulo: {props.title}") #string – The name given to the resource.
print(f"Autor: {props.author}") #string – An entity primarily responsible for making the content of the resource.
print(f"Palavras-chave: {props.keywords}") #string – descriptive words or short phrases likely to be used as search terms for this document
print(f"Descrição: {props.comments}") #string – An account of the content of the resource.
print(f"Categoria: {props.category}") #string – A categorization of the content of this package. Example values might include: Resume, Letter, Financial Forecast, Proposal, or Technical Presentation.


#Altera dados
props.title = 'Titulo do documento'
props.author = 'Nome do autor'
props.keywords = 'Aqui, Ficam, As, Palavras, Chave, Separadas, Por, Virgulas, De, Até, 255, Caractéres'
props.comments = "Resumo profisssional de até 255 caractéres"
props.category = "curriculo"

print(15*'#', 'Depois', 15*'#')
print(f"Titulo: {props.title}")
print(f"Autor: {props.author}")
print(f"Palavras-chave: {props.keywords}")
print(f"Descrição: {props.comments}")
print(f"Categoria: {props.category}")

doc.save('Seu_Documento_Aqui.docx')
