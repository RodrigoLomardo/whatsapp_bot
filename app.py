import openpyxl
from  urllib.parse import quote
import webbrowser
from time import sleep
import pyautogui

webbrowser.open('https://web.whatsapp.com') 
sleep(5)

workbook = openpyxl.load_workbook('PlanilhaContatos.xlsx')
pagine_clientes = workbook['Sheet1']


for linha in pagine_clientes.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = linha[1].value
    vencimento = linha[2].value
    
    mensagem = f'Olá {nome} seu boleto vence no dia {vencimento.strftime('%d/%m/%Y')}. Favor pagar no link https://www.link_do_pagamento.com'
    
   
    
    try:
        link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem)}'
    
        webbrowser.open(link_mensagem_whatsapp)
        # https://web.whatsapp.com/send?phone=&text
        sleep(5)
    
        send = pyautogui.locateCenterOnScreen('send.png')
        pyautogui.click(send[0],send[1])
        sleep(2)
        pyautogui.hotkey('crtl','w')
        sleep(2)
    except:
        print(f'Não foi possivel mandar mensagem para {nome} ')
        with open('erros.csv','a',newline='',encoding='utf-8') as arquivo:
            arquivo.write(f'{nome},`{telefone}')
    