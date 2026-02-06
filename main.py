import customtkinter as ctk
import pyautogui as pag
import automacoes
from pathlib import Path
from PIL import Image, ImageTk

#-------------------------#
""" Imagens e estéticos """
#-------------------------#

icone_caminho = Path(__file__).parent / "assets" / "unig_logo.ico"
logo_caminho = Path(__file__).parent / "assets" / "unig_logo.png"

def icone(janela): #Para corrigir o erro do ícone não iniciando junto com a janela.
    janela.iconbitmap(icone_caminho)


#---------------------# 
"""     Classes     """
#---------------------# 

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

        for Pagina in (Principal, LoginSophia, Sophia, LoginAvauni, Avauni, TrocaDeTurma):
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


#----------------------#
""" Página Principal """
#----------------------#

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

        botaoLoginSophia = ctk.CTkButton(frame_botoes, text= "Logar Sophia", command= lambda: controller.mostrar_pagina(LoginSophia))
        botaoLoginSophia.grid(row= 0, column= 0, padx= 10, pady= 10)

        botaoEntrarSophia = ctk.CTkButton(frame_botoes, text= "Automações Sophia", command= lambda: controller.mostrar_pagina(Sophia))
        botaoEntrarSophia.grid(row= 1, column= 0, padx= 10, pady= 10)

        botaoAvauni = ctk.CTkButton(frame_botoes, text= "Logar Avauni", command= lambda: controller.mostrar_pagina(LoginAvauni))
        botaoAvauni.grid(row= 0, column= 1, padx= 10, pady= 10)

        botaoEntrarAvauni = ctk.CTkButton(frame_botoes, text= "Automações Avauni", command= lambda: controller.mostrar_pagina(Avauni))
        botaoEntrarAvauni.grid(row= 1, column= 1, padx= 10, pady= 10)

#---------------------#
"""     Sophia      """
#---------------------#

class LoginSophia(PaginaBase):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        frame = ctk.CTkFrame(self, fg_color= "transparent")
        frame.pack(expand= True)

        ctk.CTkLabel(frame, text= "Digite seu login e senha Sophia").grid(row= 0, column= 0, padx= 10, pady= 10)
        #Automatizar a entrada no Sophia e caso der erro retornar

        usuario = ctk.CTkEntry(frame, placeholder_text= "Usuário", width= 200)
        usuario.grid(row= 1, column= 0, padx= 10, pady= 10)

        senha = ctk.CTkEntry(frame, placeholder_text= "Senha", width= 200)
        senha.grid(row= 2, column= 0, padx= 10, pady= 10)

        botao_confirmar = ctk.CTkButton(frame, text= "Confirmar", command= lambda: automacoes.SophiaEntrar(usuario.get(), senha.get()))
        botao_confirmar.grid(row= 3, column= 0, padx= 10, pady= 20)

        botao_voltar = ctk.CTkButton(frame, text= "Voltar", command= lambda: controller.mostrar_pagina(Principal))
        botao_voltar.grid(row= 4, column= 0, padx= 10,pady=0)


class Sophia(PaginaBase):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(expand= True)

        ctk.CTkLabel(frame, text="Automações para o Sistema de Gestão Acadêmica SophiA"
        ).pack(pady=20)

        frame_botoes = ctk.CTkFrame(frame, fg_color="transparent")
        frame_botoes.pack()

        qnt_botoes = 8
        texto = ["Troca de turma", "Print", "Botão", "Botão", "Botão", "Botão", "Botão", "Botão", "Botão"]
        comandos = [lambda: controller.mostrar_pagina(TrocaDeTurma),
                    lambda: print("Deu certo"), "", "", "", "", "", "", ""]

        linha, coluna = 0, 0
        intercalar = False

        for i in range(qnt_botoes):
            btn = ctk.CTkButton(frame_botoes, text= texto[i], command= comandos[i])
            btn.grid(row=linha, column=coluna, pady=10, padx=10)

            if intercalar is False:
                coluna += 1
                intercalar = True
            else:
                linha += 1
                coluna = 0
                intercalar = False

        botao_voltar = ctk.CTkButton(frame, text="Voltar", command=lambda: controller.mostrar_pagina(Principal))
        botao_voltar.pack(pady=30)

class TrocaDeTurma(PaginaBase):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        cursos = {"Administração": 0, "Análise e Des": 1, "Biomedicina": 2, "C.D.C. (IA)": 3, "Ciências Cont": 4, "Ed. Fís. Bach": 5, "Ed. Fís. Lic.": 6, "Eng. de Prod.": 7, "Eng. Elétrica": 8, "Eng. Mecânica": 9, "Farmácia": 10, "Fisioterapia": 11, "Gestão de RH": 12, "Gestão Púb.": 13, "Nutrição": 14, "Pedagogia": 15, "Serviço Social": 16}
        periodos = {"1° Período": 1, "2° Período": 2, "3° Período": 3, "4° Período": 4, "5° Período": 5, "6° Período": 6, "7° Período": 7, "8° Período": 8, "9° Período": 9, "10° Período": 10}
        turnos = {"Opção Nº1": 1, "Opção Nº2": 2,"Opção Nº3": 3,"Opção Nº4": 4,"Opção Nº5": 5,"Opção Nº6": 6,"Opção Nº7": 7,"Opção Nº8": 8,"Opção Nº9": 9,"Opção Nº10": 10}

        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(expand= True)

        label = ctk.CTkLabel(frame, text="Escolha o Curso, Período e Turno")
        label.pack(pady= 20)

        frame_opcoes = ctk.CTkFrame(frame, fg_color="transparent")
        frame_opcoes.pack()

        menu_cursos = ctk.CTkComboBox(frame_opcoes, values= list(cursos.keys()))
        menu_cursos.grid(row= 0, column= 0, padx= 10, pady= 10)

        menu_periodos = ctk.CTkComboBox(frame_opcoes, values= list(periodos.keys()))
        menu_periodos.grid(row= 0, column= 1, padx= 10, pady= 10)

        menu_turnos = ctk.CTkComboBox(frame_opcoes, values= list(turnos.keys()))
        menu_turnos.grid(row= 0, column= 2, padx= 10, pady= 10)

        botao_iniciar = ctk.CTkButton(frame_opcoes, text= "Iniciar", command=lambda: automacoes.TrocaDeTurma(curso= cursos.get(menu_cursos.get()),periodo= periodos.get(menu_periodos.get()), turno= turnos.get(menu_turnos.get())))
        botao_iniciar.grid(row= 1, column= 1, padx= 10, pady= 10)

        botao_voltar = ctk.CTkButton(frame, text="Voltar", command=lambda: controller.mostrar_pagina(Principal))
        botao_voltar.pack(pady=30)

#---------------------#
"""     AVAUni      """
#---------------------#

class LoginAvauni(PaginaBase):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)

        frame = ctk.CTkFrame(self, fg_color= "transparent")
        frame.pack(expand= True)

        ctk.CTkLabel(frame, text= "Digite seu login e senha Avauni").grid(row= 0, column= 0, padx= 10, pady= 10)
        #Automatizar a entrada no Avalia e caso der erro retornar

        usuario = ctk.CTkEntry(frame, placeholder_text= "Usuário", width= 200)
        usuario.grid(row= 1, column= 0, padx= 10, pady= 10)

        senha = ctk.CTkEntry(frame, placeholder_text= "Senha", width= 200)
        senha.grid(row= 2, column= 0, padx= 10, pady= 10)

        botao_confirmar = ctk.CTkButton(frame, text= "Confirmar", command= lambda: controller.mostrar_pagina(Avauni))
        botao_confirmar.grid(row= 3, column= 0, padx= 10, pady= 20)

        botao_voltar = ctk.CTkButton(frame, text= "Voltar", command= lambda: controller.mostrar_pagina(Principal))
        botao_voltar.grid(row= 4, column= 0, padx= 10,pady=0)

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

        botao_voltar = ctk.CTkButton(frame, text="Voltar", command=lambda: controller.mostrar_pagina(Principal))
        botao_voltar.pack(pady=30)

        #Failsafe do "Adicionar alunos no Enade"


if __name__ == "__main__":
    app = App()
    app.mainloop()