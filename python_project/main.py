import os
import pandas as pd
import math

# Função para calcular a área de um hexágono dado o comprimento do lado
def calcular_area_hexagono(lado):
    """
    Calcula a área de um hexágono regular.
    A fórmula usada é: (3 * sqrt(3) * lado²) / 2
    É utilizada em plantações como a de café, onde a disposição hexagonal é comum.
    """
    return (3 * math.sqrt(3) * (lado ** 2)) / 2

# Função para calcular a área de um retângulo dado o comprimento e a largura
def calcular_area_retangulo(comprimento, largura):
    """
    Calcula a área de um retângulo.
    Fórmula: comprimento * largura
    Utilizada em plantações como a de cana-de-açúcar, onde a disposição retangular facilita o manejo mecanizado.
    """
    return comprimento * largura

# Função que carrega as recomendações padrão de insumos (fertilizante e herbicida) para cada cultura
def carregar_recomendacoes():
    """
    Carrega as recomendações de fertilizantes e herbicidas para culturas específicas.
    As recomendações são baseadas em práticas agrícolas comuns.
    """
    return {
        'cafe': {
            'fertilizante': 150,  # Quantidade de fertilizante em kg/ha
            'herbicida': 3        # Quantidade de herbicida em L/ha
        },
        'cana-de-acucar': {
            'fertilizante': 110,  # Quantidade de fertilizante em kg/ha
            'herbicida': 4        # Quantidade de herbicida em L/ha
        }
    }

# Função para calcular o manejo dos insumos (fertilizante e herbicida) baseados em dados do solo e clima
def calcular_manejo_insumos(dados_solo, dados_clima, cultura, area, recomendacoes):
    """
    Calcula a quantidade de fertilizantes e herbicidas necessária para uma determinada área de cultivo,
    considerando as condições do solo e do clima.
    """
    recomendacao = recomendacoes.get(cultura)
    if not recomendacao:
        raise ValueError("Recomendações não encontradas para a cultura especificada.")

    # Ajustes baseados no tipo de solo
    ajuste_solo = {
        'arenoso': 1.1,  # Solo arenoso aumenta a necessidade de insumos
        'argiloso': 0.9,  # Solo argiloso reduz a necessidade de insumos
        'outro': 1.0     # Sem ajuste específico para outros solos
    }.get(dados_solo['tipo_solo'], 1.0)

    # Ajustes baseados nas condições climáticas
    ajuste_clima = {
        'chuva': 0.9,   # Clima chuvoso reduz a aplicação de insumos para evitar lixiviação
        'nublado': 1.0, # Clima nublado não altera a aplicação
        'sol': 1.1      # Clima ensolarado aumenta a aplicação de insumos
    }.get(dados_clima['previsao'], 1.0)

    # Cálculo da quantidade necessária de fertilizante e herbicida
    quantidade_fertilizante = (
        recomendacao['fertilizante'] * 0.1 * ajuste_solo * ajuste_clima * (area / 10000)
    )

    quantidade_herbicida = (
        recomendacao['herbicida'] * ajuste_solo * ajuste_clima * (area / 10000)
    )

    return {
        'fertilizante': quantidade_fertilizante,
        'herbicida': quantidade_herbicida
    }

# Função para coletar dados sobre o solo onde a cultura será plantada
def coletar_dados_solo():
    """
    Coleta informações sobre o tipo de solo da área de cultivo.
    O tipo de solo influencia a retenção de nutrientes e a necessidade de insumos.
    """
    print("\n=== Coleta de Dados do Solo ===")
    print("Seu solo é a base de tudo. Vamos entender melhor as características dessa fundação.")
    print("\nEscolha o tipo de solo:")
    print("1. Arenoso - Leve, boa drenagem, baixa retenção de nutrientes.")
    print("2. Argiloso - Pesado, retém bem os nutrientes, drenagem difícil.")
    print("3. Outro - Outros tipos de solo.")

    tipo_solo = input("Informe o tipo de solo (1/2/3): ").strip().lower()
    while tipo_solo not in ['1', '2', '3']:
        print("Opção inválida. Tente novamente.")
        tipo_solo = input("Informe o tipo de solo (1/2/3): ").strip().lower()

    tipo_solo = {
        '1': 'arenoso',
        '2': 'argiloso',
        '3': 'outro'
    }[tipo_solo]

    return {'tipo_solo': tipo_solo}

# Função para coletar dados climáticos que influenciam o manejo da cultura
def coletar_dados_clima():
    """
    Coleta informações sobre as condições climáticas previstas para a área de cultivo.
    O clima afeta diretamente a quantidade de insumos a serem aplicados.
    """
    print("\n=== Coleta de Dados Climáticos ===")
    print("As condições climáticas moldam o destino de suas colheitas. Vamos prever o que vem pela frente.")

    previsao = input("Informe a previsão do clima (1. Sol, 2. Chuva, 3. Nublado): ").strip().lower()
    while previsao not in ['1', '2', '3']:
        print("Opção inválida. Tente novamente.")
        previsao = input("Informe a previsão do clima (1. Sol, 2. Chuva, 3. Nublado): ").strip().lower()

    previsao = {
        '1': 'sol',
        '2': 'chuva',
        '3': 'nublado'
    }[previsao]

    while True:
        try:
            temperatura = float(input("Informe a temperatura média (°C): "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

    while True:
        try:
            umidade = float(input("Informe a umidade relativa do ar (%): "))
            if 0 <= umidade <= 100:
                break
            else:
                print("A umidade deve estar entre 0 e 100%.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

    return {
        'previsao': previsao,
        'temperatura': temperatura,
        'umidade': umidade
    }

# Função para salvar os dados coletados em um arquivo no formato Parquet
def salvar_dados_parquet(dados, nome_arquivo='../data/processed/dados_agricultura.parquet'):
    """
    Salva os dados em um arquivo Parquet. Esse formato é eficiente para armazenamento de dados
    estruturados e permite rápida leitura e escrita.
    """
    df_novo = pd.DataFrame(dados)
    df_novo.to_parquet(nome_arquivo)

# Função para carregar os dados de um arquivo Parquet, se existir
def carregar_dados_parquet(nome_arquivo='../data/processed/dados_agricultura.parquet'):
    """
    Carrega os dados salvos previamente em um arquivo Parquet.
    Se o arquivo não existir, retorna uma lista vazia.
    """
    if os.path.exists(nome_arquivo):
        return pd.read_parquet(nome_arquivo).to_dict(orient='records')
    else:
        return []

# Função para exibir o menu principal do programa
def exibir_menu():
    """
    Exibe o menu principal com as opções disponíveis para o usuário.
    Permite que o usuário escolha entre registrar uma nova cultura, consultar, atualizar ou remover registros.
    """
    print("\n🌿 Bem-vindo ao AgroInova - Onde a Inovação Encontra a Agricultura 🌿")
    print("\nVocê está prestes a transformar sua gestão agrícola. Escolha como deseja começar sua jornada:\n")

    print("1. 🌱 Registrar Nova Cultura")
    print("   - Inicie sua jornada: Adicione dados sobre suas culturas, solo e clima. Cada registro é um passo para uma colheita mais próspera.")

    print("2. 🌾 Consultar Registros")
    print("   - Explore seus registros: Reflita sobre o passado e descubra insights para otimizar sua produção.")

    print("3. ✏️ Atualizar Informações")
    print("   - Aperfeiçoe seus dados: Mantenha suas informações atualizadas para garantir a precisão na gestão agrícola.")

    print("4. ❌ Remover Registro")
    print("   - Limpe o desnecessário: Remova registros antigos e mantenha seu banco de dados enxuto e eficiente.")

    print("0. 🚪 Sair do AgroInova")
    print("   - Finalize sua sessão: Tenha certeza de que seu trabalho está seguro e retorne quando precisar.")

# Função para adicionar um novo registro de cultura
def adicionar_registro(dados, recomendacoes):
    """
    Adiciona um novo registro ao banco de dados. O usuário escolhe a cultura,
    e a área é calculada com base na forma geométrica apropriada. Também são coletados dados do solo e do clima.
    """
    print("\n=== Adicionar Novo Registro ===")
    print("Vamos começar escolhendo a cultura para calcular a área plantada e determinar o manejo de insumos.\n")

    cultura_input = input("Escolha a cultura (1. Café, 2. Cana-de-açúcar): ").strip()
    while cultura_input not in ['1', '2']:
        print("Opção inválida.")
        cultura_input = input("Escolha a cultura (1. Café, 2. Cana-de-açúcar): ").strip()

    if cultura_input == '1':
        cultura = 'cafe'
        print("\nCafé é sinônimo de cuidado com cada planta. Vamos calcular a área com base em uma disposição hexagonal, ideal para maximizar o espaço.")
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
        print("\nPara a cana-de-açúcar, precisão é fundamental. Vamos calcular a área com base em retângulos, facilitando o manejo mecanizado.")
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

    dados_solo = coletar_dados_solo()
    dados_clima = coletar_dados_clima()

    insumos_recomendados = calcular_manejo_insumos(dados_solo, dados_clima, cultura, area, recomendacoes)

    registro = {
        'cultura': cultura,
        'area': area,
        'dados_solo': dados_solo,
        'dados_clima': dados_clima,
        'insumos_recomendados': insumos_recomendados
    }

    dados.append(registro)
    salvar_dados_parquet(dados)

    print("\n=== Registro Adicionado com Sucesso ===")
    visualizar_registro(registro, len(dados))
    input("\nPressione Enter para continuar...")

# Função para exibir todos os registros disponíveis
def visualizar_todos_registros(dados):
    """
    Permite que o usuário visualize registros específicos, solicitando um índice ou um intervalo de índices.
    Mostra detalhes de cada cultura, solo, clima e insumos recomendados.
    """
    if not dados:
        print("\nNenhum registro disponível para exibir.")
        return

    total_registros = len(dados)

    while True:

        try:
            indice = int(input(f"Informe o número do registro (1 - {total_registros}) ou 0 para sair: "))
            if 1 <= indice <= total_registros:
                visualizar_registro(dados[indice - 1], indice)
            elif indice == 0:
                break
            else:
                print(f"Índice fora do intervalo. Escolha um número entre 1 e {total_registros}.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

        input("\nPressione Enter para continuar...")


# Função para exibir um registro específico
def visualizar_registro(registro, indice):
    """
    Exibe os detalhes de um único registro, incluindo cultura, área, tipo de solo, clima e insumos recomendados.
    """
    print(f"Registro {indice} | Cultura: {registro['cultura'].capitalize()} | Área: {registro['area']:.2f} m² | "
          f"Tipo de Solo: {registro['dados_solo']['tipo_solo'].capitalize()} | "
          f"Previsão do Clima: {registro['dados_clima']['previsao'].capitalize()} | "
          f"Temperatura Média: {registro['dados_clima']['temperatura']} °C | "
          f"Umidade Relativa: {registro['dados_clima']['umidade']}% | "
          f"Fertilizante: {registro['insumos_recomendados']['fertilizante']:.2f} Kg | "
          f"Herbicida: {registro['insumos_recomendados']['herbicida']:.2f} L")


# Função para atualizar um registro existente
def atualizar_registro(dados):
    """
    Permite atualizar um registro existente. O usuário pode escolher se deseja atualizar a entrada completa ou apenas campos específicos.
    """
    if not dados:
        print("\nNenhum registro disponível para atualizar.")
        return

    try:
        indice = int(input(f"\nInforme o número do registro que deseja atualizar (1 - {len(dados)}): "))
        if 1 <= indice <= len(dados):
            registro_atual = dados[indice - 1]
            print("\n=== Dados Atuais do Registro ===")
            visualizar_registro(registro_atual, indice)

            print("\n=== Atualização de Dados ===")
            opcao = input("Deseja atualizar toda a entrada ou campos específicos? (1. Toda entrada, 2. Campos específicos, 3. Cancelar): ").strip()
            while opcao not in ['1', '2', '3']:
                print("Opção inválida.")
                opcao = input("Deseja atualizar toda a entrada ou campos específicos? (1. Toda entrada, 2. Campos específicos, 3. Cancelar): ").strip()

            if opcao == '3':
                print("Operação cancelada.")
            elif opcao == '1':
                recomendacoes = carregar_recomendacoes()
                adicionar_registro(dados[:indice - 1] + dados[indice:], recomendacoes)
                print("\nRegistro atualizado com sucesso.")
            else:
                print("\nEscolha o campo que deseja atualizar:")
                print("1. Cultura")
                print("2. Área")
                print("3. Dados do Solo")
                print("4. Dados Climáticos")
                campo_opcao = input("Informe o número do campo que deseja atualizar: ").strip()
                while campo_opcao not in ['1', '2', '3', '4']:
                    print("Opção inválida.")
                    campo_opcao = input("Informe o número do campo que deseja atualizar: ").strip()

                if campo_opcao == '1':
                    cultura_input = input("Escolha a nova cultura (1. Café, 2. Cana-de-açúcar): ").strip()
                    while cultura_input not in ['1', '2']:
                        print("Opção inválida.")
                        cultura_input = input("Escolha a nova cultura (1. Café, 2. Cana-de-açúcar): ").strip()
                    dados[indice - 1]['cultura'] = 'cafe' if cultura_input == '1' else 'cana-de-acucar'
                elif campo_opcao == '2':
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
                elif campo_opcao == '3':
                    dados[indice - 1]['dados_solo'] = coletar_dados_solo()
                elif campo_opcao == '4':
                    dados[indice - 1]['dados_clima'] = coletar_dados_clima()

                registro = dados[indice - 1]
                recomendacoes = carregar_recomendacoes()
                insumos_recomendados = calcular_manejo_insumos(
                    registro['dados_solo'],
                    registro['dados_clima'],
                    registro['cultura'],
                    registro['area'],
                    recomendacoes
                )
                dados[indice - 1]['insumos_recomendados'] = insumos_recomendados

                salvar_dados_parquet(dados)
                print("\nRegistro atualizado com sucesso.")
        else:
            print("Número de registro inválido.")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro válido.")

    input("\nPressione Enter para continuar...")


# Função para deletar um registro existente
def deletar_registro(dados):
    """
    Permite a exclusão de um registro existente. O usuário deve confirmar a exclusão antes que o registro seja removido.
    """
    if not dados:
        print("\nNenhum registro disponível para deletar.")
    else:
        try:
            indice = int(input(f"\nInforme o número do registro que deseja deletar (1 - {len(dados)}): "))
            if 1 <= indice <= len(dados):
                registro_atual = dados[indice - 1]
                print("\n=== Dados Atuais do Registro ===")
                visualizar_registro(registro_atual, indice)

                print("\n=== Exclusão de Dados ===")
                opcao = input("Deseja excluir o registro? (1. sim, 2. não): ").strip()
                while opcao not in ['1', '2']:
                    print("Opção inválida.")
                    opcao = input("Deseja excluir o registro? (1. sim, 2. não): ").strip()

                if opcao == '1':
                    dados.pop(indice - 1)
                    salvar_dados_parquet(dados)
                    print("\nRegistro deletado com sucesso.")
                else:
                    print("Registro não deletado.")
            else:
                print("Número de registro inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro válido.")

    input("\nPressione Enter para continuar...")

# Função principal que executa o programa
def main():
    """
    Função principal que executa o programa AgroInova. Carrega os dados salvos, exibe o menu e executa as ações escolhidas pelo usuário.
    """
    dados = carregar_dados_parquet()  # Carrega os dados já existentes
    recomendacoes = carregar_recomendacoes()  # Carrega as recomendações padrão de insumos

    while True:
        exibir_menu()  # Exibe o menu principal
        opcao_menu = input("Escolha uma opção: ").strip()

        if opcao_menu == '1':
            adicionar_registro(dados, recomendacoes)
        elif opcao_menu == '2':
            visualizar_todos_registros(dados)
        elif opcao_menu == '3':
            atualizar_registro(dados)
        elif opcao_menu == '4':
            deletar_registro(dados)
        elif opcao_menu == '0':
            print("\nSaindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
