import customtkinter as ctk
from tkinter import filedialog
from docx import Document


class TelaInicial(ctk.CTkFrame):
    def __init__(self, master, on_submit):
        super().__init__(master)
        self.pack(padx=20, pady=20, fill="both", expand=True)

        self.label = ctk.CTkLabel(self, text="Selecione o arquivo DOCX:")
        self.label.pack(pady=10)

        self.entry = ctk.CTkEntry(self, width=300)
        self.entry.pack(pady=10)

        self.btn_browse = ctk.CTkButton(self, text="Procurar", command=self.browse_file)
        self.btn_browse.pack(pady=5)

        self.btn_submit = ctk.CTkButton(self, text="Confirmar", command=lambda: on_submit(self.entry.get()))
        self.btn_submit.pack(pady=10)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Documentos Word", "*.docx")])
        if file_path:
            self.entry.delete(0, "end")
            self.entry.insert(0, file_path)
        
     
class TelaDocx(ctk.CTkFrame):
    def __init__(self, master, caminho):
        super().__init__(master)
        self.pack(padx=20, pady=20, fill='both', expand=True)

        doc = Document(caminho)
        props = doc.core_properties

        #Metadata
        lbl_title = ctk.CTkLabel(self, text=f"Título: {props.title}", anchor="w", justify="left", wraplength=400)
        lbl_title.pack(fill="x", padx=10, pady=5)

        lbl_author = ctk.CTkLabel(self, text=f"Autor: {props.author}", anchor="w", justify="left", wraplength=400)
        lbl_author.pack(fill="x", padx=10, pady=5)

        lbl_keywords = ctk.CTkLabel(self, text=f"Palavras-chave: {props.keywords}", anchor="w", justify="left", wraplength=400)
        lbl_keywords.pack(fill="x", padx=10, pady=5)

        lbl_description = ctk.CTkLabel(self, text=f"Descrição: {props.comments}", anchor="w", justify="left", wraplength=400)
        lbl_description.pack(fill="x", padx=10, pady=5)

        lbl_category = ctk.CTkLabel(self, text=f"Titúlo: {props.category}", anchor="w", justify="left", wraplength=400)
        lbl_category.pack(fill="x", padx=10, pady=5)

        #Botão de voltar
        btn_voltar = ctk.CTkButton(self, text="Voltar", command=lambda: master.mostrar_tela_inicial())
        btn_voltar.pack(pady=20)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Resume Editor")
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
