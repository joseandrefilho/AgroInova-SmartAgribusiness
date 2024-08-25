# /python/manejo_insumos.py

import json
import os

def carregar_recomendacoes(caminho_arquivo='data/recomendacoes.json'):
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"O arquivo {caminho_arquivo} não foi encontrado.")
    
    with open(caminho_arquivo, 'r') as file:
        # Supondo que o arquivo seja JSON, você pode usar json.load para carregar o conteúdo
        import json
        recomendacoes = json.load(file)
    
    return recomendacoes

def calcular_manejo_insumos(cultura, area, ph_solo, clima_previsao, recomendacoes):
    insumos = recomendacoes[cultura]
    quantidade_fertilizante = area * insumos['fertilizante']
    quantidade_herbicida = area * insumos['herbicida']

    # Ajuste com base no pH do solo
    if ph_solo < 6.0:
        quantidade_fertilizante *= insumos['ajuste_ph']

    # Ajuste com base na previsão do clima
    if clima_previsao == 'chuva':
        quantidade_herbicida *= 0.8  # Reduzir aplicação se houver previsão de chuva

    return quantidade_fertilizante, quantidade_herbicida
