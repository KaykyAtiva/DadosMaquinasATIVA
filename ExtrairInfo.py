import re
import DetectarCodificacao as dt
import CapturarNulo as cn



def extrair_informacoes(caminho_arquivo):
        codificacao = dt.detectar_codificacao(caminho_arquivo)


    # Abrindo e Lendo o arquivo txt
        with open(caminho_arquivo, 'r', encoding=codificacao) as arquivo:
            texto = arquivo.read()


            #  armazenar os dados extraídos
        informacoes = []

        # Dados do Sistema e PC
        if "SYSTEMINFO.txt" in caminho_arquivo:
            regex_host = r'Nome do host:\s*(.*)'
            regex_sistema = r'Nome do sistema operacional:\s*(.*)'
            regex_placamae = r'Modelo do sistema:\s*(.*)'
            regex_bios = r'BIOS:\s*(.*)'
            regex_versao_sistema = r'Vers.*:\s*(.*)'

            # Extracao e formatacao
            host = cn.capturar_nulo(re.search(regex_host, texto))
            informacoes.append(
                f"{host.group(1).strip() if host.group(1).strip() != '' else 'N/A'}")

            sistema = cn.capturar_nulo(re.search(regex_sistema, texto))
            informacoes.append(
                f"{sistema.group(1).strip() if sistema.group(1).strip() != '' else 'N/A'}")

            versao_sistema = cn.capturar_nulo(
                re.search(regex_versao_sistema, texto))
            informacoes.append(f"{versao_sistema.group(1).strip(
            ) if versao_sistema.group(1).strip() != '' else 'N/A'}")

            placamae = cn.capturar_nulo(re.search(regex_placamae, texto))
            informacoes.append(
                f"{placamae.group(1).strip() if placamae.group(1).strip() != '' else 'N/A'}")

            bios = cn.capturar_nulo(re.search(regex_bios, texto))
            informacoes.append(
                f"{bios.group(1).strip() if bios.group(1).strip() != '' else 'N/A'}")



        else:
            pass

        if "IPCONFIG.txt" in caminho_arquivo:
            regex_mac = r'([A-F0-9]{2}(-[A-F0-9]{2}){5})'
            regex_ip = r'IPv4.*:(.*)'

            mac = cn.capturar_nulo(re.search(regex_mac, texto))
            informacoes.append(f"MAC: {mac.group(1).strip() if mac and mac.group(1).strip() != '' else 'N/A'}")

            ip = cn.capturar_nulo(re.search(regex_ip, texto))
            informacoes.append(f"{ip.group(1).strip() if ip and ip.group(1).strip() != '' else  'N/A' }")

        else:
            pass

        if "DISK.txt" in caminho_arquivo:
            regex_disk = r'\n\s*(.*)'
            disk = cn.capturar_nulo(re.search(regex_disk, texto, re.DOTALL))
            informacoes.append(f"DISCO RIGIDO: {disk.group(1).replace(
                '\n', '').strip() if disk and disk.group(1).strip() != '' else 'N/A'}")
        else:
            pass

        if "MEM.txt" in caminho_arquivo:
            regex_ram = r"^.*\n(\d*) *(\d*) *\w* \d *([\w-]*) *(\w*).*$"
            ram = cn.capturar_nulo(re.search(regex_ram, texto, re.MULTILINE))
            informacoes.append(
                f"RAM: {ram.group(1).strip() if ram and ram.group(
                    1).strip() != '' else 'N/A'} Kbs | "
                f"Serial: {ram.group(4).strip() if ram and ram.group(
                    4).strip() != '' else 'N/A'} | "
                f"Frequência: {ram.group(2).strip() if ram and ram.group(
                    2).strip() != '' else 'N/A'}"
            )
        else:
            pass

        if "CPU.txt" in caminho_arquivo:
            regex_cpu = r"(\d+)\s+(\d+)\s+(.+)\s+(\d+)\s+(.+)\s+(\d+)"
            cpu = cn.capturar_nulo(re.search(regex_cpu, texto))
            informacoes.append(f"Nome do Processador: {cpu.group(
                3).strip() if cpu and cpu.group(3).strip() != '' else 'N/A'}")
        else:
            pass

        if "dumpedid.txt" in caminho_arquivo:
            regex_monitor = r"Registry.Key...............\s*(.*)"
            regex_resolucao_heartz = r"Display.Modes.*\s*(...........)..(.*)"

            monitor = cn.capturar_nulo(re.search(regex_monitor, texto))
            informacoes.append(f"Registry Key: {monitor.group(1).strip(
            ) if monitor and monitor.group(1).strip() != '' else 'N/A'}")

            resolucao_heartz = cn.capturar_nulo(
                re.search(regex_resolucao_heartz, texto))
            informacoes.append(f"Resolução: {resolucao_heartz.group(1).strip(
            ) if resolucao_heartz and resolucao_heartz.group(1).strip() != '' else 'N/A'}")
        else:
            pass

        if "MOUSE E TECLADO.txt" in caminho_arquivo:
            regex_mouse = r"(.*)"
            regex_teclado = r"\n(.*)"

            mouse = cn.capturar_nulo(re.search(regex_mouse, texto))
            informacoes.append(
                f"{mouse.group(1).strip() if mouse and mouse.group(1).strip() != '' else 'N/A'}")

            teclado = cn.capturar_nulo(re.search(regex_teclado, texto))
            informacoes.append(f"{teclado.group(1).strip(
            ) if teclado and teclado.group(1).strip() != '' else 'N/A'}")
        else:
            pass

        return informacoes
