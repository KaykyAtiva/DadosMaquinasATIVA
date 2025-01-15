import chardet

def detectar_codificacao(caminho_arquivo):

    # Detecta a codificação do arquivo
    with open(caminho_arquivo, 'rb') as arquivo:
        dados = arquivo.read()
        resultado = chardet.detect(dados)
        codificacao = resultado['encoding']
    return codificacao