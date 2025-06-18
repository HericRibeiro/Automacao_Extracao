import pathlib
import logging
import shutil

def mover_arquivo(nome_padrao, origem, destino):
    diretorio = pathlib.Path(origem)
    arquivos = diretorio.glob(nome_padrao)
    for arquivo in arquivos:
        try:
            csv_file = arquivo
            logging.info(f"✅ Arquivo encontrado: {csv_file}")
            string = str(csv_file)
            modificado = string.replace("\\", "/")
            logging.info(f"✅ Movendo arquivo: {modificado}")
            shutil.move(modificado, destino)
        except FileNotFoundError:
            logging.warning(f"❌ Arquivo não encontrado: {nome_padrao}")
        except Exception as e:
            logging.error(f"❌ Erro ao mover arquivo: {e}")