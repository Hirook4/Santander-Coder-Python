import requests as r
import datetime as dt
import csv

# URL da API que sera usada
url = "https://api.covid19api.com/dayone/country/brazil"
resposta = r.get(url)

# Verificando se a requisição teve sucesso
print(resposta.status_code)

raw_data = resposta.json()

# Variavel que ira armazenar apenas os dados que serão usados
final_data = []
for obs in raw_data:
    final_data.append(
        [obs["Confirmed"], obs["Deaths"], obs["Recovered"], obs["Active"], obs["Date"]]
    )

# Header do CSV
final_data.insert(0, ["Confirmados", "Mortos", "Recuperados", "Ativos", "Data"])

CONFIRMADOS = 0
MORTOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4

# Deixando a data no formado correto
for i in range(1, len(final_data)):
    final_data[i][DATA] = final_data[i][DATA][:10]  # Data com no maximo 10 caracteres

# Guardando dados para uso futuro
with open("4.Projeto/brazil_covid.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(final_data)

# Transformando strings em data
for i in range(1, len(final_data)):
    final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], "%Y-%m-%d")

print(final_data)
