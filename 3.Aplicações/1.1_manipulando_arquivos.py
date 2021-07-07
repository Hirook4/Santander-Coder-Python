arquivolido = open("3.Aplicações/teste.txt", "r")
# A linha acima lê ("r", de read) um arquivo já existente chamado "teste.txt" e guarda na variável "arquivolido" as informações para manipulá-lo

# Carregar os Dados do Arquivo (leitura)
# Função read() retorna o conteúdo do arquivo como uma string
print(arquivolido.read())

# Linha por Linha While
linha = arquivolido.readline()
while linha != "":
    print(linha, end="")
    linha = arquivolido.readline()

# Linha por Linha For
for linha in arquivolido:
    print(linha, end="")

# Fechando Arquivo
# Importante para garantir a integridade dos novos dados, as modificações são salvas somente ao fechar o arquivo
arquivolido.close()
