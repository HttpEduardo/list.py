import os
import datetime

def listar_arquivos(caminho, extensao='.txt'):
    try:
        lista_arquivos = []
        for root, dirs, files in os.walk(caminho):
            for file in files:
                if file.endswith(extensao):
                    lista_arquivos.append(os.path.join(root, file))
        return lista_arquivos
    except Exception as e:
        print("Ocorreu um erro: ", e)

def ordenar_arquivos(lista_arquivos, tipo_ordenacao='alfabetica'):
    try:
        if tipo_ordenacao == 'alfabetica':
            return sorted(lista_arquivos)
        elif tipo_ordenacao == 'criacao':
            return sorted(lista_arquivos, key=lambda x: os.path.getctime(x))
        elif tipo_ordenacao == 'modificacao':
            return sorted(lista_arquivos, key=lambda x: os.path.getmtime(x))
        elif tipo_ordenacao == 'tamanho':
            return sorted(lista_arquivos, key=lambda x: os.path.getsize(x))
        else:
            return lista_arquivos
    except Exception as e:
        print("Ocorreu um erro: ", e)

def log(msg):
    try:
        with open('log.txt', 'a') as arquivo:
            agora = datetime.datetime.now()
            linha = f"{agora}: {msg}"
            arquivo.write(linha + "\n")
    except Exception as e:
        print("Ocorreu um erro: ", e)

def main():
    try:
        source_dir = r"C:\Users\eduar\OneDrive\Área de Trabalho\Vencimento projeto"
        extensao_arquivos = '.txt'
        tipo_ordenacao = 'criacao'
        lista_arquivos = listar_arquivos(source_dir, extensao_arquivos)
        lista_ordenada = ordenar_arquivos(lista_arquivos, tipo_ordenacao)
        print(f"Lista de arquivos {extensao_arquivos} no diretório '{source_dir}':")
        for arquivo in lista_ordenada:
            print(arquivo)
        log(f"Listagem de arquivos {extensao_arquivos} no diretório '{source_dir}', ordenados por '{tipo_ordenacao}'.")
    except Exception as e:
        print("Ocorreu um erro: ", e)
        log(f"Ocorreu um erro: {e}")

if __name__ == '__main__':
    main()
