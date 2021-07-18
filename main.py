import l3
import t4
import info

#L3. Desempenho do <País> nas últimas <X> olimpíadas de <Tipo de Olimpíada>, três linhas, uma por cada tipo de medalha.

#B12. Altura média dos atletas para um grupo de <Esportes> na olimpíada de <Ano> de <Tipo de Olimpíada>, separados por sexo.

#X2.Peso dos atletas de <Género> a cada ano.

#T4. O maior vencedor de <Tipo de Medalha> num mesmo evento.


def not_implemented():
    print("OPÇÃO NÃO IMPLEMENTADA")

# TODO: falta 1 grafico
def main():
    graficos = [
            "Desempenho do <País> nas últimas <X> olimpíadas de <Tipo de Olimpíada>, três linhas, uma por cada tipo de medalha.",
            "Altura média dos atletas para um grupo de <Esportes> na olimpíada de <Ano> de <Tipo de Olimpíada>, separados por sexo.",
            "Peso dos atletas de <Género> a cada ano.",
            "O maior vencedor de <Tipo de Medalha> num mesmo evento.",
            "Um grafico ainda pra escolher"
            ]

    print(" --------------------------- MENU --------------------------- ")
    num_grafico = info.criar_menu(graficos, prompt = 'Escolha uma das opções: ', only_index = True)

    [
        l3.main,
        not_implemented,
        not_implemented,
        t4.main,
        not_implemented
    ][num_grafico]()

if __name__ == '__main__':
    main()
