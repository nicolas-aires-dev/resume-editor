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
        self.title("App com múltiplas telas")
        self.geometry("600x400")
        self.tela_atual = None
        self.mostrar_tela_inicial()

    def mostrar_tela_inicial(self):
        if self.tela_atual:
            self.tela_atual.destroy()
        self.tela_atual = TelaInicial(self, on_submit=self.mostrar_tela_docx)

    def mostrar_tela_docx(self, caminho):
        if self.tela_atual:
            self.tela_atual.destroy()
        self.tela_atual = TelaDocx(self, caminho)

if __name__ == "__main__":
    app = App()
    app.mainloop()
