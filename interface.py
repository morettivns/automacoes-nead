import customtkinter as ctk
import pyautogui as pag
from pathlib import Path
from PIL import Image, ImageTk

icone_caminho = Path(__file__).parent / "assets" / "unig_logo.ico"
logo_caminho = Path(__file__).parent / "assets" / "unig_logo.png"
def icone(janela):
    janela.iconbitmap(icone_caminho)

class JanelaBase(ctk.CTkToplevel):
    def __init__(self, master, titulo, tamanho="550x400"):
        super().__init__(master)

        self.master = master
        self.title(titulo)
        self.geometry(tamanho)
        self.resizable(False, False)

        #Estético
        self.centralizar()
        self.after(200, lambda: icone(self))

        #Fecha corretamente
        self.protocol("WM_DELETE_WINDOW", self.fechar)

    #GPT fez para centralizar a janela quando abrir a aplicação.
    def centralizar(self):
        self.update_idletasks()
        w = self.winfo_width()
        h = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")

    def fechar(self):
        self.destroy()
        self.master.deiconify()

class JanelaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Automações NEAD")
        self.geometry("500x300")
        self.resizable(False, False)

        self.centralizar()

        logo = ctk.CTkImage(light_image= Image.open(logo_caminho), dark_image= Image.open(logo_caminho), size= (100, 100))
        imagem1 = ctk.CTkLabel(self, text="", image= logo)
        imagem1.pack(padx= 10, pady= 10)

        texto1 = ctk.CTkLabel(self, text= "Software contendo automações para conclusão de processos praticados no Núcleo de Ensino a Distância da Universidade Iguaçu - NEAD UNIG", width= 500, height= 50, wraplength= 450)
        texto1.pack()

        frame_botoes = ctk.CTkFrame(self, fg_color= "transparent")
        frame_botoes.pack(pady = 30)

        botao1 = ctk.CTkButton(frame_botoes, text="Automações SophiA", command=self.abrir_janela_sophia)
        botao1.grid(row = 0, column= 0, padx = 10)

        botao2 = ctk.CTkButton(frame_botoes, text="Automações AVAUni", command=self.abrir_janela_avauni)
        botao2.grid(row = 0, column= 1, padx = 10)

    def centralizar(self):
        self.update_idletasks()
        w = self.winfo_width()
        h = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")

    def abrir_janela_sophia(self):
        self.withdraw()
        JanelaSophia(self)

    def abrir_janela_avauni(self):
        self.withdraw()
        JanelaAvauni(self)

class JanelaSophia(JanelaBase):
    def __init__(self, master):
        super().__init__(master, "Janela A")

        label = ctk.CTkLabel(self, text="Automações para o Sistema de Gestão Academica SophiA")
        label.pack(pady=20)

        frame_botoes= ctk.CTkFrame(self,fg_color="transparent")
        frame_botoes.pack()

        botao1 = ctk.CTkButton(frame_botoes, text= "Procurar aluno", command= "")
        botao1.grid(row= 0, column= 0, padx= 10, pady= 10)

        botao2 = ctk.CTkButton(frame_botoes, text= "Procurar aluno", command= "")
        botao2.grid(row= 0, column= 1, padx= 10, pady= 10)

        botao3 = ctk.CTkButton(frame_botoes, text= "Procurar aluno", command= "")
        botao3.grid(row= 1, column= 0, padx= 10, pady= 10)

        botao4 = ctk.CTkButton(frame_botoes, text= "Procurar aluno", command= "")
        botao4.grid(row= 1, column= 1, padx= 10, pady= 10)

        botao5 = ctk.CTkButton(frame_botoes, text= "Procurar aluno", command= "")
        botao5.grid(row= 2, column= 0, padx= 10, pady= 10)

        botao6 = ctk.CTkButton(frame_botoes, text= "Procurar aluno", command= "")
        botao6.grid(row= 2, column= 1, padx= 10, pady= 10)

        botao7 = ctk.CTkButton(frame_botoes, text= "Procurar aluno", command= "")
        botao7.grid(row= 3, column= 0, padx= 10, pady= 10)

        botao8 = ctk.CTkButton(frame_botoes, text= "Procurar aluno", command= "")
        botao8.grid(row= 3, column= 1, padx= 10, pady= 10)



class JanelaAvauni(JanelaBase):
    def __init__(self, master):
        super().__init__(master, "Janela B")

        self.geometry("500x300")
        self.centralizar(self)


        label = ctk.CTkLabel(self, text="Automações para a plataforma de alunos AVAUni")
        label.pack(pady=20)

if __name__ == "__main__":
    app = JanelaPrincipal()
    app.mainloop()