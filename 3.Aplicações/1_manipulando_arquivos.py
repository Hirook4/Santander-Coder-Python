print("Arquivos em Python")
# Podemos criar ou abrir arquivos já existentes utilizando a função open, ela possui 2 argumentos, o caminho do arquivo e o modo de operação
# Se alteramos um arquivo e não fecha-lo as alterações não serão salvas e outros programas podem ter problemas ao acessá-lo

# Abrir ou Criar um Arquivo
arquivo = open("3.Aplicações/arquivo.txt", "w")
# A linha de comando acima abre (ou cria, caso nao exista) um arquivo chamado "arquivo.txt" para escrita ("w" de write) e guarda na variável "arquivo" as informações para manipulá-lo

# Manupulando os Dados do Arquivo
arquivo.write("Linha 1 ")
arquivo.write("Linha 2 ")
arquivo.write("Linha 3")

# Fechando Arquivo
# Importante para garantir a integridade dos novos dados, as modificações são salvas somente ao fechar o arquivo
arquivo.close()

ler = open("3.Aplicações/arquivo.txt", "r")
print(ler.read())
arquivo.close()

print("\nComando With")
# Garante que após a finalização do bloco, o arquivo será fechado

with open("3.Aplicações/arquivo.txt", "w") as arquivolido:
    arquivolido.write("Linha 1 ")
    arquivolido.write("Linha 2 ")
    arquivolido.write("Linha 3 ")
    arquivolido.write("Linha 4 ")

with open("3.Aplicações/arquivo.txt", "r") as arquivolido:
    dados = arquivolido.read()
    print(dados)

# É possível ler o arquivo linha a linha, como no exemplo
with open("3.Aplicações/arquivo.txt", "r") as arquivolido:
    linha = arquivolido.readline()
    while linha != "":
        print(linha, end="")
        linha = arquivolido.readline()

# Ou
with open("3.Aplicações/arquivo.txt", "r") as arquivolido:
    for linha in arquivolido:
        print(linha, end="")

# O mesmo pode ser feito para escrever no arquivo
# No comando as linhas do arquivo "arquivo.txt" são copiadas e salvas no arquivo "copia_arquivo.txt"
with open("3.Aplicações/arquivo.txt", "r") as arquivolido:
    with open("3.Aplicações/copia_arquivo.txt", "w") as arquivoteste:
        for linha in arquivolido:
            arquivoteste.write(linha)
