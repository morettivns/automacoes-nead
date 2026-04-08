import pyautogui as pag
import time
import keyboard
import threading
import os
import pyperclip
from pathlib import Path

def esc_listener():
    keyboard.wait("esc")
    print("ESC pressionado! Encerrando...")
    os._exit(0)

def status(msg = "Rodando..."):
    print(" " * 100, end="\r")  # limpa a linha
    print(msg, end="\r")

def clicar(pasta, arquivo, clicks= 1): #Espera a imagem aparecer na tela para clicar nela.
    caminho = Path(__file__).parent / "assets" / "prints" / pasta / arquivo
    
    while True:
        try:
            click = pag.locateCenterOnScreen(str(caminho))
            if click:
                pag.click(click, clicks= clicks)
                return click
        
        except pag.ImageNotFoundException:
            pass
        time.sleep(0.5)

def localizar(pasta, arquivos, vezes= 0): #Espera a imagem aparecer na tela para prosseguir o script.
    if isinstance(arquivos, str): #Se for uma string vira uma lista.
        arquivos = [arquivos]
    tentativas = 0

    caminho = Path(__file__).parent / "assets" / "prints" / pasta
    while True:
        for arquivo in arquivos:
            imagem = caminho / arquivo
            try:
                pos = pag.locateCenterOnScreen(str(imagem))
                if pos:
                    return arquivo, pos

            except pag.ImageNotFoundException:
                pass
        tentativas += 1
        if vezes > 0 and tentativas >= vezes:
            status("A imagem não foi encontrada, aperte 'Enter' para continuar.")
            keyboard.wait("Enter", suppress= True)
            return None
        time.sleep(0.5)

def tiposDeAvaliacoes(text, resu, tipo):
    clicar("Avaliacoes", "P5_nome.png")
    pyperclip.copy(text= str(text))
    pag.hotkey("Ctrl", "V")
    pag.press("Tab")
    pag.typewrite(str(resu))
    pag.press("Tab")
    pag.press("A")
    pag.press("Tab", presses= 2)
    pag.typewrite(str(tipo))
    check = localizar("Avaliacoes", "P6_check.png")
    pag.click(check[1].x - 35, check[1].y)

def avaliacoes(tecla = 1):
    tecla = str(tecla)
    status("Rodando Avaliações...")
    clicar("Avaliacoes", "P1_plano.png")
    pag.press("Tab")
    clicar("Avaliacoes", "P2_disciplinas.png")
    clicar("Avaliacoes", "P3_todos.png")
    tema = localizar("Avaliacoes", "PE_tema_integrador.png", vezes= 4)
    if tema:
        pag.click(tema[1].x, tema[1].y, clicks= 2)
        keyboard.wait("Enter", suppress= True)
    clicar("Avaliacoes", "P4_confirmar.png")

#Matérias normais:
    if tecla == "1":
        tiposDeAvaliacoes("Avaliação Diagnóstica", "AD", "AV-")
        #keyboard.wait("Enter", suppress= True)
        clicar("Avaliacoes", "P7_proximo.png")

    if tecla in ["1", "2"]:
        tiposDeAvaliacoes("Avaliação Substitutiva", "AS", "Sub")
        clicar("Avaliacoes", "P7_proximo.png")

    if tecla in ["1", "2", "3"]:
        tiposDeAvaliacoes("Avaliação Integradora", "AI", "API-")
        clicar("Avaliacoes", "P7_proximo.png")

    if tecla in ["1", "2", "3", "4"]:
        tiposDeAvaliacoes("Avaliação Especial", "AE", "Ava")
        clicar("Avaliacoes", "P8_confirmar.png")
        pag.press("Enter")

def temaIntegrador(tecla = "t1"):
    tecla.lower()
    status("Rodando Tema Integrador...")
    clicar("Avaliacoes", "P1_plano.png")
    pag.press("Tab")
    clicar("Avaliacoes", "P2_disciplinas.png")
    localizar("Avaliacoes", "P4_confirmar.png") #Apenas para evitar um bug.
    tema = localizar("Avaliacoes", "PE_tema_integrador.png", vezes= 4)
    if tema:
        pag.click(tema[1].x, tema[1].y, clicks= 2)
        keyboard.wait("Enter", suppress= True)
    clicar("Avaliacoes", "P4_confirmar.png")

#Tema integrador:
    if tecla == "t1":
        tiposDeAvaliacoes("Tema Integrador - Trabalho", "TI 1", "Tem")
        clicar("Avaliacoes", "P7_proximo.png")

    if tecla in ["t1", "t2"]:
        tiposDeAvaliacoes("Tema Integrador - Apresentação", "TI 2", "Tem")
        clicar("Avaliacoes", "P8_confirmar.png")
        pag.press("Enter", presses= 2)

threading.Thread(target= esc_listener, daemon= True).start()
while True:
    avaliacoes()
    temaIntegrador()
    sair = localizar("Avaliacoes", "P1_plano.png")
    pag.click(sair[1].x, sair[1].y + 35)
    pag.hotkey("Alt", "F4")
    pag.hotkey("Tab", "Down", "Enter")
    clicar("Avaliacoes", "P9_quadro_curricular.png")