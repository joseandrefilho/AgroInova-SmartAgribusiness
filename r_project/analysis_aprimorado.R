# Instalação do pacote necessário (execute apenas uma vez, se ainda não estiver instalado)
# install.packages("arrow")

# Carregar pacotes necessários
library(arrow)  # Para leitura de arquivos Parquet
library(dplyr)  # Para manipulação de dados

# Definir o caminho para o arquivo Parquet gerado no Python
arquivo_parquet <- "../data/processed/dados_agricultura.parquet"

if (!file.exists(arquivo_parquet)) {
  stop("Arquivo Parquet não encontrado. Verifique o caminho.")
}

# Ler o arquivo Parquet para um dataframe
df <- read_parquet(arquivo_parquet)

# Visualizar as primeiras linhas do dataframe para verificar a estrutura dos dados
print("Dados de Insumos Agrícolas")
print(head(df))

# Explicação:
# Este passo carrega os dados do arquivo Parquet gerado em Python para um dataframe em R.
# As primeiras linhas do dataframe são exibidas para garantir que a estrutura dos dados esteja correta.

# Calcular a média e o desvio padrão para cada variável numérica relevante, agrupando por cultura
estatisticas <- df %>%
  group_by(cultura) %>%
  summarise(
    media_area = mean(area, na.rm = TRUE),
    desvio_padrao_area = sd(area, na.rm = TRUE),
    media_num_linhas = mean(num_linhas, na.rm = TRUE),
    desvio_padrao_num_linhas = sd(num_linhas, na.rm = TRUE),
    media_potassio_solo = mean(dados_solo$nutrientes$K, na.rm = TRUE),
    desvio_padrao_potassio_solo = sd(dados_solo$nutrientes$K, na.rm = TRUE),
    media_nitrogenio_solo = mean(dados_solo$nutrientes$N, na.rm = TRUE),
    desvio_padrao_nitrogenio_solo = sd(dados_solo$nutrientes$N, na.rm = TRUE),
    media_fosforo_solo = mean(dados_solo$nutrientes$P, na.rm = TRUE),
    desvio_padrao_fosforo_solo = sd(dados_solo$nutrientes$P, na.rm = TRUE),
    media_ph = mean(dados_solo$ph, na.rm = TRUE),
    desvio_padrao_ph = sd(dados_solo$ph, na.rm = TRUE),
    media_temperatura = mean(dados_clima$temperatura, na.rm = TRUE),
    desvio_padrao_temperatura = sd(dados_clima$temperatura, na.rm = TRUE),
    media_umidade = mean(dados_clima$umidade, na.rm = TRUE),
    desvio_padrao_umidade = sd(dados_clima$umidade, na.rm = TRUE),
    media_fertilizante_K = mean(insumos_recomendados$fertilizantes$K, na.rm = TRUE),
    desvio_padrao_fertilizante_K = sd(insumos_recomendados$fertilizantes$K, na.rm = TRUE),
    media_fertilizante_N = mean(insumos_recomendados$fertilizantes$N, na.rm = TRUE),
    desvio_padrao_fertilizante_N = sd(insumos_recomendados$fertilizantes$N, na.rm = TRUE),
    media_fertilizante_P = mean(insumos_recomendados$fertilizantes$P, na.rm = TRUE),
    desvio_padrao_fertilizante_P = sd(insumos_recomendados$fertilizantes$P, na.rm = TRUE),
    media_herbicida = mean(insumos_recomendados$herbicida, na.rm = TRUE),
    desvio_padrao_herbicida = sd(insumos_recomendados$herbicida, na.rm = TRUE)
  )

# Explicação:
# Neste passo, calculamos as médias e desvios padrão para diversas variáveis, agrupadas por cultura.
# - A média indica o valor médio de cada variável para cada cultura.
# - O desvio padrão mostra o quanto os valores variam em relação à média.
# Isso ajuda a entender a consistência e a eficiência das práticas agrícolas utilizadas.

# Exibir as estatísticas no console
print("Estatísticas básicas por cultura:")
print(estatisticas)

# Explicação:
# As estatísticas calculadas são exibidas no console para revisão.
# Isso fornece uma visão rápida das tendências e variações nos dados de insumos e clima.

# Gerar insights a partir das estatísticas calculadas
# Exemplo de insights que podem ser gerados:
for (cultura in unique(df$cultura)) {
  cat("\nInsights para a cultura:", cultura, "\n")
  
  subset_df <- estatisticas[estatisticas$cultura == cultura, ]
  
  cat("Média da área plantada:", subset_df$media_area, "m²\n")
  cat("Variação na área plantada (desvio padrão):", subset_df$desvio_padrao_area, "m²\n")
  
  if (subset_df$desvio_padrao_fertilizante_N > 10) {
    cat("ALERTA: Grande variação na aplicação de Nitrogênio. Considere padronizar as práticas para evitar desperdício.\n")
  } else {
    cat("Aplicação de Nitrogênio está consistente.\n")
  }
  
  if (subset_df$media_fertilizante_K < 100) {
    cat("RECOMENDAÇÃO: A aplicação de Potássio (K2O) está baixa. Verifique se isso pode estar afetando a produtividade.\n")
  } else {
    cat("Aplicação de Potássio (K2O) está dentro dos padrões esperados.\n")
  }
  
  # Adicione mais insights conforme necessário
}

# Explicação:
# Este bloco de código gera insights com base nas estatísticas calculadas.
# Por exemplo:
# - Uma alta variação no desvio padrão pode indicar inconsistências que precisam ser abordadas.
# - Comparar as médias com valores de referência pode sugerir ajustes nas práticas de manejo.
# - Os insights ajudam a tomar decisões mais informadas e a melhorar a eficiência agrícola.

# Exportar as estatísticas para um arquivo CSV
write.csv(estatisticas, '../data/output/estatisticas_culturas.csv', row.names = FALSE)
print("Estatísticas exportadas para 'estatisticas_culturas.csv'.")

# Explicação:
# Finalmente, as estatísticas são exportadas para um arquivo CSV para fácil acesso e análise posterior.
# Isso é útil para gerar relatórios ou para uso em apresentações para stakeholders.
