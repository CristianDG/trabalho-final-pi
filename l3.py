import info
import matplotlib.pyplot as plt

#L3. Desempenho do <País> nas últimas <X> olimpíadas de <Tipo de Olimpíada>, três linhas, uma por cada tipo de medalha.


def pegar_dados_para_plotagem():
    noc_escolhido, pais_escolhido = info.escolher_noc()
    tipo_olimpiada = info.selecionar_tipo_olimpiada()

    games = sorted([game for game in set(line['games'] for line in info.athletes) if tipo_olimpiada in game], key= lambda item: int(item[:4]), reverse=True)

    num_olimpiadas = int(input("Selecione a quantidade de olimpiadas: min. {} max. {}: ".format(1, len(games))))

    jogos_selecionados = games[:num_olimpiadas]
    data = dict([(game, {'Bronze':0, 'Silver':0, 'Gold':0, 'NA':0}) for game in jogos_selecionados])

    # coletando os dados
    for athlete in info.athletes:
        olimpiada = athlete['games']
        if olimpiada in jogos_selecionados and athlete['noc'] == noc_escolhido:
            data[olimpiada][athlete['medal']] += 1
    
    return data, (pais_escolhido, num_olimpiadas, tipo_olimpiada)

def plotar_L3(data, title):
    # agora é só plotar
    fig, ax = plt.subplots()
    r = range(len(data))
    ax.plot(r,
            [year['Gold']   for year in data.values()][::-1],
            color = '#ffd700',
            label = 'Medalhas de ouro')

    ax.plot(r,
            [year['Silver'] for year in data.values()][::-1],
            color = '#c0c0c0',
            label = 'Medalhas de prata')

    ax.plot(r,
            [year['Bronze'] for year in data.values()][::-1],
            color = '#b8860b',
            label = 'Medalhas de bronze')

    ax.set_xticks(r)
    ax.set_xticklabels([year[:4] for year in data][::-1])

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
            rotation_mode="anchor")

    plt.title('Desempenho do {} nas últimas {} olimpíadas de {}, três linhas, uma por cada tipo de medalha'.format(*title))

    plt.legend()

    plt.show()
    plt.clf()

def main():
    plotar_L3(pegar_dados_para_plotagem())