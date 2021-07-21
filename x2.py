import info
import matplotlib.pyplot as plt

#X2.Peso dos atletas de <Género> a cada ano.

def pegar_dados_para_plotagem():
    genero = info.escolher_genero()

    anos = sorted(list(set([ano for (ano,tipo) in info.olimpiadas])))

    pesos = list(set([
        (int(line['id']), float(line['weight']), line['year'])
        for line in info.athletes
        if line['sex'] == genero
        and line['weight'] != 'NA' ]))

    dados = [ [peso for (_id, peso, ano_registrado) in pesos if ano_registrado == ano ] for ano in anos]

    return dados, anos, {'M': 'Masculino', 'F': 'Feminino'}[genero]

def plotar(dados,anos, genero):
    r = range(1, len(dados)+1)

    plt.boxplot(dados)
    plt.xticks(r, anos, rotation = 70)
    plt.title('Basic Plot')

    plt.show()
    plt.clf()

def main():
    plotar(*pegar_dados_para_plotagem())
