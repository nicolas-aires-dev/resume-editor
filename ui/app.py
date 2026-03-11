import customtkinter as ctk
from tkinter import filedialog


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
