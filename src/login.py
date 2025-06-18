from selenium import webdriver
from config import config
import logging
import time

def login(navegador: webdriver.Edge):
    try:
        navegador.implicitly_wait(5)  
        navegador.get(config['link_Web'])  
        navegador.maximize_window()
        time.sleep(3)  

        navegador.find_element(config['xpath'], config['acesso']).click()
        time.sleep(3)  
        
        navegador.find_element(config['xapth'], config['confirmacao_Acesso']).click()
        time.sleep(2)
        
        navegador.find_element(config['xapth'], config['modulo']).click() 
        time.sleep(4)
        logging.info('✅ Modulo')

        window_handles = navegador.window_handles
        navegador.switch_to.window(window_handles[-1])
        time.sleep(3)
    except Exception as e:
        logging.error(f"❌ Falha no login: {e}")