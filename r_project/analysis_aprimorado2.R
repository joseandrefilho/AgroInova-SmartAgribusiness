# Instalação do pacote necessário (execute apenas uma vez, se ainda não estiver instalado)
# install.packages("arrow")

# Carregar pacotes necessários
library(arrow)  # Para leitura de arquivos Parquet
library(dplyr)  # Para manipulação de dados

# Função para verificar se o arquivo Parquet existe
verificar_arquivo <- function(caminho) {
  if (!file.exists(caminho)) {
    stop("Arquivo Parquet não encontrado. Verifique o caminho.")
  }
}

# Função para carregar os dados do arquivo Parquet
carregar_dados <- function(caminho) {
  verificar_arquivo(caminho)
  df <- read_parquet(caminho)
  return(df)
}

# Função para calcular estatísticas básicas (média, desvio padrão, mediana, máximo e mínimo)
calcular_estatisticas <- function(df) {
  estatisticas <- df %>%
    group_by(cultura) %>%
    summarise(
      media_area = mean(area, na.rm = TRUE),
      desvio_padrao_area = sd(area, na.rm = TRUE),
      mediana_area = median(area, na.rm = TRUE),
      max_area = max(area, na.rm = TRUE),
      min_area = min(area, na.rm = TRUE),
      media_num_linhas = mean(num_linhas, na.rm = TRUE),
      desvio_padrao_num_linhas = sd(num_linhas, na.rm = TRUE),
      mediana_num_linhas = median(num_linhas, na.rm = TRUE),
      max_num_linhas = max(num_linhas, na.rm = TRUE),
      min_num_linhas = min(num_linhas, na.rm = TRUE),
      media_potassio_solo = mean(dados_solo$nutrientes$K, na.rm = TRUE),
      desvio_padrao_potassio_solo = sd(dados_solo$nutrientes$K, na.rm = TRUE),
      mediana_potassio_solo = median(dados_solo$nutrientes$K, na.rm = TRUE),
      max_potassio_solo = max(dados_solo$nutrientes$K, na.rm = TRUE),
      min_potassio_solo = min(dados_solo$nutrientes$K, na.rm = TRUE),
      media_nitrogenio_solo = mean(dados_solo$nutrientes$N, na.rm = TRUE),
      desvio_padrao_nitrogenio_solo = sd(dados_solo$nutrientes$N, na.rm = TRUE),
      mediana_nitrogenio_solo = median(dados_solo$nutrientes$N, na.rm = TRUE),
      max_nitrogenio_solo = max(dados_solo$nutrientes$N, na.rm = TRUE),
      min_nitrogenio_solo = min(dados_solo$nutrientes$N, na.rm = TRUE),
      media_fosforo_solo = mean(dados_solo$nutrientes$P, na.rm = TRUE),
      desvio_padrao_fosforo_solo = sd(dados_solo$nutrientes$P, na.rm = TRUE),
      mediana_fosforo_solo = median(dados_solo$nutrientes$P, na.rm = TRUE),
      max_fosforo_solo = max(dados_solo$nutrientes$P, na.rm = TRUE),
      min_fosforo_solo = min(dados_solo$nutrientes$P, na.rm = TRUE),
      media_ph = mean(dados_solo$ph, na.rm = TRUE),
      desvio_padrao_ph = sd(dados_solo$ph, na.rm = TRUE),
      mediana_ph = median(dados_solo$ph, na.rm = TRUE),
      max_ph = max(dados_solo$ph, na.rm = TRUE),
      min_ph = min(dados_solo$ph, na.rm = TRUE),
      media_temperatura = mean(dados_clima$temperatura, na.rm = TRUE),
      desvio_padrao_temperatura = sd(dados_clima$temperatura, na.rm = TRUE),
      mediana_temperatura = median(dados_clima$temperatura, na.rm = TRUE),
      max_temperatura = max(dados_clima$temperatura, na.rm = TRUE),
      min_temperatura = min(dados_clima$temperatura, na.rm = TRUE),
      media_umidade = mean(dados_clima$umidade, na.rm = TRUE),
      desvio_padrao_umidade = sd(dados_clima$umidade, na.rm = TRUE),
      mediana_umidade = median(dados_clima$umidade, na.rm = TRUE),
      max_umidade = max(dados_clima$umidade, na.rm = TRUE),
      min_umidade = min(dados_clima$umidade, na.rm = TRUE),
      media_fertilizante_K = mean(insumos_recomendados$fertilizantes$K, na.rm = TRUE),
      desvio_padrao_fertilizante_K = sd(insumos_recomendados$fertilizantes$K, na.rm = TRUE),
      mediana_fertilizante_K = median(insumos_recomendados$fertilizantes$K, na.rm = TRUE),
      max_fertilizante_K = max(insumos_recomendados$fertilizantes$K, na.rm = TRUE),
      min_fertilizante_K = min(insumos_recomendados$fertilizantes$K, na.rm = TRUE),
      media_fertilizante_N = mean(insumos_recomendados$fertilizantes$N, na.rm = TRUE),
      desvio_padrao_fertilizante_N = sd(insumos_recomendados$fertilizantes$N, na.rm = TRUE),
      mediana_fertilizante_N = median(insumos_recomendados$fertilizantes$N, na.rm = TRUE),
      max_fertilizante_N = max(insumos_recomendados$fertilizantes$N, na.rm = TRUE),
      min_fertilizante_N = min(insumos_recomendados$fertilizantes$N, na.rm = TRUE),
      media_fertilizante_P = mean(insumos_recomendados$fertilizantes$P, na.rm = TRUE),
      desvio_padrao_fertilizante_P = sd(insumos_recomendados$fertilizantes$P, na.rm = TRUE),
      mediana_fertilizante_P = median(insumos_recomendados$fertilizantes$P, na.rm = TRUE),
      max_fertilizante_P = max(insumos_recomendados$fertilizantes$P, na.rm = TRUE),
      min_fertilizante_P = min(insumos_recomendados$fertilizantes$P, na.rm = TRUE),
      media_herbicida = mean(insumos_recomendados$herbicida, na.rm = TRUE),
      desvio_padrao_herbicida = sd(insumos_recomendados$herbicida, na.rm = TRUE),
      mediana_herbicida = median(insumos_recomendados$herbicida, na.rm = TRUE),
      max_herbicida = max(insumos_recomendados$herbicida, na.rm = TRUE),
      min_herbicida = min(insumos_recomendados$herbicida, na.rm = TRUE)
    )
  
  return(estatisticas)
}

# Função para gerar insights baseados nas estatísticas calculadas
gerar_insights <- function(estatisticas) {
  for (cultura in unique(estatisticas$cultura)) {
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
}

# Função para exportar estatísticas para um arquivo CSV
exportar_estatisticas <- function(estatisticas, caminho) {
  write.csv(estatisticas, caminho, row.names = FALSE)
  cat("Estatísticas exportadas para", caminho, "\n")
}

# Caminho do arquivo Parquet e do CSV de saída
arquivo_parquet <- "../data/processed/dados_agricultura.parquet"
arquivo_saida <- "../data/output/estatisticas_culturas.csv"

# Execução do processo
df <- carregar_dados(arquivo_parquet)
estatisticas <- calcular_estatisticas(df)

# Exibir as estatísticas no console
print("Estatísticas básicas por cultura:")
print(estatisticas)

# Gerar insights
gerar_insights(estatisticas)

# Exportar estatísticas para CSV
exportar_estatisticas(estatisticas, arquivo_saida)
