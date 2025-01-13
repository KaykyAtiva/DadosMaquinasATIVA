import re
import chardet


def detectar_codificacao(caminho_arquivo):

    # Detecta a codificação do arquivo
    with open(caminho_arquivo, 'rb') as arquivo:
        dados = arquivo.read()
        resultado = chardet.detect(dados)
        codificacao = resultado['encoding']
    return codificacao

def extrair_informacoes(caminho_arquivo):


    codificacao = detectar_codificacao(caminho_arquivo)

    # Abrindo e Lendo o arquivo txt
    with open(caminho_arquivo, 'r', encoding= codificacao ) as arquivo:
        texto = arquivo.read()

#*************************************************************************************
# **************************Dados do Sistema e PC*************************************
# ************************************************************************************

        if "SYSTEMINFO.txt" in caminho_arquivo:

            # Expressões regulares 
            regex_host = r'Nome do host:\s*(.*)'
            regex_sistema = r'Nome do sistema operacional:\s*(.*)'
            regex_placamae = r'Modelo do sistema:\s*(.*)'
            regex_bios = r'BIOS:\s*(.*)'
            regex_ip =r'IP\s*\[01\]:\s*([\d]+\.[\d]+\.[\d]+\.[\d]+)'
            regex_versao_sistema = r'Vers...........................\s*(.*)'


            # Encontrando usando re.search

            host = re.search(regex_host, texto)
            sistema = re.search(regex_sistema, texto)
            versao_sistema = re.search(regex_versao_sistema, texto)
            placamae= re.search(regex_placamae, texto)
            bios= re.search(regex_bios, texto)
            ip = re.search(regex_ip, texto)

        elif "IPCONFIG.txt" in caminho_arquivo:

            # Expressões regulares 
            regex_mac = r'([A-F0-9]{2}(-[A-F0-9]{2}){5})'


            # Encontrando usando re.search
            mac = re.search(regex_mac, texto)

        elif "DISK.txt" in caminho_arquivo:

            # Expressões regulares 
            regex_disk = r'\n\s*(.*)'


            # Encontrando usando re.search
            disk = re.compile(regex_disk, texto, re.DOTALL)
            
        elif "MEM.txt" in caminho_arquivo:

            # Expressões regulares 
            regex_ram = r"^.*\n(\d*) *(\d*) *\w* \d *([\w-]*) *(\w*).*$"

            # Encontrando usando re.search
            ram = re.search(regex_ram, texto, re.MULTILINE)
            ram_nome = {ram.group(1).strip()}
            ram_serial = {ram.group(4).strip()}
            ram_speed = {ram.group(2).strip()}
        
        elif "CPU.txt" in caminho_arquivo:

            # Expressões regulares 
            regex_cpu = r"(\d+)\s+(\d+)\s+(.+)\s+(\d+)\s+(.+)\s+(\d+)"
            cpu = re.search(regex_cpu, texto)


#*************************************************************************************
# *******************************Dados do Sistema*************************************
# ************************************************************************************

        

        # # Print text
        #   if cpu != None:
        #     print(f"Nome do Processador: {cpu.group(3).strip()}")
        # if host != None:
        #     print(f"Nome do Host: {host.group(1).strip()}")
        if sistema != None:
            print(f"Nome do Sistema Operacional: {sistema.group(1).strip()}")
        # if placamae != None:
        #     print(f"Modelo Placa Mãe: {placamae.group(1).strip()}")
        # if bios != None:
        #     print(f"BIOS: {bios.group(1).strip()}")
        # if ip != None:
        #     print(f"IP: {ip.group(1).strip()}")
        # if mac != None:
        #     print(f"MAC: {mac.group(1).strip()}")
        # if disk != None:
        #     print(f"DISCO RIGIDO: " + disk.group(1).replace("\n", ""))
        # if ram != None:
    
        #     print(f"Memoria Ram: {ram.group(1).strip()}")
        #     print(f"SerialNumber: {ram.group(4).strip()}")
        #     print(f"Speed: {ram.group(2).strip()}")
        
        if versao_sistema :
            print(f"Versão do Sistema: {versao_sistema.group(1).strip()}") 
 





caminho_arquivo = "C:\\GitHub\\TermoResponsabilidadePc\\SYSTEMINFO.txt"


extrair_informacoes(caminho_arquivo)








