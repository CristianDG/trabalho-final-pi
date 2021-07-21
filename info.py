import csv

athletes_titles , *athletes = list(csv.DictReader(
    open('./csv_files/athlete_events.csv', 'r'),
    ['id', 'name', 'sex', 'age',
        'height', 'weight', 'team',
        'noc', 'games', 'year', 'season',
        'city', 'sport', 'event', 'medal']))

noc_regions_titles, *noc_regions = list(csv.reader(open('./csv_files/noc_regions.csv', 'r')))

countries_continents_titles, *countries_continents = list(csv.reader(open('./csv_files/countries-continents.csv', 'r')))

continentes = sorted(list(set([line[0] for line in countries_continents])))
olimpiadas = sorted(list(set([(line['year'], line['season']) for line in athletes])))

def esportes_por_tipo(tipo_olimpiada):
    return sorted(list(set([
        line['sport']
        for line in athletes
        if line['season'] == tipo_olimpiada])))

def criar_menu(arr,prompt = 'Selecione um numero: ', error='Numero inválido!',only_index = False):
    def get_index(had_error):
        template = "{}) {}"
        for i, item in enumerate(arr):
            if type(item) == list:
                print(template.format(i+1," ".join(item)))
            else:
                print(template.format(i+1,item))
        print()

        if had_error:
            print(error)
        index = int(input(prompt)) - 1
        return index

    index = get_index(False)

    while index < 0 or index >= len(arr):
        index = get_index(True)

    if only_index:
        return index

    return arr[index]

def escolher_noc():

    # selecionar o continente
    continente_escolhido = criar_menu(continentes, prompt = 'Selecione o numero do continente: ')
    paises_continente = [line[1] for line in countries_continents if line[0] == continente_escolhido]

    # selecionar o pais
    nome_pais = criar_menu(paises_continente, prompt = 'Selecione o numero do pais: ')
    pais = { 'Russian Federation': 'Russia' }.get(nome_pais,nome_pais)

    # pegar o noc
    # por causa dos paises US e CZ tive que adicionar esse passo
    noc_escolhido = {'US': 'USA', 'CZ':'CZE'}.get(pais, '')

    if not noc_escolhido:
        nocs = []
        for noc, region, _ in noc_regions:
            if region == pais:
                nocs.append(noc)

        if len(nocs) > 1:
            noc_escolhido = criar_menu(nocs, prompt = 'Escolha o numero do noc: ')
        else:
            noc_escolhido = nocs[0]

    return noc_escolhido, pais

def escolher_tipo_olimpiada():

    num_olimpiada = criar_menu(
            ['Verão', 'Inverno'],
            prompt = "Selecione o tipo de olimpíada: ",
            only_index = True)

    tipo_olimpiada = ["Summer", "Winter"][num_olimpiada]

    return tipo_olimpiada

def alturas_participantes(esporte,tipo_olimpiada, ano):

    alturas_homem = set()
    alturas_mulher = set()

    for line in athletes:
        if line['season'] == tipo_olimpiada and line['sport'] == esporte and line['year'] == ano and line['height'] != 'NA':
            altura = (line['id'],int(line['height']))

            if line['sex'] == 'M':
                alturas_homem.add(altura)
            elif line['sex'] == 'F':
                alturas_mulher.add(altura)

    return list(alturas_homem), list(alturas_mulher)

def escolher_ano(tipo_olimpiada):
    return criar_menu(
            [item[0] for item in olimpiadas if tipo_olimpiada == item[1]],
            prompt = 'Escolha o ano da olimpíada: ')

def escolher_esportes(tipo_olimpiada):
    esportes = []
    while True:
        esporte = criar_menu(
                ['Sair'] + esportes_por_tipo(tipo_olimpiada),
                prompt = 'Escolha um esporte (ou 1 para sair): ')

        if esporte == 'Sair':
            return esportes

        esportes.append(esporte)

def escolher_medalha():
    tipo_medalha = criar_menu(
            ['Ouro','Prata','Bronze'],
            prompt = 'Escolha o tipo da medalha: ',
            only_index = True)
    return ['Bronze', 'Silver', 'Gold'][tipo_medalha]


def medalhas_partecipantes(ano, tipo_olimpiada):
    return [(line['name'], line['medal'])
            for line in athletes
            if line['year'] == ano
            and line['season'] == tipo_olimpiada]

def escolher_genero():
    num_genero = criar_menu(['Masculino', 'Feminino'], prompt = "Escolha um genero: ", only_index = True)
    return ['M','F'][num_genero]
