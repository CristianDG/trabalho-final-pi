import info
import matplotlib.pyplot as plt

#X2.Peso dos atletas de <Género> a cada ano.

def pegar_dados_para_plotagem():
    genero = info.escolher_genero()

    anos = set([ano for (ano,tipo) in info.olimpiadas])

    pesos = list(set([
        (int(line['id']), float(line['weight']), line['year'])
        for line in info.athletes
        if line['sex'] == genero
        and line['weight'] != 'NA' ]))

    dados = [ [peso for (_id, peso, ano_registrado) in pesos if ano_registrado == ano ] for ano in anos]

    return dados, {'M': 'Masculino', 'F': 'Feminino'}[genero]

def main():
    pass
