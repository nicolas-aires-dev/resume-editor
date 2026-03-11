import customtkinter as ctk
from ui.app import TelaInicial


def processar_docx(caminho):
    print(f"O usuário escolheu: {caminho}")
    # aqui você pode chamar funções que leem/processam o docx

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("App com DOCX")
        self.geometry("500x300")

        TelaInicial(self, on_submit=processar_docx)

if __name__ == "__main__":
    app = App()
    app.mainloop()
