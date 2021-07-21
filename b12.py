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

    alturas_medias_por_esporte = []
    for esporte in esportes:
        alturas_homens, alturas_mulheres = info.alturas_partecipantes(esporte, tipo_olimpiada, ano)

        media_homens = calcular_media(alturas_homens)
        media_mulheres = calcular_media(alturas_mulheres)

        alturas_medias_por_esporte.append((esporte, media_homens, media_mulheres))

    return alturas_medias_por_esporte, (ano, tipo_olimpiada)



def main():
    pass

