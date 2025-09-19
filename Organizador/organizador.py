import os
import shutil
from datetime import datetime
import time

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# --- LÓGICA 1: Organizar por Categoria (com mapa) ---
def organizar_por_categoria(diretorio):
    categorias = {
    "Scripts": ['.bat', '.ps1', '.cmd', '.py', '.rb', '.js', '.ts', '.sh', '.ksh',
                '.zsh', '.pl', '.php', '.vbs', '.lua', '.groovy'],
    "Executaveis": ['.exe', '.msi', '.apk', '.app', '.deb', '.rpm', '.jar', '.war', '.bin'],
    "Imagens": ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.ico', '.heic', '.raw', '.webp'],
    "Videos": ['.mp4', '.avi', '.mov', '.wmv', '.mkv', '.webm', '.flv', '.mpeg', '.mpg', '.3gp'],
    "Audio": ['.mp3', '.wav', '.ogg', '.flac', '.aac', '.m4a', '.wma', '.mid'],
    "Documentos": ['.pdf', '.docx', '.doc', '.dotx', '.txt', '.rtf', '.odt', '.md', '.epub', '.mobi'],
    "Planilhas": ['.xlsx', '.xlsb', '.xlsm', '.xls', '.csv', '.ods', '.xltx', '.xltm', '.dbf', '.sav'],
    "Apresentacoes": ['.pptx', '.ppt', '.odp', '.key'],
    "Compactados": ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.iso'],
    "Banco de ados": ['.sql', '.sqlite', '.db', '.accdb', '.mdb', '.bak', '.dump'],
    "Atalhos": ['.lnk', '.alias', '.url', '.webloc', '.pif', '.desktop'],
    "Logs": ['.log'],
    "Configuracoes": ['.ini', '.json', '.xml', '.yaml', '.yml', '.cfg']
    }
    MAPA_DE_PASTAS = {
    ext: f"{cat}/{ext[1:].upper()}"
    for cat, lista in categorias.items()
    for ext in lista
    }
    
    for item_nome in os.listdir(diretorio):
        caminho_original = os.path.join(diretorio, item_nome)
        if os.path.isfile(caminho_original):
            nome, extensao = os.path.splitext(item_nome)
            pasta_destino_nome = MAPA_DE_PASTAS.get(extensao.lower(), f'Outros/{extensao[1:].upper()}')
            pasta_destino_caminho = os.path.join(diretorio, pasta_destino_nome)
            if not os.path.exists(pasta_destino_caminho):
                os.makedirs(pasta_destino_caminho)
            shutil.move(caminho_original, os.path.join(pasta_destino_caminho, item_nome))
    print("Organização por categoria concluída!")
    time.sleep(1.5)

# --- LÓGICA 2: Organizar por Extensão Exata ---
def organizar_por_extensao(diretorio):
    for item_nome in os.listdir(diretorio):
        caminho_original = os.path.join(diretorio, item_nome)
        if os.path.isfile(caminho_original):
            nome, extensao = os.path.splitext(item_nome)
            if extensao:
                pasta_destino_nome = extensao[1:].upper()
                pasta_destino_caminho = os.path.join(diretorio, pasta_destino_nome)
                if not os.path.exists(pasta_destino_caminho):
                    os.makedirs(pasta_destino_caminho)
                shutil.move(caminho_original, os.path.join(pasta_destino_caminho, item_nome))
    print("Organização por extensão concluída!")
    time.sleep(1.5)

# --- LÓGICA 3: Organizar por Data de Modificação ---
def organizar_por_data(diretorio):
    for item_nome in os.listdir(diretorio):
        caminho_original = os.path.join(diretorio, item_nome)
        if os.path.isfile(caminho_original):
            timestamp = os.path.getmtime(caminho_original)
            data_mod = datetime.fromtimestamp(timestamp)
            pasta_destino_nome = data_mod.strftime('%m-%Y')
            pasta_destino_caminho = os.path.join(diretorio, pasta_destino_nome)
            if not os.path.exists(pasta_destino_caminho):
                os.makedirs(pasta_destino_caminho)
            shutil.move(caminho_original, os.path.join(pasta_destino_caminho, item_nome))
    print("Organização por data concluída!")
    time.sleep(1.5)

# --- MENU PRINCIPAL ---
while True:
    limpar_tela()
    print("\n--- Organizador de Arquivos ---")
    print("1. Organizar por Categoria")
    print("2. Organizar por Extensão Exata")
    print("3. Organizar por Data de Modificação")
    print("4. Sair")
    
    escolha = input("Escolha uma opção: ")

    if escolha == '4':
        limpar_tela()
        break
    
    if escolha in ['1', '2', '3']:
        diretorio_alvo = input("Digite o caminho da pasta para organizar ou arraste a pasta aqui: ").strip('"')

        if not os.path.isdir(diretorio_alvo):
            print(f"ERRO: O caminho '{diretorio_alvo}' não é um diretório válido.")
            time.sleep(1.5)
            continue
        
        limpar_tela()
        # Chama a função correta baseada na escolha do usuário
        if escolha == '1':
            organizar_por_categoria(diretorio_alvo)
        elif escolha == '2':
            organizar_por_extensao(diretorio_alvo)
        elif escolha == '3':
            organizar_por_data(diretorio_alvo)
    else:
        print("ERRO: Opção inválida. Por favor, escolha 1, 2, 3 ou 4.\n")
        time.sleep(1.5)