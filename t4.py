import info
import matplotlib.pyplot as plt

#T4. O maior vencedor de <Tipo de Medalha> num mesmo evento.

def pegar_dados_para_plotagem():
    medalha = info.escolher_medalha()
    tipo_olimpiada = info.escolher_tipo_olimpiada()
    ano = info.escolher_ano(tipo_olimpiada)

    contador_medalhas = {}
    for nome, medalha_ganha in info.medalhas_partecipantes(ano,tipo_olimpiada):
        if medalha == medalha_ganha:
            contador_medalhas[nome] = contador_medalhas.get(nome,0) + 1

    maior_quantidade = max(contador_medalhas.values())
    maiores_vencedores = [nome for (nome, qtd_medalhas) in contador_medalhas.items() if qtd_medalhas == maior_quantidade]
    return maiores_vencedores, (maior_quantidade, medalha, ano, tipo_olimpiada)


def main():
    maiores_vencedores, argumentos_titulo = pegar_dados_para_plotagem()
    qtd, medalha, ano, tipo_olimpiada = argumentos_titulo

    final = 'medalha conquistada' if qtd == 1 else 'medalhas conquistadas'

    if len(maiores_vencedores) == 1:
        vencedor = maiores_vencedores[0]
        print('O maior vencedor de medalhas de {} das olimpíadas de {} de {} foi {} com {} {}'.format(medalha, tipo_olimpiada, ano, vencedor, qtd, final))
    else:
        vencedores = ', '.join(maiores_vencedores)
        print('Os maiores vencedores de medalhas de {} das olimpíadas de {} de {} foram {} com {} {}'.format(medalha,tipo_olimpiada, ano, vencedores, qtd, final))


