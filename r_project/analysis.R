# Instalação do pacote necessário (execute apenas uma vez, se ainda não estiver instalado)
# install.packages("arrow")

# Carregar pacotes necessários
library(arrow)
library(dplyr)

# Definir o caminho para o arquivo Parquet gerado no Python
arquivo_parquet <- "../data/processed/novo_dados_agricultura.parquet"

#df1 <- read_parquet("../data/processed/dados_agricultura.parquet")
#df_gerado <- read_parquet("../data/processed/novo_dados_agricultura.parquet")
#rm(list = ls())

# Ler o arquivo Parquet para um dataframe
df <- read_parquet(arquivo_parquet)

# Visualizar as primeiras linhas do dataframe para verificar a estrutura
print("Dados de Insumos Agrícolas")
print(head(df))



# Calcular a média e o desvio padrão para cada variável numérica relevante, agrupando por cultura
#record <- df[1,] %>% area)



# Calcular a média e o desvio padrão para cada variável numérica relevante, agrupando por cultura
estatisticas <- df %>%
  group_by(cultura) %>%
  summarise(
    media_area = mean(area, na.rm = TRUE),
    desvio_padrao_area = sd(area, na.rm = TRUE),
    media_temperatura = mean(dados_clima$temperatura, na.rm = TRUE),
    desvio_padrao_temperatura = sd(dados_clima$temperatura, na.rm = TRUE),
    media_umidade = mean(dados_clima$umidade, na.rm = TRUE),
    desvio_padrao_umidade = sd(dados_clima$umidade, na.rm = TRUE),
    media_fertilizante = mean(insumos_recomendados$fertilizante, na.rm = TRUE),
    desvio_padrao_fertilizante = sd(insumos_recomendados$fertilizante, na.rm = TRUE),
    media_herbicida = mean(insumos_recomendados$herbicida, na.rm = TRUE),
    desvio_padrao_herbicida = sd(insumos_recomendados$herbicida, na.rm = TRUE)
  )

# Exibir as estatísticas
print("Estatísticas básicas por cultura:")
print(estatisticas)

# Exportar as estatísticas para um arquivo CSV
write.csv(estatisticas, '../data/output/estatisticas_culturas.csv', row.names = FALSE)
print("Estatísticas exportadas para 'estatisticas_culturas.csv'.")
