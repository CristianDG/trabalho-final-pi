import info

#B12. Altura média dos atletas para um grupo de <Esportes> na olimpíada de <Ano> de <Tipo de Olimpíada>, separados por sexo.

def pegar_dados_para_plotagem():
    tipo_olimpiada = info.escolher_tipo_olimpiada()
    ano = info.escolher_ano(tipo_olimpiada)
    esportes = info.escolher_esportes(tipo_olimpiada)

    alturas_medias_por_esporte = []
    for esporte in esportes:
        alturas = list(info.alturas_partecipantes(esporte, tipo_olimpiada, ano))

        media_alturas = 0
        if len(alturas):
            media_alturas = sum(alturas) / len(alturas)

        alturas_medias_por_esporte.append((esporte, media_alturas))

    return alturas_medias_por_esporte, (ano, tipo_olimpiada)



def main():
    pass

