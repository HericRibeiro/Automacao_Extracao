from dotenv import load_dotenv
import os

load_dotenv()

config = {
    "link_Web": os.getenv("LINK_PORTAL"),
    "nome_Arquivo": os.getenv("NOME"),
    "diretorio_Origem": os.getenv("DIRETORIO_ORIGEM_ARQUIVO"),
    "diretorio_Destino": os.getenv("DIRETORIO_DESTINO_ARQUIVO"),
    "diretorio_Download": os.getenv("DIRETORIO_DOWNLOAD_PASTA"),
    "pasta": os.getenv("pastaFim"), # substituir por DIRETORIO_DESTINO_ARQUIVO
    "caminho_arquivo_erro": os.getenv("CAMINHO_ARQUIVO_LOG"),
    "acesso": os.getenv("XPATH_ACESSO"),
    "confirmacao_Acesso": os.getenv('XPATH_CONFIRMACAO_ACESSO'),
    "modulo": os.getenv("XPATH_MODULO"),
    "extracao_Tabela": os.getenv("XPATH_EXTRACAO_TABELA"),
    "xpath": os.getenv("XPATH"),
}