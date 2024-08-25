
# Agricultura Digital Project

## Descrição do Projeto

Este projeto tem como objetivo calcular a área de plantio e o manejo de insumos para as culturas agrícolas de café e cana-de-açúcar. A aplicação foi desenvolvida em Python, com um módulo adicional em R para realizar análises estatísticas dos dados coletados.

## Estrutura do Projeto

A estrutura de diretórios do projeto é organizada da seguinte forma:

```
/AgriculturaDigitalProject
│
├── /data
│   ├── /processed          # Dados processados, incluindo arquivos Parquet
│   │   └── dados_agricultura.parquet
│   └── /output             # Resultados finais, gráficos, relatórios, etc.
│
├── /python
│   ├── __init__.py
│   ├── main.py             # Script principal em Python para cálculos e exportação
│   ├── area_calculations.py # Funções de cálculo de área
│   └── manejo_insumos.py    # Funções de manejo de insumos
│
├── /r
│   ├── analysis.R          # Script R para análise estatística dos dados Parquet
│   └── requirements.R      # Lista de pacotes necessários para o ambiente R
│
├── /docs
│   └── README.md           # Instruções gerais sobre o projeto
│
└── /env
    ├── requirements.txt    # Dependências para Python
    └── environment.yml     # Arquivo YAML para Conda, se estiver usando
```

## Configuração do Ambiente

### 1. Configuração do Ambiente Python

Para configurar o ambiente Python, siga os passos abaixo:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/AgriculturaDigitalProject.git
   cd AgriculturaDigitalProject/python
   ```

2. **Crie um ambiente virtual e instale as dependências:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   .\venv\Scripts\activate  # Windows
   pip install -r ../env/requirements.txt
   ```

3. **Execute o script Python:**

   ```bash
   python main.py
   ```

### 2. Configuração do Ambiente R

Para configurar o ambiente R, siga os passos abaixo:

1. **Instale as dependências do R:**

   Navegue até a pasta `/r` e execute o script `requirements.R` no R ou RStudio para instalar os pacotes necessários.

   ```r
   source("requirements.R")
   ```

2. **Execute a análise:**

   Depois que os dados forem gerados pelo script Python, você pode realizar a análise estatística no R:

   ```r
   source("analysis.R")
   ```

## Uso da Aplicação

### Passo a Passo

1. **Entrada de Dados:**
   - No menu do script Python (`main.py`), escolha a cultura (café ou cana-de-açúcar).
   - Informe as dimensões necessárias para calcular a área (lado do hexágono para café, ou comprimento e largura para cana-de-açúcar).
   - Insira informações sobre o pH do solo e a previsão do clima.
   - O programa calculará automaticamente a quantidade de fertilizante e herbicida necessários e salvará os dados em um arquivo Parquet.

2. **Análise dos Dados:**
   - Use o script R (`analysis.R`) para carregar os dados do arquivo Parquet e realizar análises estatísticas, como cálculo de médias e desvios padrão.

3. **Resultados e Gráficos:**
   - O script R também gera gráficos que podem ser encontrados na pasta `/data/output`.

## Estrutura de Dados

Os dados manipulados pelo projeto são organizados da seguinte forma:

- **`cultura:`** A cultura selecionada (café ou cana-de-açúcar).
- **`area:`** A área calculada em metros quadrados.
- **`ph_solo:`** O pH do solo informado.
- **`clima_previsao:`** A previsão do clima informada (sol/chuva).
- **`quantidade_fertilizante:`** Quantidade de fertilizante necessária (em litros).
- **`quantidade_herbicida:`** Quantidade de herbicida necessária (em litros).

## Contribuição

Contribuições para o projeto são bem-vindas. Siga as etapas abaixo para contribuir:

1. Faça um fork do repositório.
2. Crie uma branch para suas alterações (`git checkout -b feature/nova-funcionalidade`).
3. Commit suas alterações (`git commit -m 'Adiciona nova funcionalidade'`).
4. Faça o push para a branch (`git push origin feature/nova-funcionalidade`).
5. Abra um Pull Request para revisar suas alterações.

## Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais informações.

## Contato

Para mais informações, entre em contato com [Seu Nome](mailto:seu-email@example.com).
