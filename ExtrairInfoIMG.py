# import pytesseract
# import cv2
# import re
# from PIL import Image

# # __________________________IMAGEM DE INFORMAÇÃO______________________________________
# # Caminho da Imagem
# # Converter IMG para PNG
# informacoes = []



# # Identificar luminosidade da imagem
# def luminosidade(caminho_img):
#     imagem = Image.open(caminho_img)
#     imagem = imagem.convert('L')  # Converte para escala de cinza
#     pixels = list(imagem.getdata())
#     media = sum(pixels) / len(pixels)
#     return media





# # Converter IMG jfif para png
# def convertjfif(caminho_imagem):


#     # Abrir a imagem
#     imagem = Image.open(caminho_imagem)

#     # Abrir a imagem
#     imagem = Image.open(caminho_imagem)
#     # Salvar a imagem como PNG
#     novo_caminho = caminho_imagem.replace(".jfif", ".png")
#     imagem.save(novo_caminho, 'PNG')
#     return novo_caminho




# # Scanear Imagem OCR
# def ocrImagem(caminho_img):

#     if "jfif" in caminho_img:
#         caminho_img = convertjfif(caminho_img)

#         ocrImagem(caminho_img)


#     imagem = cv2.imread(caminho_img)
#     # Verificar Luminosidade
#     media_luminosidade = luminosidade(caminho_img)
#     print("Luminosidade: " + str(media_luminosidade))
#     caminho_tesseract = ('C:\Program Files\Tesseract-OCR')
#     pytesseract.pytesseract.tesseract_cmd = caminho_tesseract + r"\tesseract.exe"
#     # Extrai o texto
#     texto = pytesseract.image_to_string(imagem)
#     print(texto)




# # # Dark Default Samsung :

# # Main screen 1 - 15.19301710348222 | Parameters ('Galaxy')
#     if 'Galaxy' in texto and media_luminosidade > 10 and media_luminosidade < 23:


#         regex_nome = r'(Galaxy.*)'
#         regex_numero = r'([+]55.*)'
#         regex_modelo = r'(SM.*)'
#         regex_serie = r'.*\s([A-Z\d]{11})\s.*'

#         informacoes.append(f"{re.search(regex_nome, texto).group(1).strip(
#         ) if re.search(regex_nome, texto).group(1).strip() != '' and len(re.search(regex_nome, texto).group(1).strip()) < 25 else 'N/A'}")

#         informacoes.append(f"{re.search(regex_modelo, texto).group(1).strip(
#         ) if re.search(regex_modelo, texto).group(1).strip() != ''and len(re.search(regex_modelo, texto).group(1).strip()) < 25 else 'N/A'}")

#         informacoes.append(f"{re.search(regex_numero, texto).group(1).strip(
#         ) if re.search(regex_numero, texto).group(1).strip() != '' and len(re.search(regex_numero, texto).group(1).strip()) < 25 else 'N/A'}")

#         informacoes.append(f"{re.search(regex_serie, texto).group(1).strip(
#         ) if re.search(regex_serie, texto).group(1).strip() != '' and len(re.search(regex_serie, texto).group(1).strip()) < 13 else 'N/A'}")

#         print("Infos:\n")
#         print(informacoes)
#     else:
#          pass





# # Main screen 2 - 28.01311408016444 | Parameters ('Galaxy')
#     if 'Galaxy' in texto and media_luminosidade > 24 and media_luminosidade < 30:

#         regex_nome = r'(Galaxy.*)'
#         regex_modelo = r'(SM.*)'
#         regex_numero = r'Numero de telefone [(]Slot1[)]\s*(.*)'
#         regex_serie = r'.*\s([A-Z\d]{11})\s.*'
#         regex_imei = r'^.*([0-9\d]{15}).*([0-9\d]{15}).*$'

#         informacoes.append(f"{re.search(regex_nome, texto).group(1).strip(
#         ) if re.search(regex_nome, texto).group(1).strip() != '' and len(re.search(regex_nome, texto).group(1).strip()) < 25 else 'N/A'}")

#         informacoes.append(f"{re.search(regex_modelo, texto).group(1).strip(
#         ) if re.search(regex_modelo, texto).group(1).strip() != ''and len(re.search(regex_modelo, texto).group(1).strip()) < 25 else 'N/A'}")

#         informacoes.append(f"{re.search(regex_numero, texto).group(1).strip(
#         ) if re.search(regex_numero, texto).group(1).strip() != '' and len(re.search(regex_numero, texto).group(1).strip()) < 25 else 'N/A'}")

#         informacoes.append(f"{re.search(regex_serie, texto).group(1).strip(
#         ) if re.search(regex_serie, texto).group(1).strip() != '' and len(re.search(regex_serie, texto).group(1).strip()) < 13 else 'N/A'}")

#         informacoes.append(f"{re.search(regex_imei, texto, re.DOTALL).group(1).strip(
#         ) if re.search(regex_imei, texto, re.DOTALL).group(1).strip() != '' and len(re.search(regex_imei, texto, re.DOTALL).group(1).strip()) < 25 else 'N/A'}")

#         informacoes.append(f"{re.search(regex_imei, texto, re.DOTALL).group(2).strip(
#         ) if re.search(regex_imei, texto, re.DOTALL).group(2).strip() != '' and len(re.search(regex_imei, texto, re.DOTALL).group(2).strip()) < 25 else 'N/A'}")

#         print("Infos:\n")
#         print(informacoes)
#     else:
#          pass





# # # Barcode Screen - 43.44098221976129| Parameters ('IMEI')
#     if 'IMEI' in texto and media_luminosidade > 35 and media_luminosidade < 60:

#         regex_imei = r'^.*([0-9\d]{15}).*([0-9\d]{15}).*$'

#         informacoes.append(f"{re.search(regex_imei, texto, re.DOTALL).group(1).strip(
#         ) if re.search(regex_imei, texto, re.DOTALL).group(1).strip() != '' and len(re.search(regex_imei, texto, re.DOTALL).group(1).strip()) < 25 else 'N/A'}")
#         informacoes.append(f"{re.search(regex_imei, texto, re.DOTALL).group(2).strip(
#         ) if re.search(regex_imei, texto, re.DOTALL).group(2).strip() != '' and len(re.search(regex_imei, texto, re.DOTALL ).group(2).strip()) < 25 else 'N/A'}")

#         print("Infos:\n")
#         print(informacoes)
#     else:
#         pass





# # Light Default Samsung :

# # Main screen 1 - 238.98211558577407 | Parameters ('Galaxy')
#     if 'Galaxy' in texto and media_luminosidade > 180 and media_luminosidade < 240:

#             regex_nome = r'(Galaxy.*)'
#             regex_numero = r'([+]55.*)'
#             regex_modelo = r'(SM.*)'
#             regex_serie = r'.*\s([A-Z\d]{11})\s.*'

#             informacoes.append(f"{re.search(regex_nome, texto).group(1).strip(
#             ) if re.search(regex_nome, texto).group(1).strip() != '' and len(re.search(regex_nome, texto).group(1).strip()) < 25 else 'N/A'}")
#             informacoes.append(f"{re.search(regex_modelo, texto).group(1).strip(
#             ) if re.search(regex_modelo, texto).group(1).strip() != ''and len(re.search(regex_modelo, texto).group(1).strip()) < 25 else 'N/A'}")
#             informacoes.append(f"{re.search(regex_numero, texto).group(1).strip(
#             ) if re.search(regex_numero, texto).group(1).strip() != '' and len(re.search(regex_numero, texto).group(1).strip()) < 25 else 'N/A'}")
#             informacoes.append(f"{re.search(regex_serie, texto).group(1).strip(
#             ) if re.search(regex_serie, texto).group(1).strip() != '' and len(re.search(regex_serie, texto).group(1).strip()) < 13 else 'N/A'}")

#             print("Infos:\n")
#             print(informacoes)
#     else:
#             pass




# # Main screen 2 - 241.80702989366318 | Parameters ('Galaxy')
#     if 'Galaxy' in texto and media_luminosidade > 240 and media_luminosidade < 300:

#             regex_nome = r'(Galaxy.*)'
#             regex_modelo = r'(SM.*)'
#             regex_numero = r'([0-9]{13})'
#             regex_serie = r'.*\s([A-Z\d]{11})\s.*'
#             regex_imei = r'^.*([0-9\d]{15}).*([0-9\d]{15}).*$'

#             informacoes.append(f"{re.search(regex_nome, texto).group(1).strip(
#             ) if re.search(regex_nome, texto).group(1).strip() != '' and len(re.search(regex_nome, texto).group(1).strip()) < 25 else 'N/A'}")

#             informacoes.append(f"{re.search(regex_modelo, texto).group(1).strip(
#             ) if re.search(regex_modelo, texto).group(1).strip() != ''and len(re.search(regex_modelo, texto).group(1).strip()) < 25 else 'N/A'}")

#             informacoes.append(f"{re.search(regex_numero, texto).group(1).strip(
#             ) if re.search(regex_numero, texto).group(1).strip() != '' and len(re.search(regex_numero, texto).group(1).strip()) < 25 else 'N/A'}")

#             informacoes.append(f"{re.search(regex_serie, texto).group(1).strip(
#             ) if re.search(regex_serie, texto).group(1).strip() != '' and len(re.search(regex_serie, texto).group(1).strip()) < 13 else 'N/A'}")

#             informacoes.append(f"{re.search(regex_imei, texto, re.DOTALL).group(1).strip(
#             ) if re.search(regex_imei, texto, re.DOTALL).group(1).strip() != '' and len(re.search(regex_imei, texto, re.DOTALL).group(1).strip()) < 25 else 'N/A'}")

#             informacoes.append(f"{re.search(regex_imei, texto, re.DOTALL).group(2).strip(
#             ) if re.search(regex_imei, texto, re.DOTALL).group(2).strip() != '' and len(re.search(regex_imei, texto, re.DOTALL).group(2).strip()) < 25 else 'N/A'}")

#             print("Infos :\n")
#             print(informacoes)
#     else:
#         pass

#     return informacoes





















import pytesseract
import cv2
import re
from PIL import Image

# Identificar luminosidade da imagem
def luminosidade(caminho_img):
    imagem = Image.open(caminho_img)
    imagem = imagem.convert('L')  # Converte para escala de cinza
    pixels = list(imagem.getdata())
    media = sum(pixels) / len(pixels)
    return media

# Converter IMG jfif para png
def convertjfif(caminho_imagem):
    # Abrir a imagem
    imagem = Image.open(caminho_imagem)
    # Salvar a imagem como PNG
    novo_caminho = caminho_imagem.replace(".jfif", ".png")
    imagem.save(novo_caminho, 'PNG')
    return novo_caminho

# Função auxiliar para buscar regex com segurança
def buscar_regex(regex, texto, grupo):

    match = re.search(regex, texto)
    return match.group(grupo).strip() if match and match.group(grupo).strip() != '' else 'N/A'

def buscar_regex_dotall(regex, texto, grupo):

    match = re.search(regex, texto, re.DOTALL)
    return match.group(grupo).strip() if match and match.group(grupo).strip() != '' else 'N/A'

# Scanear Imagem OCR
def ocrImagem(caminho_img):
    # Verificar se o arquivo é jfif e converter
    if ".jfif" in caminho_img:
        caminho_img = convertjfif(caminho_img)

    # Verificar se a imagem foi carregada corretamente
    imagem = cv2.imread(caminho_img)
    if imagem is None:
        print(f"Erro ao carregar a imagem: {caminho_img}")
        return []

    # Verificar Luminosidade
    media_luminosidade = luminosidade(caminho_img)
    print("Luminosidade: " + str(media_luminosidade))
    caminho_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    pytesseract.pytesseract.tesseract_cmd = caminho_tesseract
    # Extrair o texto
    texto = pytesseract.image_to_string(imagem)
    # print(texto)

    informacoes = []

    # # Dark Default Samsung
    if 'Galaxy' in texto and 10 < media_luminosidade < 23:
        regex_nome = r'(Galaxy.*)'
        regex_numero = r'([+]55.*)'
        regex_modelo = r'(SM.*)'
        regex_serie = r'.*\s([A-Z\d]{11})\s.*'

        informacoes.extend([
            buscar_regex(regex_nome, texto, 1),
            buscar_regex(regex_modelo, texto, 1),
            buscar_regex(regex_numero, texto, 1),
            buscar_regex(regex_serie, texto, 1)
        ])
        print("Infos:\n")
        print(informacoes)

    # Main screen 2
    elif 'Galaxy' in texto and 24 < media_luminosidade < 30:
        regex_nome = r'(Galaxy.*)'
        regex_modelo = r'(SM.*)'
        regex_numero = r'Numero de telefone [(]Slot1[)]\s*(.*)'
        regex_serie = r'.*\s([A-Z\d]{11})\s.*'
        regex_imei = r'^.*([0-9\d]{15}).*([0-9\d]{15}).*$'

        informacoes.extend([
            buscar_regex(regex_nome, texto, 1),
            buscar_regex(regex_modelo, texto, 1),
            buscar_regex(regex_numero, texto, 1),
            buscar_regex(regex_serie, texto, 1),
            buscar_regex_dotall(regex_imei, texto, 1),
            buscar_regex_dotall(regex_imei, texto, 2)
        ])
        print("Infos:\n")
        print(informacoes)

    # Barcode Screen
    elif 'IMEI' in texto and 35 < media_luminosidade < 60:
        regex_imei = r'^.*([0-9\d]{15}).*([0-9\d]{15}).*$'

        informacoes.extend([
            buscar_regex_dotall(regex_imei, texto, 1),
            buscar_regex_dotall-(regex_imei, texto, 2)
        ])
        print("Infos:\n")
        print(informacoes)




    # Light Default Samsung
    elif 'Galaxy' in texto and 180 < media_luminosidade < 240:
        regex_nome = r'(Galaxy.*)'
        regex_numero = r'([+]55.*)'
        regex_modelo = r'(SM.*)'
        regex_serie = r'.*\s([A-Z\d]{11})\s.*'

        informacoes.extend([
            buscar_regex(regex_nome, texto, 1),
            buscar_regex(regex_modelo, texto, 1),
            buscar_regex(regex_numero, texto, 1),
            buscar_regex(regex_serie, texto, 1)
        ])
        print("Infos:\n")
        print(informacoes)

    # Main screen 2 - Light Default Samsung
    elif 'Galaxy' in texto and 240 < media_luminosidade < 300:
        regex_nome = r'(Galaxy.*)'
        regex_modelo = r'(SM.*)'
        regex_numero = r'([0-9]{13})'
        regex_serie = r'.*\s([A-Z\d]{11})\s.*'
        regex_imei = r'^.*([0-9\d]{15}).*([0-9\d]{15}).*$'

        informacoes.extend([
            buscar_regex(regex_nome, texto, 1),
            buscar_regex(regex_modelo, texto, 1),
            buscar_regex(regex_numero, texto, 1),
            buscar_regex(regex_serie, texto, 1),
            buscar_regex_dotall(regex_imei, texto, 1),
            buscar_regex_dotall(regex_imei, texto, 2),
        ])
        print("Infos:\n")
        # print(informacoes)

    return informacoes














