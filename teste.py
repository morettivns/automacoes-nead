import pyautogui as pag
import time
import keyboard
import threading
import os
from pathlib import Path

def esc_listener():
    keyboard.wait("esc")
    print("ESC pressionado! Encerrando...")
    os._exit(0)

def status(msg):
    print(" " * 80, end="\r")  # limpa a linha
    print(msg, end="\r")

def Adaptacao():
    pag.FAILSAFE = True
    #curr = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P1_farm2026.png"))
    #pag.click(curr.x, curr.y, clicks= 2)
    status("Rodando...")

    acad = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P2_academico.png"))
    pag.click(acad.x, acad.y, clicks= 2)

    cria = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P3_criar.png"))
    pag.click(cria.x, cria.y, clicks= 1)
    pag.hotkey("Enter", "N")
    time.sleep(1)
    sele = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P4_selecionar.png"))
    pag.click(sele.x, sele.y, clicks= 1)
    conf = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P5_confirmar.png"))
    pag.click(conf.x, conf.y, clicks= 1)
    time.sleep(0.2)

    #Vai mudar dependendo da matéria:
    pag.hotkey("Tab", "Enter")
    time.sleep(0.2)
    pag.typewrite("fun")
    pag.press("Down", presses= 30)
    pag.keyDown("shift")
    pag.press("down", presses= 1)
    pag.keyUp("shift")
    time.sleep(0.2)
    pag.click(sele.x, sele.y, clicks= 1)
    pag.click(conf.x, conf.y, clicks= 1)
    time.sleep(0.2)

    pag.hotkey("tab", "enter")
    time.sleep(0.5)
    pag.press("s")  #de semipresencial
    pag.press("down", presses= 37)
    pag.click(sele.x, sele.y, clicks= 1)
    pag.click(conf.x, conf.y, clicks= 1)
    time.sleep(2)

    filt = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P6_filtrar.png"))
    pag.click(filt.x, filt.y, clicks= 1)
    time.sleep(2)

    mais = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P7_mais.png"))
    pag.click(mais.x, mais.y, clicks= 1)
    time.sleep(0.5)
    pag.click(mais.x + 15, mais.y + 15, clicks= 1)
    chec = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P8_check.png"))
    pag.click(chec.x, chec.y, clicks= 1)
    regu = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P9_regular.png"))
    pag.click(regu.x, regu.y, clicks= 1)
    drop = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P10_drop.png"))
    pag.click(drop.x, drop.y, clicks= 1)
    pag.press("up", presses= 14)
    pag.press("enter")
    drop = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P10_drop.png"))
    pag.click(drop.x, drop.y, clicks= 1)
    grav = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P11_gravar.png"))
    pag.click(grav.x, grav.y, clicks= 1)
    time.sleep(1)

    fech = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P11_fechar.png"))
    pag.click(fech.x, fech.y, clicks= 1)
    status("Aperte '[' para aceitar a adaptação...")
    keyboard.wait("[", suppress= True)
    status("Aceitando adaptação...")
    acei = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P12_aceitar.png"))
    pag.click(acei.x, acei.y, clicks= 1)
    prox = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P13_proximo.png"))
    pag.click(prox.x, prox.y, clicks= 1)
    pag.press("enter", presses= 2)
    status("Escolha o currículo desejado e aperte '[' em seguida.")
    time.sleep(2)
    pag.press("down", presses= 10)
    keyboard.wait("[", suppress= True)
    Adaptacao()

threading.Thread(target=esc_listener, daemon=True).start()
status("Selecione o currículo correto e em seguida pressione '[' para dar início.")
keyboard.wait("[", suppress= True)
Adaptacao()