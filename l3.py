import info
import matplotlib.pyplot as plt

#L3. Desempenho do <País> nas últimas <X> olimpíadas de <Tipo de Olimpíada>, três linhas, uma por cada tipo de medalha.


def pegar_dados_para_plotagem():
    noc_escolhido, pais_escolhido = info.escolher_noc()
    tipo_olimpiada = info.escolher_tipo_olimpiada()

    games = sorted([game for game in set(line['games'] for line in info.athletes if line['noc'] == noc_escolhido) if tipo_olimpiada in game], key= lambda item: int(item[:4]), reverse=True)

    # TODO: adicionar tratamento de erro
    num_olimpiadas = int(input("Selecione a quantidade de olimpiadas: min. {} max. {}: ".format(1, len(games))))

    jogos_selecionados = games[:num_olimpiadas]
    data = dict([(game, {'Bronze':0, 'Silver':0, 'Gold':0, 'NA':0}) for game in jogos_selecionados])

    # coletando os dados
    for athlete in info.athletes:
        olimpiada = athlete['games']
        if olimpiada in jogos_selecionados and athlete['noc'] == noc_escolhido:
            data[olimpiada][athlete['medal']] += 1

    return data, (pais_escolhido, num_olimpiadas, {'Summer' : 'Verão', 'Winter' : 'Inverno'}[tipo_olimpiada])

def plotar_L3(data, title):
    # agora é só plotar
    fig, ax = plt.subplots()
    r = range(len(data))
    ax.plot(r,
            [year['Gold']   for year in data.values()][::-1],
            color = 'gold',
            label = 'Medalhas de ouro')

    ax.plot(r,
            [year['Silver'] for year in data.values()][::-1],
            color = 'silver',
            label = 'Medalhas de prata')

    ax.plot(r,
            [year['Bronze'] for year in data.values()][::-1],
            color = 'saddlebrown',
            label = 'Medalhas de bronze')

    plt.xticks(r, [year[:4] for year in data][::-1])

    plt.title('Desempenho do país "{}" nas últimas {} olimpíadas de {}'.format(*title))

    plt.legend()

    plt.savefig('png/l3.png')
    plt.clf()

def main():
    data, title = pegar_dados_para_plotagem()
    plotar_L3(data, title)
