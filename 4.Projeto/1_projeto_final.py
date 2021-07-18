import requests as r
import datetime as dt
import csv
from PIL import Image
from IPython.display import display

# URL da API que sera usada
url = "https://api.covid19api.com/dayone/country/brazil"
resposta = r.get(url)

# Verificando se a requisição teve sucesso
print(resposta.status_code)

raw_data = resposta.json()

# Vendo raw_data[0]
print(raw_data[0])

# Variavel que ira armazenar apenas os dados que serão usados
final_data = []
for obs in raw_data:
    final_data.append(
        [obs["Confirmed"], obs["Deaths"], obs["Recovered"], obs["Active"], obs["Date"]]
    )

# Header do CSV
final_data.insert(0, ["confirmados", "mortos", "recuperados", "ativos", "data"])

# Checando dados finais
# print(final_data)

# "Constantes" para referenciar cada posição da lista
CONFIRMADOS = 0
MORTOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4

# Deixando a data no formado correto
for i in range(1, len(final_data)):
    final_data[i][DATA] = final_data[i][DATA][:10]  # Data com no maximo 10 caracteres

# Guardando dados em CSV
with open("4.Projeto/brazil_covid.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(final_data)

# Transformando strings em data
for i in range(1, len(final_data)):
    final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], "%Y-%m-%d")

# Imprime todos os dados
# print(final_data)

# Parte II

# Função que sera responsavel pela chave que constroi os dados
def get_datasets(y, labels):
    if type(y[0]) == list:
        datasets = []
        for i in range(len(y)):
            datasets.append(
                {
                    "label": labels[i],
                    "data": y[i],
                }
            )
            return datasets
        else:
            return [
                {
                    "label": labels[0],
                    "data": y,
                }
            ]


# Função que cria o titulo do grafico
def set_title(title=""):
    if title != "":
        display = "true"
    else:
        display = "false"
    return {
        "title": title,
        "display": display,
    }


# Função que cria o dicionario que representa o grafico
def create_chart(x, y, labels, kind="bar", title=""):
    datasets = get_datasets(y, labels)
    options = set_title(title)
    chart = {
        "type": kind,
        "data": {
            "labels": x,
            "datasets": datasets,
        },
        "options": options,
    }
    return chart


# Função que fara a requisição na API, essa função ira retornar um arquivo de imagem em binario
def get_api_chart(chart):
    url_base = "https://quickchart.io/chart"
    resp = r.get(f"{url_base}?c={str(chart)}")
    return resp.content


# Função responsavel por salvar a imagem
def save_image(path, content):
    with open(path, "wb") as image:
        image.write(content)


# Função que ira mostrar a imagem
def display_image(path):
    img_pil = Image.open(path)
    display(img_pil)


# Para melhor entendimento serão mostrados os dados de 10 em 10 dias
y_data_1 = []
for obs in final_data[1::10]:
    y_data_1.append(obs[CONFIRMADOS])

y_data_2 = []
for obs in final_data[1::10]:
    y_data_2.append(obs[RECUPERADOS])

labels = ["Confirmados", "Recuperados"]

x = []
for obs in final_data[1::10]:
    x.append(obs[DATA].strftime("%d/%m/%Y"))

chart = create_chart(
    x, [y_data_1, y_data_2], labels, title="Grafico Confirmados vs Recuperados"
)

chart_content = get_api_chart(chart)
save_image("4.Projeto\meu_primeiro_grafico.png", chart_content)
display_image("4.Projeto\meu_primeiro_grafico.png")
