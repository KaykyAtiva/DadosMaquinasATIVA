from ExtrairInfo import extrair_informacoes
import os
caminho_base = os.path.join("C:\\", "UNIDADES", "UNIDADES")

arquivos = ["systeminfo.txt", "ipconfig.txt", "disk.txt", "mem.txt", "cpu.txt", "dumpedid.txt", "mouse e teclado.txt"]

# Lista para armazenar as informações de todos os arquivos



def caminhar(caminho):
    dados_completos = []
    old_folder = ""

    with open("Computadores.csv", "w", encoding="utf-8") as fd:
        for root, subfolders, files in os.walk(caminho) :

                if "CELULARES" and "REUNIÃO"in root:
                    continue

                if old_folder and root != old_folder:
                    fd.write(old_folder + ';' + ';'.join(dados_completos) + '\n')
                    dados_completos = []
                old_folder = root

                for nome_arquivo in files:

                    if "REUNIÃO" in root or "CELULARES" in root or nome_arquivo.lower() not in arquivos:
                        continue

                    caminho_arquivo = os.path.join(root, nome_arquivo)
                    print(caminho_arquivo)

                        # Verificação se o arquivo existe
                    if os.path.exists(caminho_arquivo):

                      #se caminho_arquivo conter .txt se caminhi_arquivo terminar com .png
                        if ".txt" in caminho_arquivo:
                            dados = extrair_informacoes(caminho_arquivo)
                            dados_completos.extend(dados)
                        if ".png" or ".jpg" in caminho_arquivo:
                            dados = extrair_informacoes(caminho_arquivo)
                            dados_completos.extend(dados)

                    for dado in dados:
                     print(dado)
                     print("-" * 50)



if __name__ == "__main__":
    caminhar(caminho_base)




