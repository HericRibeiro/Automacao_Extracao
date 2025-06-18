from config import config
from selenium import webdriver
from login import login
from download_arquivo import download_arquivo
from mover_arquivo import mover_arquivo
from obter_arquivo_recente import obter_arquivo_recente
from logger import setup_logging
import pandas as pd
import logging


def automacao_Extracao():
    setup_logging()
    navegador = webdriver.Edge()  
    try:
        logging.info("✅ Iniciando automação!")
        logging.info("✅ Iniciando locomoção de arquivo antigo!")
        if not mover_arquivo(config['nome_Arquivo'], config['diretorio_Origem'], config['diretorio_Destino']):
            logging.error("❌ Falha na locomoção de arquivo para pasta de antigos!")
            

        logging.info("✅ Iniciando login!")
        if not login(navegador):
            logging.error("❌ Falha no login!")

        logging.info("✅ Iniciando download!")
        if not download_arquivo(navegador):
            logging.error("❌ Falha no download do arquivo!")


        logging.info("✅ Iniciando locomoção do arquivo!")
        if not mover_arquivo(config['nome_Arquivo'], config['diretorio_Download'], config['diretorio_Origem']):
            logging.error("❌ Falha na locomoção do arquivo!")
            
        caminho_arquivo = obter_arquivo_recente(config['diretorio_Destino'], config['nome_Arquivo'])
        
        df = pd.read_csv(caminho_arquivo)
        num_lines = len(df)
        logging.info("✅ Automação Concluída")
        logging.info(f"✅ Número de linhas no arquivo CSV: {num_lines}")

    except FileNotFoundError as e:
        logging.error(f"❌ Falha na automação: {e}")


if __name__ == '__main__':
    automacao_Extracao()