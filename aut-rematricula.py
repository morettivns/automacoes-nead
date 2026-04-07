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

def status(msg):
    print(" " * 100, end="\r")  # limpa a linha
    print(msg, end="\r")

def locate(pasta, arquivo, clicks= 1):
    click = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / pasta / arquivo))
    pag.click(click.x, click.y, clicks= clicks)

def rematricula():
    #Na página 1:
    status("Rodando...")
    disp = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "Rematricula" / "P1_disponibilidade.png"))
    pag.click(disp.x + 100, disp.y)

    pag.press("up", presses= 5)
    pag.hotkey("down", "enter")

    #Na página 2:
    locate("Rematricula", "P2_proxima_pagina.png")
    pag.press("enter")
    time.sleep(6)
    #keyboard.wait("[", suppress= True)

    cal1 = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "Rematricula" / "P3_inicio.png"))
    pag.click(cal1.x, cal1.y)
    pag.click(cal1.x - 65, cal1.y + 25, clicks= 2)
    locate("Rematricula", "P6_dia.png")
    pag.press("enter")

    cal2 = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "Rematricula" / "P4_termino.png"))
    pag.click(cal2.x, cal2.y)
    pag.click(cal2.x - 65, cal2.y + 25, clicks= 2)
    pag.click(cal2.x - 10, cal2.y + 20, clicks= 1)
    locate("Rematricula", "P6_dia.png")
    pag.press("enter")

    text = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "Rematricula" / "P8_texto.png"))
    pag.click(text.x, text.y + 100)
    pag.hotkey("ctrl", "a")
    pag.press("del")
    texto = "Agora você renovará sua matrícula para o primeiro semestre de 2026. Fique atento ao prazo final para a renovação de matrícula, prevista para 23 de Abril de 2026.\n\nO processo de matrícula fora do prazo ocorrerá de 24 de Abril de 2026 a 24 de Maio de 2026.\n\nNas próximas etapas você terá acesso às disciplinas do próximo semestre, bem como ao Contrato de Renovação de Matrícula e ao Boleto de Matrícula."
    pyperclip.copy(texto)
    pag.hotkey("ctrl", "v")

    #Gravar e próximo:
    locate("Rematricula", "P9_gravar.png")
    prox = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "Rematricula" / "P10_proximo.png"))
    pag.click(prox.x, prox.y + 25)
    pag.hotkey("down", "enter")

threading.Thread(target=esc_listener, daemon=True).start()
while True:
    status("Para rodar novamente aperte '['")
    keyboard.wait("[", suppress= True)
    rematricula()