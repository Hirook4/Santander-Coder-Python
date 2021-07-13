# Usamos a biblioteca Requests
import requests

# URL que sera acessado
url = "https://api.exchangerate-api.com/v6/latest"

req = requests.get(url)

# Verificando se o status esta certo (codigo 200)
# print(req.status_code)

# Recupera dados da requisição e o transforma em um dicionario
dados = req.json()

valor_reais = float(input("Informe o Valor em R$\n"))
cotacao = dados["rates"]["BRL"]
print(f"R${(valor_reais)} em dolar vale US$ {(valor_reais / cotacao):.2f}")
