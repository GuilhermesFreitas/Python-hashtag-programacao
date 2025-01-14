# Automação com Python.

import pyautogui
import time
import pandas

link = (" https://dlp.hashtagtreinamentos.com/python/intensivao/login ")

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("Firefox")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")

time.sleep(3)

pyautogui.click(x=680, y=371)
pyautogui.write("teste@gmail.com")
pyautogui.press("tab")
pyautogui.write("12345678")
pyautogui.press("tab")
pyautogui.press("enter") # => faz o login.

tabela = pandas.read_csv("Arquivos/produtos.csv")
print("tabela")

time.sleep(2)

for linha in tabela.index:
#HARDCODE

  pyautogui.click(x=820, y=252)

  codigo = tabela.loc[linha, "codigo"]
  pyautogui.write(codigo)
  pyautogui.press("tab")

  marca = tabela.loc[linha, "marca"]
  pyautogui.write(marca)
  pyautogui.press("tab")

  tipo = tabela.loc[linha, "tipo"]
  pyautogui.write(tipo)
  pyautogui.press("tab")

  categoria = 1 
  pyautogui.write(str(categoria))
  pyautogui.press("tab")

  preco = tabela.loc[linha, "preco_unitario"]
  pyautogui.write(str(preco))
  pyautogui.press("tab")

  custo = tabela.loc[linha, "custo"]
  pyautogui.write(str(custo))
  pyautogui.press("tab")

  obs = "Verificar o estoque."
  pyautogui.write(obs)
  pyautogui.press("tab")

  pyautogui.press("enter")

  pyautogui.scroll(-1000)
  time.sleep(0.3)
  pyautogui.scroll(1000)