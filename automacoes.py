import pyautogui as pag
import time
import keyboard
import threading
from pathlib import Path

pag.PAUSE = 1
pag.FAILSAFE = True

#---------------------#
"""  Abrir Sophia   """
#---------------------#

def SophiaEntrar():
    pag.press("Win")
    pag.typewrite("Sophia Lite", interval= 0.2)
    pag.press("Enter")


#---------------------#
""" Troca de turma  """
#---------------------# 

def TrocaDeTurma(campus = "n", curso = None, periodo = None, turno = None, texto_func= None):
    #time.sleep(4) #Amanhã vou fazer com que ao pressionar "[" o código inicie,
                   #para dar tempo de mudar do programa para o Sophia.
    try:
        teste = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "TrocaDeTurma" / "PTeste_1.png"))
        if teste:
            pag.click(teste.x, teste.y, clicks= 2)
            pag.hotkey("t", "Enter", interval= 0.5)
    except pag.ImageNotFoundException:
        print("Imagem nao encontrada")
        pass

    """ Botão executar """
    exec = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "TrocaDeTurma" / "P1_executar.png"))
    pag.click(exec.x, exec.y, clicks= 2)
    time.sleep(1)
    pag.press("down", presses= 4, interval= 0.1)
    pag.press("Enter", presses= 2, interval= 0.1)
    print("Currículo antigo mudado!")

    """ Desativar currículo """
    desa = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "TrocaDeTurma" / "P2_desativar.png"))
    pag.click(desa.x, desa.y)
    time.sleep(2)
    pag.hotkey("up", "Tab", "Tab", interval= 0.3)
    pag.typewrite("tr")
    pag.hotkey("down", "Tab", "Tab", "Tab", "Enter", interval= 0.3)
    print("Currículo antigo desativado por transferência!")

    """ Criar curriculo """
    curr = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "TrocaDeTurma" / "P3_criarCurriculo.png"))
    pag.click(curr.x, curr.y)
    time.sleep(1.5)
    pag.hotkey(campus, "Tab", "G", "Space", "S", interval= 0.3)
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

    explicacao = "No Sophia: Selecione a turma desejada  →  Clique duas vezes no aluno a ser transferido  →  Clique em 'Acadêmico'  →  Selecione a turma desejada  →  Por fim, Selecione as opções abaixo e inicie o programa."

    instrucao1 = ("Aperte '[' para confirmar e ir para próximo.\n" 
    "Aperte ']' para cancelar as alterações.\n" 
    "Aperte 'Esc' para sair da automação.")

    if texto_func:
        texto_func.configure(text= instrucao1)
        texto_func.update()

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

            texto_func.configure(text= "Quando na tela nova, selecione a disciplina para mudar e aperte '[' para continuar.")
            texto_func.update()
            keyboard.wait("[")
            TrocaDeTurma(curso= curso, periodo= periodo, turno= turno)
            
        elif tecla == "]":
            print("Opção cancelar selecionada.")
            if texto_func:
                texto_func.configure(text=explicacao)
                texto_func.update()
            canc = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "TrocaDeTurma" / "P6_cancelar.png"))
            pag.click(canc.x, canc.y)
            break

        elif tecla == "esc":
            if texto_func:
                texto_func.configure(text=explicacao)
                texto_func.update()
            print("Saindo...")
            break


#---------------------#
"""      Censo      """
#---------------------# 

def Censo(letra = "", baixo= 0, alunos= 0):
    pag.PAUSE = 0.2
    keyboard.wait("[", suppress= True)
    alunos = int(alunos)

    while alunos > 0:
        pag.press(letra)
        pag.press("down", presses= int(baixo))
        pag.hotkey("Enter", "down")
        alunos -= 1


#---------------------#
"""Inserir Adaptação"""
#---------------------#

def Adaptacao():
    curr = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P1_farm2026.png"))
    pag.click(curr.x, curr.y, clicks= 2)

    acad = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P2_academico.png"))
    pag.click(acad.x, acad.y, clicks= 2)

    cria = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P3_criar.png"))
    pag.click(cria.x, cria.y, clicks= 1)
    pag.hotkey("Enter", "N")
    sele = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P4_selecionar.png"))
    pag.click(sele.x, sele.y, clicks= 1)
    conf = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P5_confirmar.png"))
    pag.click(conf.x, conf.y, clicks= 1)

    pag.hotkey("Tab", "Enter")
    pag.typewrite("por")
    #Vai mudar dependendo da matéria:
    pag.press("Down")
    pag.keyDown("shift")
    pag.press("down", presses= 4)
    pag.keyUp("shift")
    pag.click(sele.x, sele.y, clicks= 1)
    pag.click(conf.x, conf.y, clicks= 1)

    pag.hotkey("tab", "enter")
    time.sleep(0.5)
    pag.press("s")  #de semipresencial
    pag.press("down", presses=15)
    pag.click(sele.x, sele.y, clicks= 1)
    pag.click(conf.x, conf.y, clicks= 1)

    filt = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P6_filtrar.png"))
    pag.click(filt.x, filt.y, clicks= 1)

    mais = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P7_mais.png"))
    pag.click(mais.x, mais.y, clicks= 1)
    time.sleep(0.5)
    pag.click(mais.x, mais.y, clicks= 1)
    chec = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P8_check.png"))
    pag.click(chec.x, chec.y, clicks= 1)
    regu = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P9_regular.png"))
    pag.click(regu.x, regu.y, clicks= 1)
    drop = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P10_drop.png"))
    pag.click(drop.x, drop.y, clicks= 1)
    pag.press("up", presses= 14)

    pag.hotkey("enter", "tab", "tab", "enter")
    fech = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P11_fechar.png"))
    pag.click(fech.x, fech.y, clicks= 1)

    acei = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P12_aceitar.png"))
    pag.click(acei.x, acei.y, clicks= 1)
    prox = pag.locateCenterOnScreen(str(Path(__file__).parent / "assets" / "prints" / "InserirAdaptacao" / "P12_aceitar.png"))
    pag.click(prox.x, prox.y, clicks= 1)

    keyboard.wait("[")
    Adaptacao()


if __name__ == "__main__":
    TrocaDeTurma(periodo= 1, turno= 2)