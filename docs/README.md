# AgroInova - Smart Agribusiness

## Visão Geral

O AgroInova é uma solução de software desenvolvida para ajudar agricultores a gerenciar suas operações agrícolas de forma mais eficiente. Através da integração de dados sobre solo, clima e insumos agrícolas, o AgroInova fornece recomendações precisas para o manejo de fertilizantes e herbicidas, contribuindo para uma melhor produtividade e sustentabilidade.

## Funcionalidades Principais

- **Cálculo de Manejo de Insumos**: Com base em dados sobre o solo, clima e área plantada, o AgroInova calcula a quantidade necessária de fertilizantes (N, P2O5, K2O) e herbicidas para culturas específicas.
- **Exportação de Dados**: Os dados gerados são salvos em um arquivo Parquet, facilitando a análise posterior.
- **Análise Estatística**: Um script em R é fornecido para calcular estatísticas básicas (média, desvio padrão) e gerar insights a partir dos dados salvos.

## Alterações Recentes

### 1. Remoção do Histórico de Cultivo

Anteriormente, o cálculo de manejo de insumos considerava o histórico de cultivo (rotatividade de culturas) como um dos fatores de ajuste. Esta funcionalidade foi removida para simplificar o cálculo e focar nas variáveis de solo e clima. 

Agora, o cálculo considera apenas:

- **Tipo de Solo**: Ajuste baseado no tipo de solo (arenoso, argiloso, etc.).
- **pH do Solo**: Ajuste baseado no pH do solo, que influencia a disponibilidade de nutrientes.
- **Condições Climáticas**: Ajuste baseado na previsão do clima (sol, chuva, nublado).

### 2. Ajuste na Função `calcular_manejo_insumos`

A função `calcular_manejo_insumos` foi simplificada, removendo qualquer influência do histórico de cultivo. O foco agora está no tipo de solo, pH e condições climáticas.

## Estrutura do Projeto

- **`main.py`**: Script principal onde os dados são inseridos e o cálculo de manejo de insumos é realizado.
- **`area_calculations.py`**: Contém funções para calcular a área plantada, considerando diferentes formas geométricas.
- **`manejo_insumos.py`**: Contém as recomendações padrão para cada cultura e a lógica para calcular as quantidades necessárias de fertilizantes e herbicidas.
- **`r_project/analysis.R`**: Script em R para análise estatística dos dados gerados, incluindo cálculo de média e desvio padrão.
- **`r_project/requirements.R`**: Lista de pacotes necessários para executar a análise em R.
- **`data/processed/`**: Diretório onde os arquivos Parquet gerados são armazenados.
- **`data/output/`**: Diretório onde os resultados da análise em R são salvos.

## Instruções de Uso

### 1. Executar o Código Python

1. Certifique-se de ter instalado os pacotes necessários: `pandas`, `pyarrow`.
2. Execute o script `main.py` para inserir os dados e calcular as quantidades de insumos.
3. O arquivo Parquet gerado será salvo em `data/processed/dados_agricultura.parquet`.

### 2. Executar o Código R

1. Instale os pacotes necessários mencionados em `r_project/requirements.R`.
2. Execute o script `r_project/analysis.R` para ler o arquivo Parquet e calcular as estatísticas.
3. Os resultados serão salvos em `data/output/estatisticas_culturas.csv`.

## Contribuições

Contribuições são bem-vindas! Por favor, faça um fork do repositório e envie um pull request com suas melhorias.

## Licença

Este projeto é licenciado sob a Licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
