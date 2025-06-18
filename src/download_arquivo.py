from selenium import webdriver
from config import config
import time
import logging

def download_arquivo(navegador: webdriver.Edge):
    try:
        window_handles = navegador.window_handles
        navegador.switch_to.window(window_handles[-1])
        time.sleep(3)  

        # Quantidade de Chamadas.
        navegador.find_element(config['xapth'], config['extracao_Tabela']).click()
        logging.info('✅ Baixando Arquivo!')
        time.sleep(190)
        logging.info('✅ Arquivo baixado')

    except Exception as e:
        logging.error(f"❌ Erro na extração de dados: {e}")

    finally:
        if 'navegador' in locals():
            navegador.quit()