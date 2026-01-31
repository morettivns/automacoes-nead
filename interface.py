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
        self.protocol("WM_DELETE_WINDOW", self.voltar)

    #GPT fez para centralizar a janela quando abrir a aplicação.
    def centralizar(self):
        self.update_idletasks()
        w = self.winfo_width()
        h = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f"{w}x{h}+{x}+{y}")

    def voltar(self):
        self.destroy()
        self.master.deiconify()

class JanelaPrincipal(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Automações NEAD")
        self.geometry("550x400")
        self.resizable(False, False)

        self.centralizar()

        frame = ctk.CTkFrame(self, fg_color= "transparent")
        frame.pack(expand= True)

        logo = ctk.CTkImage(light_image= Image.open(logo_caminho), dark_image= Image.open(logo_caminho), size= (100, 100))
        imagem1 = ctk.CTkLabel(frame, text="", image= logo)
        imagem1.pack(padx= 10, pady= 10)

        texto1 = ctk.CTkLabel(frame, text= "Software contendo automações para conclusão de processos praticados no Núcleo de Ensino a Distância da Universidade Iguaçu - NEAD UNIG", width= 500, height= 50, wraplength= 450)
        texto1.pack()

        frame_botoes = ctk.CTkFrame(frame, fg_color= "transparent")
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



""" Janela do Sophia """
class JanelaSophia(JanelaBase):
    def __init__(self, master):
        super().__init__(master, "Automações Sophia")

        frame = ctk.CTkFrame(self, fg_color= "transparent")
        frame.pack(expand= True)

        label = ctk.CTkLabel(frame, text="Automações para o Sistema de Gestão Academica SophiA")
        label.pack(pady=20)

        frame_botoes= ctk.CTkFrame(frame,fg_color="transparent")
        frame_botoes.pack()

        #Háviam muitos botões poluindo tudo, estou tentando evitar essa crise.
        #Posteriormente vou ver uma maneira de transformar o código abaixo em uma função
        #visto que está sendo usado em duas janelas diferentes e caso eu queira mais
        #janelas a bagunça retornará. Muito feliz que consegui pensar esse código abaixo
        #sem ajuda, sinto que estou melhorando.

        qnt_botoes = 8
        texto = ["Botão", "Botão", "Botão", "Botão", "Botão", "Botão", "Botão", "Botão", "Botão"]
        #Prefiro uma lista com meus textos do que linhas e linhas de botões manualmente
        #escritos, posteriormente terei que fazer algo parecido para acomodar os comandos.
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

        botao_voltar = ctk.CTkButton(frame, text= "Voltar", command= self.voltar)
        botao_voltar.pack(pady = 30)



""" Janela do AVAUni """
class JanelaAvauni(JanelaBase):
    def __init__(self, master):
        super().__init__(master, "Automações AVAUni")

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

        botao_voltar = ctk.CTkButton(frame, text= "Voltar", command= self.voltar)
        botao_voltar.pack(pady = 30)


#TODO: Ajeitar as janelas, estou criando novas, quero que todas sejam 
#uma janela só com navegabilidade, pois se eu entro na janela Sophia,
#arrasto ela para o outro monitor e depois a fecho, a janela principal
#irá voltar para o monitor que estava anteriormente, e elas piscam
#quando estão mudando entre sí, são pequenos detalhes que me encomodam. 

if __name__ == "__main__":
    app = JanelaPrincipal()
    app.mainloop()