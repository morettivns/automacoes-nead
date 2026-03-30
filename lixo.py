import pyautogui as pag
import time
import keyboard
import threading
import os
import pyperclip
from pathlib import Path

contador = 0

def contar_down(event):
    global contador
    contador += 1
    print(f"Tecla ↓ pressionada {contador} vezes")

# Escuta a tecla "down"
keyboard.on_press_key("down", contar_down)

print("Pressione a tecla ↓ (seta para baixo). Pressione ESC para sair.")

# Mantém o programa rodando até apertar ESC
keyboard.wait("esc")

print(f"Total de vezes que você pressionou ↓: {contador}")

