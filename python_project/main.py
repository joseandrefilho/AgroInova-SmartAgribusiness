import os
import pandas as pd
from area_calculations import calcular_area_hexagono, calcular_area_retangulo
from manejo_insumos import calcular_manejo_insumos, carregar_recomendacoes

def coletar_dados_solo():
    print("\n=== Coleta de Dados do Solo ===")
    print("Vamos começar coletando informações sobre o solo onde a cultura será plantada.")
    print(
        "O pH do solo indica o quão ácido ou alcalino ele é, o que afeta a disponibilidade de nutrientes para as plantas.\n")

    while True:
        try:
            ph = float(input("Informe o pH do solo (ex: 5.5): "))
            if 0 <= ph <= 14:
                break
            else:
                print("O valor de pH deve estar entre 0 e 14.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido para o pH.")

    print("\nO tipo de solo influencia a retenção de água e nutrientes. Aqui estão algumas opções comuns:")
    print(" - Arenoso: Solo leve com boa drenagem, mas baixa retenção de nutrientes.")
    print(" - Argiloso: Solo pesado, retém bem os nutrientes, mas pode drenar mal.")
    print(" - Outro: Qualquer outro tipo de solo.\n")

    tipo_solo = input("Informe o tipo de solo (arenoso/argiloso/outro): ").strip().lower()
    while tipo_solo not in ['arenoso', 'argiloso', 'outro']:
        print("Tipo de solo inválido.")
        tipo_solo = input("Informe o tipo de solo (arenoso/argiloso/outro): ").strip().lower()

    print("\nAgora, vamos coletar os níveis de nutrientes no solo em miligramas por quilograma (mg/kg):")
    print("Esses nutrientes são fundamentais para o crescimento saudável das plantas:")
    print(" - Nitrogênio (N): Essencial para o crescimento vegetativo e desenvolvimento das folhas.")
    print(" - Fósforo (P): Crucial para o desenvolvimento das raízes e a floração.")
    print(" - Potássio (K): Importante para a resistência das plantas, controle de água, e formação de frutos.\n")

    nutrientes = {}
    for nutriente, descricao in [('N', 'Nitrogênio (N)'), ('P', 'Fósforo (P)'), ('K', 'Potássio (K)')]:
        while True:
            try:
                valor = float(input(f"Informe o nível de {descricao} no solo (mg/kg): "))
                if valor >= 0:
                    nutrientes[nutriente] = valor
                    break
                else:
                    print("O valor não pode ser negativo.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")

    return {
        'ph': ph,
        'tipo_solo': tipo_solo,
        'nutrientes': nutrientes
    }


def coletar_dados_clima():
    print("\n=== Coleta de Dados Climáticos ===")
    print("As condições climáticas influenciam diretamente o manejo das culturas.")
    print(
        "Por exemplo, em climas chuvosos, a aplicação de fertilizantes deve ser ajustada para evitar perdas por lixiviação.\n")

    previsao = input("Informe a previsão do clima (sol/chuva/nublado): ").strip().lower()
    while previsao not in ['sol', 'chuva', 'nublado']:
        print("Previsão do clima inválida.")
        previsao = input("Informe a previsão do clima (sol/chuva/nublado): ").strip().lower()

    while True:
        try:
            temperatura = float(input("Informe a temperatura média (°C): "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido para a temperatura.")

    while True:
        try:
            umidade = float(input("Informe a umidade relativa do ar (%): "))
            if 0 <= umidade <= 100:
                break
            else:
                print("A umidade deve estar entre 0 e 100%.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido para a umidade.")

    return {
        'previsao': previsao,
        'temperatura': temperatura,
        'umidade': umidade
    }


def coletar_historico_cultivo():
    print("\n=== Histórico de Cultivo ===")
    print(
        "O histórico de cultivo ajuda a entender como o solo tem sido utilizado, o que afeta as recomendações de insumos.")
    print(
        "Rotação de culturas, por exemplo, pode melhorar a qualidade do solo e reduzir a necessidade de fertilizantes.\n")

    ultima_cultura = input("Qual foi a última cultura plantada? ").strip().lower()
    rotacao_input = input("Houve rotação de culturas? (sim/não): ").strip().lower()
    while rotacao_input not in ['sim', 'não', 'nao']:
        print("Entrada inválida.")
        rotacao_input = input("Houve rotação de culturas? (sim/não): ").strip().lower()
    rotacao = rotacao_input == 'sim'

    return {
        'ultima_cultura': ultima_cultura,
        'rotacao': rotacao
    }


def salvar_dados_parquet(dados, nome_arquivo='../data/processed/dados_agricultura.parquet'):
    """
    Salva os dados em um arquivo Parquet. Se o arquivo já existir, os dados novos são anexados.
    """
    # Converte os dados em um DataFrame
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

    # Salva o DataFrame resultante no arquivo Parquet
    df_final.to_parquet(nome_arquivo)

    print(f"\nDados salvos com sucesso em '{nome_arquivo}'.\n")


def carregar_dados_parquet(nome_arquivo='../data/processed/dados_agricultura.parquet'):
    """
    Carrega os dados de um arquivo Parquet, se existir.
    """
    if os.path.exists(nome_arquivo):
        df = pd.read_parquet(nome_arquivo)
        return df.to_dict(orient='records')
    else:
        return []

def exibir_menu():
    print("\nBem-vindo ao AgroInova - Sua Ferramenta Completa de Gestão Agrícola!")
    print("\nPor favor, escolha uma das opções abaixo:\n")
    print("1. Adicionar Novo Registro 🌱")
    print("   - Insira novas informações sobre suas culturas, solo e clima.")
    print("2. Visualizar Registros 🌾")
    print("   - Veja um resumo detalhado de todos os registros salvos.")
    print("3. Atualizar Registro Existente ✏️")
    print("   - Atualize os dados de uma cultura existente.")
    print("4. Remover Registro ❌")
    print("   - Exclua registros antigos ou desnecessários.")
    print("0. Sair do AgroInova 🚪")
    print("   - Encerrar o programa.")


def adicionar_registro(dados, recomendacoes):
    print("\n=== Adicionar Novo Registro ===")
    print("Escolha a cultura para a qual deseja calcular a área plantada e o manejo de insumos.\n")
    cultura_input = input("Escolha a cultura (1. Café, 2. Cana-de-açúcar): ").strip()
    while cultura_input not in ['1', '2']:
        print("Opção inválida.")
        cultura_input = input("Escolha a cultura (1. Café, 2. Cana-de-açúcar): ").strip()

    if cultura_input == '1':
        cultura = 'cafe'
        print(
            "\nA cultura do café é frequentemente plantada em áreas com forma hexagonal para maximizar o espaço disponível.")
        while True:
            try:
                lado = float(input("Informe o comprimento do lado do hexágono (em metros): "))
                if lado > 0:
                    area = calcular_area_hexagono(lado)
                    break
                else:
                    print("O valor deve ser maior que zero.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
    else:
        cultura = 'cana-de-acucar'
        print(
            "\nA cana-de-açúcar é tipicamente plantada em fileiras retangulares, o que facilita a colheita mecanizada.")
        while True:
            try:
                comprimento = float(input("Informe o comprimento do retângulo (em metros): "))
                largura = float(input("Informe a largura do retângulo (em metros): "))
                if comprimento > 0 and largura > 0:
                    area = calcular_area_retangulo(comprimento, largura)
                    break
                else:
                    print("Os valores devem ser maiores que zero.")
            except ValueError:
                print("Entrada inválida. Por favor, insira números válidos.")

    print("\nO número de linhas na lavoura influencia diretamente na quantidade de insumos necessários.")
    num_linhas = int(input("Informe o número de linhas na lavoura: "))
    dados_solo = coletar_dados_solo()
    dados_clima = coletar_dados_clima()
    #historico_cultivo = coletar_historico_cultivo()

    insumos_recomendados = calcular_manejo_insumos(
        dados_solo, dados_clima, cultura, area, num_linhas, recomendacoes
    )
    '''
    insumos_recomendados = calcular_manejo_insumos(
        dados_solo, dados_clima, historico_cultivo, cultura, area, num_linhas, recomendacoes
    )
    '''

    registro = {
        'cultura': cultura,
        'area': area,
        'num_linhas': num_linhas,
        'dados_solo': dados_solo,
        'dados_clima': dados_clima,
        #'historico_cultivo': historico_cultivo,
        'insumos_recomendados': insumos_recomendados
    }

    dados.append(registro)
    salvar_dados_parquet(dados)

    print("\n=== Registro Adicionado com Sucesso ===")
    visualizar_registro(registro, len(dados))


def visualizar_todos_registros(dados):
    if not dados:
        print("\nNão há registros para exibir.")
        return
    print(f"\n==== Exibindo {len(dados)} Registros ====")
    for idx, registro in enumerate(dados, start=1):
        visualizar_registro(registro, idx)


def visualizar_registro(registro, indice):
    print(f"\n----- Registro {indice} -----")
    print(f"Cultura: {registro['cultura'].capitalize()}")
    print(f"Área: {registro['area']:.2f} m²")
    print(f"Número de Linhas: {registro['num_linhas']}")
    print("\n--- Dados do Solo ---")
    print(f"pH: {registro['dados_solo']['ph']}")
    print(f"Tipo de Solo: {registro['dados_solo']['tipo_solo'].capitalize()}")
    print(f"Níveis de Nutrientes (mg/kg):")
    for nutriente, valor in registro['dados_solo']['nutrientes'].items():
        print(f"  {nutriente}: {valor}")
    print("\n--- Dados Climáticos ---")
    print(f"Previsão do Clima: {registro['dados_clima']['previsao'].capitalize()}")
    print(f"Temperatura Média: {registro['dados_clima']['temperatura']} °C")
    print(f"Umidade Relativa: {registro['dados_clima']['umidade']}%")
    #print("\n--- Histórico de Cultivo ---")
    #print(f"Última Cultura Plantada: {registro['historico_cultivo']['ultima_cultura'].capitalize()}")
    #print(f"Rotação de Culturas: {'Sim' if registro['historico_cultivo']['rotacao'] else 'Não'}")
    print("\n--- Insumos Recomendados ---")
    print("Fertilizantes (kg):")
    for nutriente, valor in registro['insumos_recomendados']['fertilizantes'].items():
        print(f"  {nutriente}: {valor:.2f} kg")
    print(f"Herbicida: {registro['insumos_recomendados']['herbicida']:.2f} L")
    print("-----------------------------")


def atualizar_registro(dados):
    if not dados:
        print("\nNão há registros para atualizar.")
        return

    try:
        indice = int(input(f"\nInforme o número do registro que deseja atualizar (1 - {len(dados)}): "))
        if 1 <= indice <= len(dados):
            registro_atual = dados[indice - 1]
            print("\n=== Dados Atuais do Registro ===")
            visualizar_registro(registro_atual, indice)

            print("\n=== Atualização de Dados ===")
            opcao = input(
                "Deseja atualizar toda a entrada ou campos específicos? (1. Toda entrada, 2. Campos específicos): ").strip()
            while opcao not in ['1', '2']:
                print("Opção inválida.")
                opcao = input(
                    "Deseja atualizar toda a entrada ou campos específicos? (1. Toda entrada, 2. Campos específicos): ").strip()

            if opcao == '1':
                recomendacoes = carregar_recomendacoes()
                adicionar_registro(dados[:indice - 1] + dados[indice:], recomendacoes)
                print("\nRegistro atualizado com sucesso.")
            else:
                campo = input(
                    "Informe o campo que deseja atualizar (cultura/area/num_linhas/dados_solo/dados_clima/historico_cultivo): ").strip().lower()
                campos_validos = ['cultura', 'area', 'num_linhas', 'dados_solo', 'dados_clima', 'historico_cultivo']
                while campo not in campos_validos:
                    print("Campo inválido.")
                    campo = input("Informe o campo que deseja atualizar: ").strip().lower()

                if campo == 'cultura':
                    cultura_input = input("Escolha a nova cultura (1. Café, 2. Cana-de-açúcar): ").strip()
                    while cultura_input not in ['1', '2']:
                        print("Opção inválida.")
                        cultura_input = input("Escolha a nova cultura (1. Café, 2. Cana-de-açúcar): ").strip()
                    dados[indice - 1]['cultura'] = 'cafe' if cultura_input == '1' else 'cana-de-acucar'
                elif campo == 'area':
                    cultura = dados[indice - 1]['cultura']
                    if cultura == 'cafe':
                        while True:
                            try:
                                lado = float(input("Informe o novo comprimento do lado do hexágono (em metros): "))
                                if lado > 0:
                                    area = calcular_area_hexagono(lado)
                                    dados[indice - 1]['area'] = area
                                    break
                                else:
                                    print("O valor deve ser maior que zero.")
                            except ValueError:
                                print("Entrada inválida. Por favor, insira um número válido.")
                    else:
                        while True:
                            try:
                                comprimento = float(input("Informe o novo comprimento do retângulo (em metros): "))
                                largura = float(input("Informe a nova largura do retângulo (em metros): "))
                                if comprimento > 0 and largura > 0:
                                    area = calcular_area_retangulo(comprimento, largura)
                                    dados[indice - 1]['area'] = area
                                    break
                                else:
                                    print("Os valores devem ser maiores que zero.")
                            except ValueError:
                                print("Entrada inválida. Por favor, insira números válidos.")
                elif campo == 'num_linhas':
                    while True:
                        try:
                            num_linhas = int(input("Informe o novo número de linhas na lavoura: "))
                            if num_linhas > 0:
                                dados[indice - 1]['num_linhas'] = num_linhas
                                break
                            else:
                                print("O número deve ser maior que zero.")
                        except ValueError:
                            print("Entrada inválida. Por favor, insira um número inteiro válido.")
                elif campo == 'dados_solo':
                    dados[indice - 1]['dados_solo'] = coletar_dados_solo()
                elif campo == 'dados_clima':
                    dados[indice - 1]['dados_clima'] = coletar_dados_clima()
                #elif campo == 'historico_cultivo':
                #    dados[indice - 1]['historico_cultivo'] = coletar_historico_cultivo()

                # Recalcular insumos após atualização
                registro = dados[indice - 1]
                recomendacoes = carregar_recomendacoes()
                insumos_recomendados = calcular_manejo_insumos(
                    registro['dados_solo'],
                    registro['dados_clima'],
                    registro['historico_cultivo'],
                    registro['cultura'],
                    registro['area'],
                    registro['num_linhas'],
                    recomendacoes
                )
                dados[indice - 1]['insumos_recomendados'] = insumos_recomendados

                salvar_dados_parquet(dados)
                print("\nRegistro atualizado com sucesso.")
        else:
            print("Número de registro inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro válido.")


def deletar_registro(dados):
    if not dados:
        print("\nNão há registros para deletar.")
        return

    try:
        indice = int(input(f"\nInforme o número do registro que deseja deletar (1 - {len(dados)}): "))
        if 1 <= indice <= len(dados):
            registro = dados.pop(indice - 1)
            salvar_dados_parquet(dados)
            print("\nRegistro deletado com sucesso.")
        else:
            print("Número de registro inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro válido.")


def main():
    #dados = []
    dados = carregar_dados_parquet()
    recomendacoes = carregar_recomendacoes()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == '1':
            adicionar_registro(dados, recomendacoes)
        elif opcao == '2':
            visualizar_todos_registros(dados)
        elif opcao == '3':
            atualizar_registro(dados)
        elif opcao == '4':
            deletar_registro(dados)
        elif opcao == '0':
            print("\nSaindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

        #salvar_dados_parquet(dados)


if __name__ == "__main__":
    main()
