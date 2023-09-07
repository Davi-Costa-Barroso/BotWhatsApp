# Davi Costa Barroso
import pyautogui as bot
import time
import webbrowser as web
import pandas as pd
def bot_zap():
    # Mude o diretorio da planilha
    data = pd.read_excel("contatos.xlsx") 
    data_lista = data.to_dict('list')
    telefones = data_lista['telefone']
    msg = data_lista['mensagem']
    for i in range(len(telefones)):
        web.open(f"https://web.whatsapp.com/send?phone={telefones[i]}&text={msg[i]}")
        # Ajuste o tempo se o whatsapp demorar para abrir
        time.sleep(15)
        bot.press("Enter")
        time.sleep(2)
        bot.hotkey("ctrl", "w")
bot_zap()