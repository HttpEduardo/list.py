# list.py

Esse script é um programa em Python que lista arquivos em um determinado diretório e os ordena de acordo com um critério escolhido pelo usuário. Ele contém quatro funções principais:


listar_arquivos(caminho, extensao='.txt'): recebe o caminho do diretório e uma extensão de arquivo opcional, e retorna uma lista com os caminhos completos de todos os arquivos com a extensão especificada no diretório e seus subdiretórios.



ordenar_arquivos(lista_arquivos, tipo_ordenacao='alfabetica'): recebe uma lista de caminhos de arquivos e um tipo de ordenação, e retorna a lista ordenada de acordo com o critério escolhido. Os critérios possíveis são: “alfabetica” (ordenação alfabética padrão), “criacao” (ordem de criação dos arquivos), “modificacao” (ordem de modificação dos arquivos) e “tamanho” (ordem de tamanho dos arquivos).



log(msg): recebe uma mensagem e a escreve em um arquivo de log chamado “log.txt”, juntamente com a data e hora atuais.



main(): é a função principal do programa, que configura as variáveis para o diretório de origem, extensão de arquivo e tipo de ordenação, chama as funções listar_arquivos e ordenar_arquivos para obter a lista de arquivos ordenada, e imprime essa lista na tela. Também chama a função log para registrar a operação em um arquivo de log.
