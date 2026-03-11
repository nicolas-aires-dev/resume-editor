import customtkinter as ctk
from ui.app import TelaInicial
from docx import Document


def processar_docx(caminho):    
    #Open document
    doc = Document(caminho) 

    props = doc.core_properties

     
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Resume Editor")
        self.geometry("500x300")

        TelaInicial(self, on_submit=processar_docx)

if __name__ == "__main__":
    app = App()
    app.mainloop()
