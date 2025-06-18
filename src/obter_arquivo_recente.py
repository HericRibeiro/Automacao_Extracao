import pathlib


def obter_arquivo_recente(pasta, padrao):
    diretorio = pathlib.Path(pasta)
    arquivos = list(diretorio.glob(padrao))
    if not arquivos:
        raise FileNotFoundError(f"❌ Nenhum arquivo encontrado com o padrão: {padrao}")
    arquivo_recente = max(arquivos, key=lambda f: f.stat().st_mtime)
    return str(arquivo_recente)
