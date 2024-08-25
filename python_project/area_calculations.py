import math

def calcular_area_hexagono(lado):
    """
    Calcula a área de um hexágono regular dado o comprimento do lado.
    Fórmula: (3 * sqrt(3) * lado²) / 2
    A escolha de um hexágono é comum em cultivos como o café, onde a otimização do espaço é importante.
    """
    area = (3 * math.sqrt(3) * (lado ** 2)) / 2
    return area

def calcular_area_retangulo(comprimento, largura):
    """
    Calcula a área de um retângulo dado o comprimento e a largura.
    Fórmula: comprimento * largura
    Retângulos são frequentemente utilizados em cultivos como cana-de-açúcar, facilitando a colheita mecanizada.
    """
    area = comprimento * largura
    return area
