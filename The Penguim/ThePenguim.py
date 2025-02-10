import os
import shutil

# Nome do arquivo de imagem original
nome_imagem_original = "ThePenguim.png"

# Pasta onde o script Python está sendo executado
pasta_script = os.getcwd()

# Caminho completo para a imagem original
caminho_imagem_original = os.path.join(pasta_script, nome_imagem_original)

# Pasta de destino onde as cópias serão salvas
nome_pasta_destino = "thePenguim"
caminho_pasta_destino = os.path.join(pasta_script, nome_pasta_destino)

# Verificar se a imagem original existe
if not os.path.exists(caminho_imagem_original):
    print(f"Erro: A imagem '{nome_imagem_original}' não foi encontrada na pasta do script.")
    exit()

# Criar a pasta de destino se ela não existir
if not os.path.exists(caminho_pasta_destino):
    os.makedirs(caminho_pasta_destino)
    print(f"Pasta '{nome_pasta_destino}' criada com sucesso.")
else:
    print(f"Pasta '{nome_pasta_destino}' já existe. As cópias serão salvas nela.")

# Número de cópias que você quer criar
numero_de_copias = 5000

# Loop para copiar a imagem mil vezes
for i in range(numero_de_copias):
    # Criar um novo nome para cada cópia para evitar conflitos
    nome_copia = f"ThePenguim_copia_{i+1}.png"
    caminho_copia = os.path.join(caminho_pasta_destino, nome_copia)

    # Copiar a imagem original para o novo caminho
    shutil.copy2(caminho_imagem_original, caminho_copia) 