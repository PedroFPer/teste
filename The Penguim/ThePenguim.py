import os
import shutil


nome_imagem_original = "ThePenguim.png"

pasta_script = os.getcwd()


caminho_imagem_original = os.path.join(pasta_script, nome_imagem_original)


nome_pasta_destino = "thePenguim"
caminho_pasta_destino = os.path.join(pasta_script, nome_pasta_destino)


if not os.path.exists(caminho_imagem_original):
    print(f"Erro: A imagem '{nome_imagem_original}' não foi encontrada na pasta do script.")
    exit()


if not os.path.exists(caminho_pasta_destino):
    os.makedirs(caminho_pasta_destino)
    print(f"Pasta '{nome_pasta_destino}' criada com sucesso.")
else:
    print(f"Pasta '{nome_pasta_destino}' já existe. As cópias serão salvas nela.")


numero_de_copias = 1000


for i in range(numero_de_copias):
    
    nome_copia = f"ThePenguim_copia_{i+1}.png"
    caminho_copia = os.path.join(caminho_pasta_destino, nome_copia)

    
    shutil.copy2(caminho_imagem_original, caminho_copia) 