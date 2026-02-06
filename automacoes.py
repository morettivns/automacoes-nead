import pyautogui as pag
import time
from pathlib import Path
import keyboard

pag.PAUSE = 1
pag.FAILSAFE = True

#---------------------#
"""  Abrir Sophia   """
#---------------------#

def SophiaEntrar(usuario, senha):
    pag.press("Win")
    pag.typewrite("Sophia Lite", interval= 0.2)
    pag.press("Enter")
    time.sleep(2)
    cx_usuario = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "TrocaDeTurma" / "P1_sophiaUsuario.png"))
    pag.click(cx_usuario.x, cx_usuario.y)
    pag.typewrite(usuario, interval= 0.2)
    pag.press("Tab")
    pag.typewrite(senha, interval= 0.2)
    pag.press("Enter")



#---------------------#
""" Troca de turma  """
#---------------------# 

def TrocaDeTurma(curso = None, periodo = None, turno = None):
    time.sleep(4) #Amanhã vou fazer com que ao pressionar "[" o código inicie,
                  #para dar tempo de mudar do programa para o Sophia.
    """ Botão executar """
    exec = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "TrocaDeTurma" / "P1_executar.png"))
    pag.click(exec.x, exec.y, clicks= 2)
    time.sleep(1)
    pag.press("down", presses= 3, interval= 0.1)
    pag.press("Enter", presses= 2, interval= 0.1)
    print("Currículo antigo mudado!")

    """ Desativar currículo """
    desa = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "TrocaDeTurma" / "P2_desativar.png"))
    pag.click(desa.x, desa.y)
    pag.hotkey("up", "Tab", "Tab", interval= 0.3)
    pag.typewrite("tr")
    pag.hotkey("down", "Tab", "Tab", "Tab", "Enter", interval= 0.3)
    print("Currículo antigo desativado por transferência!")

    """ Criar curriculo """
    curr = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "TrocaDeTurma" / "P3_criarCurriculo.png"))
    pag.click(curr.x, curr.y)
    time.sleep(1.5)
    pag.hotkey("Tab", "G", "Space", "S", interval= 0.3)
    pag.press("down", presses= curso, interval= 0.3) #Número do curso
    pag.press("Tab", presses= 2)
    time.sleep(2)
    pag.press("down")
    
    seri = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "TrocaDeTurma" / "P4_serie.png"))
    pag.click(seri.x, seri.y)
    time.sleep(1.5)
    pag.press("down", presses= periodo) #Número do período
    pag.hotkey("Enter", "Tab", interval= 1)
    time.sleep(1)
    if turno != None:
        pag.press("down", presses= turno) #1 para manha, 2 para noite
    print("Currículo novo criado!")


    print("Aperte '[' para confirmar e ir para próximo.\n" \
    "Aperte ']' para cancelar as alterações.\n" \
    "Aperte 'Esc' para sair da automação.")

    while True:
        tecla = keyboard.read_key()

        if tecla == "[":
            print("Opção continuar selecionada.")
            grav = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "TrocaDeTurma" / "P4_gravar.png"))
            pag.click(grav.x, grav.y)
            time.sleep(3)
            pag.hotkey("Enter", "Enter", interval= 1)
            time.sleep(1)
            prox = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "TrocaDeTurma" / "P5_proximo.png"))
            pag.click(prox.x, prox.y)
            
            print("Quando na tela nova, selecione a disciplina para mudar e aperte '[' para continuar.")
            keyboard.wait("[")
            TrocaDeTurma(curso= curso, periodo= periodo, turno= turno)
            
        elif tecla == "]":
            print("Opção cancelar selecionada.")
            canc = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "TrocaDeTurma" / "P6_cancelar.png"))
            pag.click(canc.x, canc.y)
            break

        elif tecla == "esc":
            print("Saindo...")
            break

if __name__ == "__main__":
    TrocaDeTurma(periodo= 1, turno= 2)