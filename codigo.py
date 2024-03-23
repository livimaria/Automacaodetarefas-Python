#Passo a passo do projeto:

#Passo 1: Entrar no sistema da empresa
    
#pyautogui: Biblioteca que permite a automatização do mouse e teclado
  #pyautogui.click = clicar em algum lugar da tela 
  #pyautogui.write = escrever um texto
  #pyautogui.press = pressionar 1 tecla do teclado

#abrir o navegador(chrome)
import pyautogui
import time  
pyautogui.PAUSE = 0.5   #configuração para pausa entre uma digitação e outra
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)   #dar uma pausa um pouco maior, pra poder carregar totalmente


#Passo 2: Fazer login no sistema 
pyautogui.click("indicar a posição exata do mouse")
pyautogui.write("e-mail aqui")

#escrever a senha no sistema
pyautogui.press("tab")  #clica na tecla tab
pyautogui.write("senha aqui")

#clicar no botão de logar
pyautogui.click("indicar a posição exata do mouse")
time.sleep(3)


#Passo 3: Importar a base de dados 
import pandas
tabela = pandas.read_csv("produtos.csv")

print(tabela)

#Passo 4: Cadastrar 1 produto
#para cada linha da minha tabela
for linha in tabela.index:


    #clicar no 1° campo
    pyautogui.click("indicar a posição exata do mouse")

    #codigo do produto
    codigo = tabela.loc[linha, 'coluna']
    pyautogui.write("Codigo do produto")
    pyautogui.press("tab")

    #marca
    pyautogui.write(tabela.loc[linha, 'marca'])
    pyautogui.press("tab")

    #tipo
    pyautogui.write(tabela.loc[linha, 'tipo'])
    pyautogui.press("tab")

    #categoria
    str()
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    pyautogui.press("tab")

    #preço unitário do produto
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    pyautogui.press("tab")

    #custo
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press("tab")

    #obs
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
      pyautogui.write(tabela.loc[linha, 'obs'])   #tabela.loc- localiza uma informação na tabela, tendo que informar  a linha e a coluna da tabela
    pyautogui.press("tab")

    #enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)     #volta para início da tela, se colocar -número, vai para baixo


#Passo 5: Repetir o processo de cadastro até acabar


