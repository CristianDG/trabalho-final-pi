import l3
import t4
import b12
import t9
import x2
import info

#L3. Desempenho do <País> nas últimas <X> olimpíadas de <Tipo de Olimpíada>, três linhas, uma por cada tipo de medalha.

#B12. Altura média dos atletas para um grupo de <Esportes> na olimpíada de <Ano> de <Tipo de Olimpíada>, separados por sexo.

#X2.Peso dos atletas de <Género> a cada ano.

#T4. O maior vencedor de <Tipo de Medalha> num mesmo evento.

#T9. Em que anos não houve olimpíadas?

def not_implemented():
    print("OPÇÃO NÃO IMPLEMENTADA")

def main():
    graficos = [
            "Desempenho do <País> nas últimas <X> olimpíadas de <Tipo de Olimpíada>, três linhas, uma por cada tipo de medalha.",
            "Altura média dos atletas para um grupo de <Esportes> na olimpíada de <Ano> de <Tipo de Olimpíada>, separados por sexo.",
            "Peso dos atletas de <Género> a cada ano.",
            "O maior vencedor de <Tipo de Medalha> num mesmo evento.",
            "Em que anos não houve olimpíadas"
            ]

    print(" --------------------------- MENU --------------------------- ")
    num_grafico = info.criar_menu(graficos, prompt = 'Escolha uma das opções: ', only_index = True)

    try:
        [
            l3.main,
            b12.main,
            x2.main,
            t4.main,
            t9.main
        ][num_grafico]()
    except FileNotFoundError:
        print('ERRO: Por favor crie um diretorio png')
    except:
        print('Ocorreu um erro inesperado')


if __name__ == '__main__':
    main()
