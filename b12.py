import info

#B12. Altura média dos atletas para um grupo de <Esportes> na olimpíada de <Ano> de <Tipo de Olimpíada>, separados por sexo.

def calcular_media(arr):
    media = 0
    if len(arr):
        media = sum(arr) / len(arr)
    return media

def pegar_dados_para_plotagem():
    tipo_olimpiada = info.escolher_tipo_olimpiada()
    ano = info.escolher_ano(tipo_olimpiada)
    esportes = info.escolher_esportes(tipo_olimpiada)

    altura_homens = []
    altura_mulheres = []
    for esporte in esportes:
        alturas_homens, alturas_mulheres = info.alturas_participantes(esporte, tipo_olimpiada, ano)

        media_homens = calcular_media(alturas_homens)
        media_mulheres = calcular_media(alturas_mulheres)

        altura_homens.append(media_homens)
        altura_mulheres.append(media_mulheres)
    

    return esportes, altura_homens, altura_mulheres, (ano, tipo_olimpiada)

def plotarGrafico (alturas_medias_por_esporte, grupo, ano):

    grupos = []
    alturas_homens = []
    alturas_mulheres = []


   x = np.arange(len(grupos))  # local dos labels
   width = 0.35  # espaçamento entre as barras

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, alturas_homens, width, label='Homens')
    rects2 = ax.bar(x + width / 2, alturas_mulheres, width, label='Mulheres')

    # Títulos etc
    ax.set_ylabel('Altura em cm')
    ax.set_title('Altura média dos atletas por grupo e gênero')
    ax.set_xticks(x)
    ax.set_xticklabels(grupos)
    ax.legend()

    ax.bar_label(rects1, padding=3)
    ax.bar_label(rects2, padding=3)

    fig.tight_layout()

    plt.show()
    plt.clf()

def main():
    pass

