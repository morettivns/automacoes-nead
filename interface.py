import customtkinter as ctk
import pyautogui as ptg

def abrir_janela():
    pass


janela = ctk.CTk()
janela.geometry(f"500x400+{(janela.winfo_screenwidth() - 500) // 2}+{(janela.winfo_screenheight() - 400) // 2}")
janela.title("Automações UNIG")
janela.resizable(False, False)

titulo = ctk.CTkLabel(janela, text= "Automações para processos realizados dentro do Núcleo de Ensino a Distância - UNIG", width= 500, height=100, wraplength=450)
titulo.pack(padx= 5, pady= 10)

frame_botoes = ctk.CTkFrame(janela, fg_color= "transparent")
frame_botoes.pack(pady= 10)

botao1 = ctk.CTkButton(frame_botoes, text= "SophiA", command= abrir_janela, fg_color= "#0f6fbb", hover_color= "#89cde2")
botao1.grid(row= 0, column= 0,padx= 10)

botao2 = ctk.CTkButton(frame_botoes, text= "AVAUni", command= abrir_janela, fg_color= "#0f6fbb", hover_color= "#89cde2")
botao2.grid(row= 0, column= 1,padx= 10)

janela.mainloop()