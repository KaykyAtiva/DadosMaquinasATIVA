import pytesseract
import cv2
import re
from PIL import Image

#__________________________IMAGEM DE INFORMAÇÃO______________________________________
#Caminho da Imagem
#Converter IMG para PNG
def convertjfif(caminho_imagem):

    # Abrir a imagem
    imagem = Image.open(caminho_imagem)

    # Salvar a imagem como PNG
    imagem.save(caminho_imagem.replace(".jfif", "") + '.png', 'PNG')
    return  caminho_imagem.replace(".jfif", "") + '.png'

#Scanear Imagem OCR
def ocrImagem(caminho_img):

        imagem = cv2.imread(caminho_img)
        #Verificar Luminosidade
        media_luminosidade = luminosidade(caminho_img)
        print("Luminosidade: " + str(media_luminosidade))
        caminho_tesseract = ('C:\Program Files\Tesseract-OCR')
        pytesseract.pytesseract.tesseract_cmd = caminho_tesseract + r"\tesseract.exe"
         # Extrai o texto
        texto = pytesseract.image_to_string(imagem)
        print(texto)

        # # Dark Default Samsung :

        # Main screen 1 - 15.19301710348222 | Parameters ('Galaxy')
        # if 'Galaxy' in texto  and media_luminosidade > 10 and media_luminosidade < 23:


        #     regex_nome = r'(Galaxy.*)'
        #     regex_numero = r'([+]55.*)'
        #     regex_modelo = r'(SM.*)'
        #     regex_serie= r'.*\s([A-Z\d]{11})\s.*'

        #     informacoes.append(f"{re.search(texto, regex_nome).group(1).strip() if re.search(texto, regex_nome).group(1).strip() != '' else  'N/A' }")
        #     informacoes.append(f"{re.search(texto, regex_numero).group(1).strip() if re.search(texto, regex_numero).group(1).strip() != '' else  'N/A' }")
        #     informacoes.append(f"{re.search(texto, regex_modelo).group(1).strip() if re.search(texto, regex_modelo).group(1).strip() != '' else  'N/A' }")
        #     informacoes.append(f"{re.search(texto, regex_serie).group(1).strip() if re.search(texto, regex_serie).group(1).strip() != '' else  'N/A' }")

        #     print("Infos:\n")
        #     print(informacoes)
        # else:
        #     pass
         # # # Barcode Screen - 43.44098221976129| Parameters ('IMEI')
        if 'IMEI' in texto and media_luminosidade > 35 and media_luminosidade < 60 :

            regex_imei = r'^.*([0-9\d]{15}).*([0-9\d]{15}).*$'

            informacoes.append(f"{re.search(texto, regex_imei).group(1).strip() if re.search(texto, regex_imei).group(1).strip() != '' else  'N/A' }")
            informacoes.append(f"{re.search(texto, regex_imei).group(2).strip() if re.search(texto, regex_imei).group(2).strip() != '' else  'N/A' }")




        # # Main screen 2 - 28.01311408016444 | Parameters ('Galaxy')
        # if 'Galaxy' in texto and media_luminosidade > 24 and media_luminosidade < 30 :

        #     regex_nome = r'(Galaxy.*)'
        #     regex_modelo = r'(SM.*)'
        #     regex_numero = r'Numero de telefone [(]Slot1[)]\s*(.*)'
        #     regex_serie= r'.*\s([A-Z\d]{11})\s.*'
        #     regex_imei1 = r'IMEI [(]Slot1[)]\s\s(.*)'
        #     regex_imei2 = r'IMEI [(]Slot2[)]\s\s(.*)'

        #     informacoes.append(f"{re.search(texto, regex_nome).group(1).strip() if re.search(texto, regex_nome).group(1).strip() != '' else  'N/A' }")
        #     informacoes.append(f"{re.search(texto, regex_modelo).group(1).strip() if re.search(texto, regex_modelo).group(1).strip() != '' else  'N/A' }")
        #     informacoes.append(f"{re.search(texto, regex_numero).group(1).strip() if re.search(texto, regex_numero).group(1).strip() != '' else  'N/A' }")
        #     informacoes.append(f"{re.search(texto, regex_serie).group(1).strip() if re.search(texto, regex_serie).group(1).strip() != '' else  'N/A' }")
        #     informacoes.append(f"{re.search(texto, regex_imei1).group(1).strip() if re.search(texto, regex_imei1).group(1).strip() != '' else  'N/A' }")
        #     informacoes.append(f"{re.search(texto, regex_imei2).group(1).strip() if re.search(texto, regex_imei2).group(1).strip() != '' else  'N/A' }")
        #     print("Infos:\n")
        #     print(informacoes)

        # else:
        #     pass








    # Light Default Samsung :
    # Main screen 1 - 238.98211558577407 | Parameters ('Galaxy')
    # Main screen 2 - 241.80702989366318 | Parameters ('Galaxy')
    # Barcode Screen - 43.44098221976129| Parameters ('IMEI')













        # print(texto)
        # palavras = re.search(texto)

        # informacoes.append(f"{palavras.group(1).strip() if palavras.group(1).strip() != '' else  'N/A' }")
        # informacoes.append(f"{palavras.group(2).strip() if palavras.group(2).strip() != '' else  'N/A' }")
        # informacoes.append(f"{palavras.group(3).strip() if palavras.group(3).strip() != '' else  'N/A' }")
        # print("Infos:\n")
        # print(informacoes)

#Identificar qual padrao da imagem (PADRAO 1 (Escura, Clara) PADRAO 2 (Escura ou Clara))
#Fazer a Def de REGEX para coleta das informações

#__________________________IMAGEM DE CODIGO DE BARRAS______________________________________
#Caminho da Imagem
#Converter IMG para PNG
#Scanear Imagem OCR
#Se texto imagem conter a string IMEI executar o regex solicitado


informacoes = []

#verificar luiminosidade da imagem e retornar media de liuminosidade metodo
def luminosidade(caminho_img):
    imagem = Image.open(caminho_img)
    imagem = imagem.convert('L')  # Converte para escala de cinza
    pixels = list(imagem.getdata())
    media = sum(pixels) / len(pixels)
    return media









# Abre a imagem

if __name__ == "__main__":

   caminho_img = "DBC.png"

   if ".jfif" in caminho_img:
    caminho_img = convertjfif(caminho_img)


   print("CAMINHO SALVO: " + caminho_img)
   ocrImagem(caminho_img)









