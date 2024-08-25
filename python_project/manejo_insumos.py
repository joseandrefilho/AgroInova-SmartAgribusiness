def carregar_recomendacoes():
    """
    Carrega as recomendações padrão de insumos para cada cultura.
    Os valores são baseados em práticas agrícolas comuns e podem ser ajustados conforme necessário.
    As recomendações incluem quantidades de fertilizantes (N, P, K) e herbicidas.
    """
    return {
        'cafe': {
            'fertilizantes': {
                'N': 180,   # kg/ha (Nitrogênio)
                'P': 120,   # kg/ha (Fósforo - P2O5)
                'K': 150    # kg/ha (Potássio - K2O)
            },
            'herbicida': 3  # L/ha (Herbicida típico como Glifosato)
        },
        'cana-de-acucar': {
            'fertilizantes': {
                'N': 120,   # kg/ha (Nitrogênio)
                'P': 80,    # kg/ha (Fósforo - P2O5)
                'K': 140    # kg/ha (Potássio - K2O)
            },
            'herbicida': 4  # L/ha (Herbicida típico como Ametrina)
        }
    }

def calcular_manejo_insumos(dados_solo, dados_clima, cultura, area, num_linhas, recomendacoes):
    """
    Calcula a quantidade necessária de fertilizantes e herbicidas com base nos dados fornecidos.
    Leva em consideração o tipo de solo, pH, clima, e histórico de cultivo, além das recomendações padrão.
    """
    recomendacao = recomendacoes.get(cultura)
    if not recomendacao:
        raise ValueError("Recomendações não encontradas para a cultura especificada.")

    # Ajustes baseados no tipo de solo
    ajuste_solo = {
        'arenoso': 1.1,
        'argiloso': 0.9,
        'outro': 1.0
    }.get(dados_solo['tipo_solo'], 1.0)

    # Ajustes baseados no pH do solo
    ph = dados_solo['ph']
    if ph < 5.5:
        ajuste_ph = 1.2
    elif 5.5 <= ph <= 6.5:
        ajuste_ph = 1.0
    else:
        ajuste_ph = 0.8

    # Ajustes baseados nas condições climáticas
    clima = dados_clima['previsao']
    if clima == 'chuva':
        ajuste_clima = 0.9
    elif clima == 'nublado':
        ajuste_clima = 1.0
    else:  # sol
        ajuste_clima = 1.1

    # Cálculo das necessidades de fertilizantes
    fertilizantes = {}
    for nutriente, quantidade_base in recomendacao['fertilizantes'].items():
        nivel_atual = dados_solo['nutrientes'].get(nutriente, 0)
        necessidade = quantidade_base - (nivel_atual * 0.1)
        necessidade = max(necessidade, 0)  # Evita valores negativos
        ajuste_total = ajuste_solo * ajuste_ph * ajuste_clima
        quantidade_final = necessidade * ajuste_total * (area / 10000)  # Convertendo área para hectares
        fertilizantes[nutriente] = quantidade_final

    # Cálculo da necessidade de herbicida
    quantidade_base_herbicida = recomendacao['herbicida']
    ajuste_total_herbicida = ajuste_solo * ajuste_clima
    quantidade_herbicida = quantidade_base_herbicida * ajuste_total_herbicida * (area / 10000)

    return {
        'fertilizantes': fertilizantes,
        'herbicida': quantidade_herbicida
    }

def calcular_manejo_insumosOLD(dados_solo, dados_clima, historico_cultivo, cultura, area, num_linhas, recomendacoes):
    """
    Calcula a quantidade necessária de fertilizantes e herbicidas com base nos dados fornecidos.
    Leva em consideração o tipo de solo, pH, clima, e histórico de cultivo, além das recomendações padrão.
    """
    recomendacao = recomendacoes.get(cultura)
    if not recomendacao:
        raise ValueError("Recomendações não encontradas para a cultura especificada.")

    # Ajustes baseados no tipo de solo
    ajuste_solo = {
        'arenoso': 1.1,
        'argiloso': 0.9,
        'outro': 1.0
    }.get(dados_solo['tipo_solo'], 1.0)

    # Ajustes baseados no pH do solo
    ph = dados_solo['ph']
    if ph < 5.5:
        ajuste_ph = 1.2
    elif 5.5 <= ph <= 6.5:
        ajuste_ph = 1.0
    else:
        ajuste_ph = 0.8

    # Ajustes baseados nas condições climáticas
    clima = dados_clima['previsao']
    if clima == 'chuva':
        ajuste_clima = 0.9
    elif clima == 'nublado':
        ajuste_clima = 1.0
    else:  # sol
        ajuste_clima = 1.1

    # Ajustes baseados no histórico de cultivo
    rotacao = historico_cultivo['rotacao']
    ajuste_rotacao = 0.95 if rotacao else 1.05

    # Cálculo das necessidades de fertilizantes
    fertilizantes = {}
    for nutriente, quantidade_base in recomendacao['fertilizantes'].items():
        nivel_atual = dados_solo['nutrientes'].get(nutriente, 0)
        necessidade = quantidade_base - (nivel_atual * 0.1)
        necessidade = max(necessidade, 0)  # Evita valores negativos
        ajuste_total = ajuste_solo * ajuste_ph * ajuste_clima * ajuste_rotacao
        quantidade_final = necessidade * ajuste_total * (area / 10000)  # Convertendo área para hectares
        fertilizantes[nutriente] = quantidade_final

    # Cálculo da necessidade de herbicida
    quantidade_base_herbicida = recomendacao['herbicida']
    ajuste_total_herbicida = ajuste_solo * ajuste_clima
    quantidade_herbicida = quantidade_base_herbicida * ajuste_total_herbicida * (area / 10000)

    return {
        'fertilizantes': fertilizantes,
        'herbicida': quantidade_herbicida
    }
