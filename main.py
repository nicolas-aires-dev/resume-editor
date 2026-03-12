import customtkinter as ctk
from tkinter import filedialog
from docx import Document
from PIL import Image, ImageTk


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
    def __init__(self, master, path):
        super().__init__(master)
        self.pack(padx=20, pady=20, fill='both', expand=True)

        #Open docs
        self.doc = Document(path)
        self.path = path
        props = self.doc.core_properties

        # Title
        lbl_title = ctk.CTkLabel(self, text="Título:")
        lbl_title.grid(row=0, column=0, sticky="w", padx=5, pady=5)

        self.entry_title = ctk.CTkEntry(self, width=400)
        self.entry_title.insert(0, props.title)
        self.entry_title.grid(row=0, column=1, padx=5, pady=5)

        # Author
        lbl_author = ctk.CTkLabel(self, text="Autor:")
        lbl_author.grid(row=1, column=0, sticky="w", padx=5, pady=5)

        self.entry_author = ctk.CTkEntry(self, width=400)
        self.entry_author.insert(0, props.author)
        self.entry_author.grid(row=1, column=1, padx=5, pady=5)

        # Keywords
        lbl_keywords = ctk.CTkLabel(self, text="Palavras-chave:")
        lbl_keywords.grid(row=2, column=0, sticky="w", padx=5, pady=5)

        self.entry_keywords = ctk.CTkEntry(self, width=400)
        self.entry_keywords.insert(0, props.keywords)
        self.entry_keywords.grid(row=2, column=1, padx=5, pady=5)

        # Description
        lbl_description = ctk.CTkLabel(self, text="Descrição:")
        lbl_description.grid(row=3, column=0, sticky="w", padx=5, pady=5)

        self.entry_description = ctk.CTkEntry(self, width=400)
        self.entry_description.insert(0, props.comments)
        self.entry_description.grid(row=3, column=1, padx=5, pady=5)

        # Category
        lbl_category = ctk.CTkLabel(self, text="Categoria:")
        lbl_category.grid(row=4, column=0, sticky="w", padx=5, pady=5)

        self.entry_category = ctk.CTkEntry(self, width=400)
        self.entry_category.insert(0, props.category)
        self.entry_category.grid(row=4, column=1, padx=5, pady=5)

        # Botão salvar
        btn_salvar = ctk.CTkButton(self, text="Salvar alterações", command=self.salvar_props)
        btn_salvar.grid(row=5, column=0, columnspan=2, pady=10, sticky="w")

        # Botão voltar
        btn_voltar = ctk.CTkButton(self, text="Voltar", command=lambda: master.mostrar_tela_inicial())
        btn_voltar.grid(row=6, column=0, columnspan=2, pady=10, sticky="w")


    def salvar_props(self):
        props = self.doc.core_properties
        props.title = self.entry_title.get()
        props.author = self.entry_author.get()
        props.keywords = self.entry_keywords.get()
        props.comments = self.entry_description.get()
        props.category = self.entry_category.get()

        #Save doc
        self.doc.save(self.path)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Resume Editor")
        self.geometry("600x400")
        self.tela_atual = None
        self.resizable(False, False)  # trava a dimensão
        self.mostrar_tela_inicial()

        self.iconbitmap("common/logos/Logo.ico")

    def mostrar_tela_inicial(self):
        if self.tela_atual:
            self.tela_atual.destroy()
        self.tela_atual = TelaInicial(self, on_submit=self.mostrar_tela_docx)

    def mostrar_tela_docx(self, path):
        if self.tela_atual:
            self.tela_atual.destroy()
        self.tela_atual = TelaDocx(self, path)

if __name__ == "__main__":
    app = App()
    app.mainloop()
