# AgroInova - Smart Agribusiness

## Descrição

Bem-vindo ao repositório do projeto **AgroInova**, desenvolvido pela equipe de Dev da Startup FarmTech Solutions. O objetivo deste projeto é aplicar soluções tecnológicas inovadoras no agronegócio, focando no cultivo de Café e Cana-de-açúcar. Utilizando Python e R, esta aplicação fornece ferramentas para o cálculo de áreas de plantio, manejo de insumos, e análise de dados estatísticos, integrando também dados climáticos via API.

## Informações sobre as Culturas

### Café
O cultivo de Café é uma das principais atividades agrícolas no Brasil, sendo o país o maior produtor e exportador mundial. O projeto AgroInova utiliza formas geométricas de hexágonos para calcular as áreas de plantio de café. As análises e manejos são adaptados para otimizar o uso de recursos e maximizar a produtividade dessa cultura.

### Cana-de-açúcar
A Cana-de-açúcar também é uma cultura de grande importância econômica no Brasil, utilizada principalmente para a produção de açúcar e etanol. No projeto AgroInova, utilizamos formas geométricas de retângulos para calcular as áreas de plantio da cana. O manejo de insumos e a análise de dados são feitos de forma a garantir a eficiência e sustentabilidade do cultivo.

## Funcionalidades

- **Cálculo de Área de Plantio:**  
  Calcule a área plantada para culturas específicas utilizando formas geométricas como hexágonos (Café) e retângulos (Cana-de-açúcar).

- **Manejo de Insumos:**  
  Determine a quantidade necessária de insumos e aplique-os de maneira eficiente, calculando, por exemplo, a quantidade de fosfato ou litros de pulverização por metro.

- **Gestão de Dados:**  
  Interface interativa para entrada, saída, atualização, e deleção de dados referentes às culturas e insumos.

- **Análise Estatística:**  
  Use R para calcular estatísticas básicas como média e desvio padrão, com base nos dados inseridos.

- **Integração com API Meteorológica:**  
  Conecte-se a uma API pública para obter dados climáticos e exibi-los no terminal.

## Itens Atendidos

Este projeto foi desenvolvido para atender a todos os requisitos da atividade avaliativa conforme solicitado:

a. **Suporte a 2 tipos de culturas:**  
   As culturas escolhidas foram Café e Cana-de-açúcar, ambas de grande importância no estado de São Paulo.

b. **Cálculo de área de plantio:**  
   Implementado utilizando formas geométricas específicas: hexágonos para Café e retângulos para Cana-de-açúcar.

c. **Cálculo do manejo de insumos:**  
   Desenvolvido para calcular a quantidade necessária de insumos com base em parâmetros específicos para cada cultura.

d. **Dados organizados em vetores:**  
   Os dados de entrada e manipulação são armazenados em vetores, conforme solicitado.

e. **Menu de opções na aplicação Python:**  
   A aplicação inclui um menu interativo com opções para entrada, saída, atualização e deleção de dados, além de permitir sair do programa.

f. **Uso de rotinas de loop e decisão:**  
   Loops e estruturas de decisão são utilizados para garantir a funcionalidade correta da aplicação.

g. **Aplicação em R para cálculos estatísticos:**  
   Uma aplicação em R foi desenvolvida para calcular média e desvio padrão, integrando-se ao projeto via GitHub para versionamento.

h. **Resumo do artigo da disciplina de Formação Social:**  
   O resumo do artigo exigido foi incluído na pasta `docs`, seguindo as especificações de formato solicitadas.


## Estrutura do Projeto

- **/python_project**  
  Contém o código-fonte em Python.
  
- **/r_project**  
  Contém o código-fonte em R.
  
- **/data**  
  Dados de exemplo e arquivos de entrada utilizados para testes.
  
- **/docs**  
  Documentação adicional, incluindo o resumo do artigo exigido pela disciplina de Formação Social.

- **README.md**  
  Este arquivo com informações sobre o projeto.

## Como Executar

### Pré-requisitos

- Python 3.x
- R

### Passos para Executar

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/AgroInova-SmartAgribusiness.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd AgroInova-SmartAgribusiness
    ```
3. Execute o script principal em Python:
    ```bash
    python python_project/gestao_agricola_agroinova.py
    ```
4. Para a análise estatística em R, execute o script `analise_dados_agricultura.R`:
    ```bash
    Rscript r_project/analise_dados_agricultura.R
    ```
5. Para consultar a API meteorológica em R, execute o script `consulta_clima_api_meteorologica.R`:
    ```bash
    Rscript r_project/consulta_clima_api_meteorologica.R
    ```

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para mais informações, entre em contato com a equipe através do e-mail: `rm87775@fiap.com.br`.
