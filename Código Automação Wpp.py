import pyautogui
import time
import pyperclip
import pandas as pd

#Importando a base de dados
tabela = pd.read_excel(r'C:\Users\gilso\OneDrive\Área de Trabalho\Casa\MinhaCasaMinhaVida.xlsx')
Valor = tabela['Valor']
name_devedor = tabela['Contribuintes']

contador_nome_devedor = 0

#Abrir uma nova aba
pyautogui.hotkey('ctrl','t')

#Acessar o Whatsapp
link = 'https://web.whatsapp.com/'
pyperclip.copy(link)
pyautogui.hotkey('ctrl','v')
pyautogui.press('enter')

for cell in Valor:
    valor_total = cell    

    #Procurando o contato
    time.sleep(7)
    pyautogui.click(150, 150)

    name = name_devedor[contador_nome_devedor]
    pyperclip.copy(name)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')

    pyautogui.click(645, 689)
    mensagem = f"""
    Teste: Automação de cobrança das Despesas da casa
    
    Valor total = R${valor_total:,.2f}
    
    Boa noite, obrigado!

    """
    pyperclip.copy(mensagem)
    pyautogui.hotkey('ctrl','v')
    pyautogui.press('enter')
    
    contador_nome_devedor = contador_nome_devedor + 1
    
break