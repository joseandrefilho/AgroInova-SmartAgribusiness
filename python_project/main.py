# /python/main.py

import pandas as pd
from area_calculations import calcular_area_hexagono, calcular_area_retangulo
from manejo_insumos import calcular_manejo_insumos, carregar_recomendacoes

# Função para exibir o menu
def exibir_menu():
    print("\nMenu de Opções:")
    print("  1. Gestão de Plantio e Insumos")
    print("  0. Sair")

import os
import pandas as pd

# Função para salvar dados em Parquet, adicionando ao arquivo existente
def salvar_dados_parquet(dados, nome_arquivo='data/processed/dados_agricultura.parquet'):
    # Converta os novos dados em um DataFrame
    df_novo = pd.DataFrame(dados)
    
    # Verifica se o arquivo já existe
    if os.path.exists(nome_arquivo):
        # Se o arquivo existir, carregue os dados existentes
        df_existente = pd.read_parquet(nome_arquivo)
        # Concatene os novos dados com os dados existentes
        df_final = pd.concat([df_existente, df_novo], ignore_index=True)
    else:
        # Se o arquivo não existir, use apenas os novos dados
        df_final = df_novo
    
    # Salve o DataFrame resultante no arquivo Parquet
    df_final.to_parquet(nome_arquivo)


# Função principal
def main():
    dados = []
    recomendacoes = carregar_recomendacoes()  # Carregar as recomendações do arquivo externo

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            tipo_plantacao = input("\nQual tipo de plantação você deseja gerenciar?\n  1. Café\n  2. Cana-de-açúcar\nEscolha uma opção: ").lower()
            if tipo_plantacao == '1':
                cultura= 'cafe'
                lado = float(input("\nInforme o lado do hexágono em metros: "))
                area = calcular_area_hexagono(lado)
            elif tipo_plantacao == '2':
                cultura = 'cana-de-acucar'
                comprimento = float(input("\nInforme o comprimento do retângulo em metros: "))
                largura = float(input("Informe a largura do retângulo em metros: "))
                area = calcular_area_retangulo(comprimento, largura)
            else:
                print("Cultura não reconhecida.")
                continue

            ph_solo = float(input("Informe o pH do solo: "))
            clima_previsaoOpcao = input("Informe a previsão do clima\n  1. Sol\n  2. Chuva\nEscolha uma opção: ").lower()

            if clima_previsaoOpcao in ['1', 'sol']:
                clima_previsao = 'sol'
            elif clima_previsaoOpcao in ['2', 'chuva']:
                clima_previsao = 'chuva'
            else:
                print("Previsão do clima não reconhecida.")
                continue

            # Calcular a quantidade de insumos necessários com base nas recomendações
            quantidade_fertilizante, quantidade_herbicida = calcular_manejo_insumos(cultura, area, ph_solo, clima_previsao, recomendacoes)

            # Adicionar dados ao vetor e salvar automaticamente
            dados.append({
                'cultura': cultura,
                'area': area,
                'ph_solo': ph_solo,
                'clima_previsao': clima_previsao,
                'quantidade_fertilizante': quantidade_fertilizante,
                'quantidade_herbicida': quantidade_herbicida
            })
            salvar_dados_parquet(dados)  # Salvar automaticamente após cada inserção

            # Exibir o item recém-adicionado na tela
            entrada = dados[-1]

            print("\n***********************************************************")
            print("Informações de Plantio e Insumos:")
            print("***********************************************************")
            print(f"Cultura: {entrada['cultura']}")
            print(f"Área: {entrada['area']:.2f} metros quadrados")
            print(f"pH do solo: {entrada['ph_solo']}")
            print(f"Previsão do clima: {entrada['clima_previsao']}")
            print(f"Quantidade de fertilizante necessária: {entrada['quantidade_fertilizante']:.2f} litros")
            print(f"Quantidade de herbicida necessária: {entrada['quantidade_herbicida']:.2f} litros")
            print("***********************************************************")


        elif opcao == '0':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
