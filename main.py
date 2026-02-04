import customtkinter as ctk
import pyautogui as pag
from pathlib import Path
from PIL import Image, ImageTk

""" Imagens e estéticos """
icone_caminho = Path(__file__).parent / "assets" / "unig_logo.ico"
logo_caminho = Path(__file__).parent / "assets" / "unig_logo.png"

def icone(janela): #Para corrigir o erro do ícone não iniciando junto com a janela.
    janela.iconbitmap(icone_caminho)



""" Classes """
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Automações NEAD")
        self.geometry("550x400")
        self.resizable(False, False)
        self.centralizar()
        self.after(200, lambda: icone(self))

        self.container = ctk.CTkFrame(self, fg_color= "transparent")
        self.container.pack(fill = "both", expand = True)

        self.paginas = {}

        for Pagina in (Principal, Sophia, Avauni):
            pagina = Pagina(self.container, self)
            self.paginas[Pagina] = pagina
            pagina.place(relwidth = 1, relheight = 1)

        self.mostrar_pagina(Principal)

    def mostrar_pagina(self, pagina):
        self.paginas[pagina].tkraise()


    def centralizar(self):
        self.update_idletasks()
        w = self.winfo_width()
        h = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")



class PaginaBase(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color= "transparent")
        self.controller = controller



""" Janela Principal """
class Principal(PaginaBase):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        frame = ctk.CTkFrame(self, fg_color= "transparent")
        frame.pack(expand= True)

        logo = ctk.CTkImage(light_image= Image.open(logo_caminho), dark_image= Image.open(logo_caminho), size= (100, 100))
        imagem1 = ctk.CTkLabel(frame, text="", image= logo)
        imagem1.pack(padx= 10, pady= 10)

        label = ctk.CTkLabel(frame, text="Automações para o Sistema de Gestão Academica SophiA")
        label.pack(pady=20)

        frame_botoes= ctk.CTkFrame(frame,fg_color="transparent")
        frame_botoes.pack()

        botaoSophia = ctk.CTkButton(frame_botoes, text= "Automações Sophia", command= lambda: controller.mostrar_pagina(Sophia))
        botaoSophia.grid(row= 0, column= 0, padx= 10)

        botaoAvauni = ctk.CTkButton(frame_botoes, text= "Automações Avauni", command= lambda: controller.mostrar_pagina(Avauni))
        botaoAvauni.grid(row= 0, column= 1, padx= 10)



""" Janela do Sophia """
class Sophia(PaginaBase):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(expand=True)

        ctk.CTkLabel(frame, text="Automações para o Sistema de Gestão Acadêmica SophiA"
        ).pack(pady=20)

        frame_botoes = ctk.CTkFrame(frame, fg_color="transparent")
        frame_botoes.pack()

        qnt_botoes = 8
        texto = ["Botão", "Botão", "Botão", "Botão", "Botão", "Botão", "Botão", "Botão", "Botão"]

        linha, coluna = 0, 0
        intercalar = False

        for i in range(qnt_botoes):
            btn = ctk.CTkButton(frame_botoes, text=texto[i], command="")
            btn.grid(row=linha, column=coluna, pady=10, padx=10)

            if intercalar is False:
                coluna += 1
                intercalar = True
            else:
                linha += 1
                coluna = 0
                intercalar = False

        botao_voltar = ctk.CTkButton(
            frame,
            text="Voltar",
            command=lambda: controller.mostrar_pagina(Principal)
        )
        botao_voltar.pack(pady=30)


""" Janela do AVAUni """
class Avauni(PaginaBase):
    def __init__(self, master, controller):
        super().__init__(master, controller)

        frame = ctk.CTkFrame(self, fg_color= "transparent")
        frame.pack(expand= True)

        label = ctk.CTkLabel(frame, text="Automações para a plataforma de alunos AVAUni")
        label.pack(pady=20)

        frame_botoes = ctk.CTkFrame(frame, fg_color= "transparent")
        frame_botoes.pack()

        qnt_botoes = 8
        texto = ["Botão", "Botão", "Botão", "Botão", "Botão", "Botão", "Botão", "Botão", "Botão"]
        linha, coluna = 0, 0
        intercalar = False

        for i in range(qnt_botoes):
            btn = ctk.CTkButton(frame_botoes,text= texto[i], command= "")
            btn.grid(row= linha, column = coluna, pady= 10, padx= 10)
            if intercalar == False:
                coluna += 1
                intercalar = True
            else:
                linha += 1
                coluna = 0
                intercalar = False

        botao_voltar = ctk.CTkButton(
            frame,
            text="Voltar",
            command=lambda: controller.mostrar_pagina(Principal)
        )
        botao_voltar.pack(pady=30)

if __name__ == "__main__":
    app = App()
    app.mainloop()