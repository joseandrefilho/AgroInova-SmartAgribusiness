# Instalar pacotes se não estiverem instalados
if (!require(arrow)) install.packages("arrow")
if (!require(dplyr)) install.packages("dplyr")

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
      media_fertilizante = mean(insumos_recomendados$fertilizantes, na.rm = TRUE),
      desvio_padrao_fertilizante = sd(insumos_recomendados$fertilizantes, na.rm = TRUE),
      mediana_fertilizante = median(insumos_recomendados$fertilizantes, na.rm = TRUE),
      max_fertilizante = max(insumos_recomendados$fertilizantes, na.rm = TRUE),
      min_fertilizante = min(insumos_recomendados$fertilizantes, na.rm = TRUE),
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
    
    # Análise da variação de temperatura
    if (!is.na(subset_df$desvio_padrao_temperatura) && subset_df$desvio_padrao_temperatura > 5) {
      cat("ALERTA: Grande variação de temperatura observada. Isso pode impactar o crescimento das plantas.\n")
    } else {
      cat("Temperatura está dentro de uma variação aceitável.\n")
    }
    
    # Análise de umidade
    if (!is.na(subset_df$media_umidade) && subset_df$media_umidade < 30) {
      cat("RECOMENDAÇÃO: A umidade está abaixo do ideal. Considere ajustar as práticas de irrigação.\n")
    } else {
      cat("Umidade está dentro dos padrões esperados.\n")
    }
    
    # Análise de fertilizante
    if (!is.na(subset_df$desvio_padrao_fertilizante) && subset_df$desvio_padrao_fertilizante > 0.1) {
      cat("ALERTA: Grande variação na aplicação de fertilizantes. Considere padronizar as práticas para evitar desperdício.\n")
    } else {
      cat("Aplicação de fertilizantes está consistente.\n")
    }
    
    if (!is.na(subset_df$media_fertilizante) && subset_df$media_fertilizante < 0.5) {
      cat("RECOMENDAÇÃO: A aplicação de fertilizantes está baixa. Verifique se isso pode estar afetando a produtividade.\n")
    } else {
      cat("Aplicação de fertilizantes está dentro dos padrões esperados.\n")
    }
    
    # Análise de herbicida
    if (!is.na(subset_df$media_herbicida) && subset_df$media_herbicida > 0.5) {
      cat("RECOMENDAÇÃO: A aplicação de herbicida está alta. Verifique se isso é necessário para a cultura.\n")
    } else {
      cat("Aplicação de herbicida está dentro dos padrões esperados.\n")
    }
    
    # Substitua 'dados_solo' e 'dados_clima.previsao' pelos nomes corretos
    if ("dados_solo" %in% colnames(subset_df) && any(subset_df$dados_solo == "arenoso")) {
      cat("AVISO: Solo arenoso detectado. Isso pode necessitar de ajustes na irrigação e fertilização.\n")
    } else {
      cat("Solo adequado para o cultivo.\n")
    }
    
    if ("dados_clima.previsao" %in% colnames(subset_df)) {
      if (any(subset_df$dados_clima.previsao == "seca")) {
        cat("AVISO: Condições de seca previstas. Considere aumentar a irrigação.\n")
      } else if (any(subset_df$dados_clima.previsao == "chuva")) {
        cat("RECOMENDAÇÃO: Previsão de chuva. Planeje a aplicação de herbicidas e fertilizantes para evitar perdas.\n")
      }
    }
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
