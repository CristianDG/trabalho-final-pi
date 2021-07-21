import info
import matplotlib.pyplot as plt

#T4. O maior vencedor de <Tipo de Medalha> num mesmo evento.

def main():
    print("Escolha o tipo de medalha:")
    tipo_medalha = info.criar_menu(['Ouro','Prata','Bronze'], only_index = True)

    medal = { 3: 'Bronze', 2: 'Silver', 1: 'Gold' }.get(tipo_medalha, 'Bronze')
