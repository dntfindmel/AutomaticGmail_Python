import yfinance as yf
import pyautogui
import pyperclip
import time

ticker = input('Digite o código da ação: ')
dados = yf.Ticker(ticker).history('6mo')
fechamento = dados.Close

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
atual = round(fechamento[-1], 2)

# dar uma pausa de 2 segundos entre os passos
pyautogui.PAUSE = 1.5

# abrir guia do firefox
pyautogui.click(x=1205, y=1052)

# abrir nova aba (ctrl + t)
pyautogui.hotkey('ctrl', 't')

# digitar www.gmail.com e dar um enter
pyperclip.copy('www.gmail.com')
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('enter')

# clicar no botão escrever
pyautogui.click(x=65, y=272)

# digitar o destinatário (tab)
time.sleep(2)
pyautogui.click(x=1470, y=456)
pyperclip.copy('semanapython@gmail.com')
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')

# digitar o assunto
pyperclip.copy('Análises diárias | Projeto Python')
pyautogui.hotkey('ctrl', 'v')
pyautogui.hotkey('tab')

# preencher o corpo do e-mail
mensagem = f'''Prezado gestor, 

Seguem, conforme solicitado, as análises dos últimos 6 meses da {ticker}
Cotação máxima: R${maxima}
Cotação mínima: R${minima}
Cotação atual: R${atual}

Qualquer dúvida, fico à disposição!
Atte.
Melyssa.'''

pyperclip.copy(mensagem)
pyautogui.hotkey('ctrl', 'v')

pyautogui.click(x=1217, y=980)
