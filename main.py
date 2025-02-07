from ExtrairInfo import extrair_informacoes
from ExtrairInfoIMG import ocrImagem
from ExtrairInfoIMG import convertjfif
import os
caminho_base = os.path.join("C:\\", "UNIDADES", "UNIDADES")

arquivos = ["systeminfo.txt", "ipconfig.txt", "disk.txt", "mem.txt", "cpu.txt", "dumpedid.txt", "mouse e teclado.txt"]

# Lista para armazenar as informações de todos os arquivos



def caminhar(caminho):
    dados_completos = []
    old_folder = ""

    with open("Computadores.csv", "w", encoding="utf-8") as fd:
        for root, subfolders, files in os.walk(caminho) :

                ##PULAR PASTAS REUNIAO
                if "REUNIÃO"in root:
                   continue

                if old_folder and root != old_folder:
                    fd.write(old_folder + ';' + ';'.join(dados_completos) + '\n')
                    dados_completos = []
                old_folder = root

                for nome_arquivo in files:

                    caminho_arquivo = os.path.join(root, nome_arquivo)
                    print(caminho_arquivo)



                    if "txt" in caminho_arquivo:

                                dados = extrair_informacoes(caminho_arquivo)
                                dados_completos.extend(dados)


                    if any(ext in caminho_arquivo for ext in ["png", "jpeg", "jfif", "jpg"]):
                        if "jfif" in caminho_arquivo:
                            # caminho_modificado = convertjfif(caminho_arquivo)
                            # dados = ocrImagem(caminho_modificado)
                            pass
                        else:
                            dados = ocrImagem(caminho_arquivo)
                        dados_completos.extend(dados)


                


if __name__ == "__main__":
    caminhar(caminho_base)




