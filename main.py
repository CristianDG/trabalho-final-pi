import l3
import t4

#L3. Desempenho do <País> nas últimas <X> olimpíadas de <Tipo de Olimpíada>, três linhas, uma por cada tipo de medalha.

#B12. Altura média dos atletas para um grupo de <Esportes> na olimpíada de <Ano> de <Tipo de Olimpíada>, separados por sexo.

#X2.Peso dos atletas de <Género> a cada ano.

#T4. O maior vencedor de <Tipo de Medalha> num mesmo evento.


def not_implemented():
    print("OPÇÃO NÃO IMPLEMENTADA")

# TODO: falta 1 grafico
def main():
    print("""
--------------------------- MENU ---------------------------

1) Desempenho do <País> nas últimas <X> olimpíadas de <Tipo de Olimpíada>, três linhas, uma por cada tipo de medalha.
2) Altura média dos atletas para um grupo de <Esportes> na olimpíada de <Ano> de <Tipo de Olimpíada>, separados por sexo.
3) Peso dos atletas de <Género> a cada ano.
4) O maior vencedor de <Tipo de Medalha> num mesmo evento.
5) Um grafico ainda pra escolher

""")


    num_grafico = int(input('Escolha uma das opções: '))

    {
        1: l3.main,
        2: not_implemented,
        3: not_implemented,
        4: t4.main,
        5: not_implemented
    }.get(num_grafico)()

if __name__ == '__main__':
    main()
