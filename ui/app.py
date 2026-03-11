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

        #Abertura e processamento de dados
        doc = Document(caminho)
        props = doc.core_properties

        #Metadata
        lbl_title = ctk.CTkLabel(self, text=f"Titúlo: {props.title}")
        lbl_title.pack(pady=5)

        lbl_author = ctk.CTkLabel(self, text=f"Autor: {props.author}")
        lbl_author.pack(pady=5)

        lbl_keywords = ctk.CTkLabel(self, text=f"Palavras-chave: {props.keywords}")
        lbl_keywords.pack(pady=5)

        lbl_description = ctk.CTkLabel(self, text=f"Descrição: {props.comments}")
        lbl_description.pack(pady=5)

        lbl_category = ctk.CTkLabel(self, text=f"Titúlo: {props.category}")
        lbl_category.pack(pady=5)
        
        self.label = ctk.CTkLabel

