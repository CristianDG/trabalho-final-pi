import csv

athletes_titles , *athletes = list(csv.DictReader(open('./csv_files/athlete_events.csv', 'r'),
    ['id', 'name', 'sex', 'age',
    'height', 'weight', 'team',
    'noc', 'games', 'year', 'season',
    'city', 'sport', 'event', 'medal']))

noc_regions_titles, *noc_regions = list(csv.reader(open('./csv_files/noc_regions.csv', 'r')))

countries_continents_titles, *countries_continents = list(csv.reader(open('./csv_files/countries-continents.csv', 'r')))

continentes = sorted(list(set([line[0] for line in countries_continents])))

def criar_menu(arr):
    for i, item in enumerate(arr):
        print("{}) {}".format(i,item))
    print()

def escolher_noc():

    # selecionar o continente
    criar_menu(continentes)
    
    num_continentes = int(input('Selecione o numero do continente: ')) - 1
    continente_escolhido = continentes[num_continentes]

    paises_continente = list(filter(lambda line: line[0] == continente_escolhido,
        countries_continents))

    # selecionar o pais
    criar_menu(paises_continente)

    num_pais = int(input('Selecione o numero do pais: ')) - 1
    pais = paises_continente[num_pais][1]

    # pegar o noc
    # por causa dos paises US e CZ tive que adicionar esse passo
    noc_escolhido = {'US': 'USA', 'CZ':'CZE'}.get(pais, '')
    for noc, region, _ in noc_regions:
        if region == pais:
            
            noc_escolhido = noc
            break

    return noc_escolhido, pais

def selecionar_tipo_olimpiada():

    criar_menu(['Verão', 'Inverno'])

    num_escolhido = int(input("Selecione o tipo de olimpiada: "))
    tipo_olimpiada = {1: "Summer", 2: "Winter"}[num_escolhido]
    
    return tipo_olimpiada
