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

def locate(pasta, arquivo, clicks= 1): #Espera a imagem aparecer na tela para clicar nela.
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

def esperarImagem(pasta, arquivo): #Espera a imagem aparecer na tela para prosseguir o script.
    caminho = Path(__file__).parent / "assets" / "prints" / pasta / arquivo
    
    while True:
        try:
            pos = pag.locateCenterOnScreen(str(caminho))
            if pos:
                return pos
            
        except pag.ImageNotFoundException:
            pass
        time.sleep(0.5)


def avaliacoes(tecla = 1):
    tecla = str(tecla)
    status()
    locate("Avaliacoes", "P1_plano.png")
    pag.press("Tab")
    locate("Avaliacoes", "P2_disciplinas.png")
    locate("Avaliacoes", "P3_todos.png")
    keyboard.wait("Enter", suppress= True)
    locate("Avaliacoes", "P4_confirmar.png")

    def tiposDeAvaliacoes(text, resu, tipo):
        locate("Avaliacoes", "P5_nome.png")
        pyperclip.copy(text= str(text))
        pag.hotkey("Ctrl", "V")
        pag.press("Tab")
        pag.typewrite(str(resu))
        pag.press("Tab")
        pag.press("A")
        pag.press("Tab", presses= 2)
        pag.typewrite(str(tipo))
        esperarImagem("Avaliacoes", "P5_check.png")
        check = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "Avaliacoes" / "P5_check.png"))
        pag.click(check.x - 35, check.y)

    if tecla == "1":
        tiposDeAvaliacoes("Avaliação Diagnóstica", "AD", "AV-")
        locate("Avaliacoes", "P6_proximo.png")
        keyboard.wait("Enter", suppress= True)

    if tecla in ["1", "2"]:
        tiposDeAvaliacoes("Avaliação Substitutiva", "AS", "Sub")
        locate("Avaliacoes", "P6_proximo.png")

    if tecla in ["1", "2", "3"]:
        tiposDeAvaliacoes("Avaliação Integradora", "AI", "API-")
        locate("Avaliacoes", "P6_proximo.png")

    if tecla in ["1", "2", "3", "4"]:
        tiposDeAvaliacoes("Avaliação Especial", "AE", "Ava")
        locate("Avaliacoes", "P4_confirmar.png")

threading.Thread(target= esc_listener, daemon= True).start()
avaliacoes()
