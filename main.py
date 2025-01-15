from ExtrairInfo import extrair_informacoes

caminho_base = "C:\\UNIDADES\\UNIDADES\\MATRIZ\\ATIVO FIXO\\LUIS"

arquivos = ["SYSTEMINFO.txt", "IPCONFIG.txt", "DISK.txt", "MEM.txt", "CPU.txt", "dumpedid.txt", "MOUSE E TECLADO.txt"]

# Lista para armazenar as informações de todos os arquivos
dados_completos = []

for nome_arquivo in arquivos:
    caminho_arquivo = f"{caminho_base}\\{nome_arquivo}"
    dados = extrair_informacoes(caminho_arquivo)
    dados_completos.append((nome_arquivo, dados))


for arquivo, dados in dados_completos:
    print(f"Arquivo: {arquivo}")
    for dado in dados:
        print(dado)
    print("-" * 50)




