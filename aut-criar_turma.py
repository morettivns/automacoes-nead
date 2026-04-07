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

def criarTurma(num_periodo = 1, periodos= 8, curso= "", baixo= 0):
    while num_periodo <= periodos:
        status()
        locate("CriarTurma", "P1_incluir.png")
        esperarImagem("CriarTurma", "P3_gravar.png")
        time.sleep(1)
        pyperclip.copy(f"G - 2026.2.1.{num_periodo}P - {curso}")
        pag.hotkey("Ctrl", "V")
        pag.press("Tab", presses= 3)
        pag.typewrite("ge")
        pag.press("Tab", presses= 4)
        pag.typewrite("g")
        pag.press("down", presses= baixo) #<===
        pag.press("Tab")
        esperarImagem("CriarTurma", "P2_curriculo.png")
        curr = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "CriarTurma" / "P2_curriculo.png"))
        pag.click(curr.x + 30, curr.y)
        pag.press("down", presses= 5)
        pag.hotkey("Enter", "Tab")

        pag.press("down", presses= int(num_periodo))
        pag.press("Tab", presses= 2)
        pag.typewrite("120")
        pag.press("Tab")
        pag.typewrite("01082026")
        if num_periodo == 1: #or num_periodo == 6:
            status("Aperte '[' para confirmar...")
            keyboard.wait("[", suppress= True)
        locate("CriarTurma", "P3_gravar.png")
        time.sleep(2)
        pag.hotkey("Alt", "F4")
        esperarImagem("CriarTurma", "P4_altf4.png")
        time.sleep(1)
        num_periodo += 1

threading.Thread(target= esc_listener, daemon= True).start()
#comex
criarTurma(1, 4, "Tecnologia da Informação", 9)
