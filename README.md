
# AgroInova - Smart Agribusiness

## Descrição

Bem-vindo ao repositório do projeto **AgroInova**, desenvolvido pela equipe de Dev da Startup FarmTech Solutions. O objetivo deste projeto é aplicar soluções tecnológicas inovadoras no agronegócio, focando no cultivo de Café e Cana-de-açúcar. Utilizando Python e R, esta aplicação fornece ferramentas para o cálculo de áreas de plantio, manejo de insumos, e análise de dados estatísticos, integrando também dados climáticos via API.

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

## Estrutura do Projeto

- **/src**  
  Contém o código-fonte em Python e R.
  
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
- Bibliotecas necessárias (ver `requirements.txt`)

### Passos para Executar

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/AgroInova-SmartAgribusiness.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd AgroInova-SmartAgribusiness
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4. Execute o script principal em Python:
    ```bash
    python src/main.py
    ```
5. Para a análise estatística em R, execute o script `analysis.R`:
    ```bash
    Rscript src/analysis.R
    ```

## Contribuições

Contribuições são bem-vindas! Por favor, siga estas etapas para contribuir:

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/sua-feature`).
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`).
4. Faça o push para a branch (`git push origin feature/sua-feature`).
5. Abra um Pull Request.

## Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para mais informações, entre em contato com a equipe através do e-mail: `rm87775@fiap.com.br`.
