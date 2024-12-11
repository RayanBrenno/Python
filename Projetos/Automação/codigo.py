import pandas as pd
import time
import pyautogui

def pegarPosicao():
    pyautogui.sleep(3)
    print(pyautogui.position())
    pyautogui.sleep(3)
    print(pyautogui.position())

def acessar(inscricao):
    pyautogui.click(x=1393, y=271) # click abrir periodo 1
    pyautogui.click(x=1294, y=360) # data 1 mes anterior x=1451, y=364
    pyautogui.click(x=1592, y=273) # click abrir periodo 2
    pyautogui.click(x=1473, y=305) # volta no mes x=1473, y=305
    pyautogui.click(x=1576, y=448) # data 30 mes anterior x=1480, y=472
    pyautogui.click(x=1254, y=326) # inscrição x=1254, y=326
    pyautogui.write(inscricao)
    pyautogui.click(x=1575, y=695) # pesquisa x=1575, y=695

def baixar():
    pyautogui.sleep(2)
    pyautogui.click(x=1596, y=1001) # baixar x=1596, y=1001
    pyautogui.click(x=1839, y=413) # baixar 2 x=1839, y=413  
    
def copiar():
    pyautogui.click(x=1823, y=58) # simbolo de dowload
    pyautogui.click(x=1686, y=146) # ultimo arquivo baixado
    pyautogui.sleep(2)
    pyautogui.click(x=1172, y=526) # padronizar para ser exatamente embaixo da caixa de Inscrição Estadual
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")

def colar(locX, locY):
    pyautogui.doubleClick(x=locX, y=locY)
    pyautogui.click(x=321, y=378)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.sleep(2)
    pyautogui.hotkey("alt", "left")

def fecharEvoltar():
    pyautogui.click(x=1319, y=522)
    pyautogui.hotkey("ctrl", "w")
    pyautogui.click(x=1457, y=1001)

def final():
    empresasEspeciais = ["amperco", "de", "distribuidora", "g7", "ga","kfc","lc","leandra","reginaldo","val tech","transgiro","ceramica catito","ceramica forte","ceramica rios","ceramica xavante"]
    pyautogui.sleep(5)
    pyautogui.PAUSE = 1
    tabela = pd.read_csv("Python - Lira Hashtag/Projeto/empresas.csv")
    locX = 410
    locY = 180
    x = 1413
    y = 987
    largura = 264
    altura = 30

    for linha in tabela.index:
        nome = tabela.loc[linha, "nome"]
        inscricao = tabela.loc[linha, "inscricao"]  
        if nome == "reginaldo":
            pyautogui.click(x=897, y=847)
            pyautogui.scroll(-5000)
            locY = 801  
        printInicio = pyautogui.screenshot(region=(x, y, largura, altura))
        acessar(str(inscricao))
        pyautogui.sleep(1)
        printDepois = pyautogui.screenshot(region=(x, y, largura, altura))
        
        if printInicio != printDepois:
            baixar()
            if nome in empresasEspeciais: pyautogui.sleep(15)
            else: pyautogui.sleep(23)
            copiar()
            colar(locX, locY)
            fecharEvoltar()
            locY += 31
            
        else: 
            locY += 31
            print(f"Não há notas para '{nome}'")
            pyautogui.click(x=1053, y=60)
            pyautogui.sleep(2)
            pyautogui.click(x=1266, y=255)
            
start_time = time.time()
final()
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tempo decorrido: {elapsed_time} segundos")
        