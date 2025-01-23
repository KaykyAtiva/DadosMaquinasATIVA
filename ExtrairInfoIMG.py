import pytesseract
import cv2
import re

caminho_img = "Teste\\teste.png"

informacoes = []

def regex(texto):

    regex = r'telefone\s...(.*)\s*(.*)\s*............(.*)'

    # Encontra todas as palavras com 3 letras
    result = re.search(regex, texto)

    return result




def ocrImagem(caminho_img):

    if "" in caminho_img:
        imagem = cv2.imread(caminho_img)

        caminho_tesseract = ('C:\Program Files\Tesseract-OCR')
        pytesseract.pytesseract.tesseract_cmd = caminho_tesseract + r"\tesseract.exe"
        # Extrai o texto
        texto = pytesseract.image_to_string(imagem)

        print(texto)
        palavras = regex(texto)

        informacoes.append(f"{palavras.group(1).strip() if palavras.group(1).strip() != '' else  'N/A' }")
        informacoes.append(f"{palavras.group(2).strip() if palavras.group(2).strip() != '' else  'N/A' }")
        informacoes.append(f"{palavras.group(3).strip() if palavras.group(3).strip() != '' else  'N/A' }")


# Abre a imagem

if __name__ == "__main__":

    ocrImagem(caminho_img)
