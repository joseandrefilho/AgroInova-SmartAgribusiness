# Instalação do pacote necessário (execute apenas uma vez, se ainda não estiver instalado)
# install.packages("arrow")

# Carregar pacotes necessários
library(arrow)
library(dplyr)

# Definir o caminho para o arquivo Parquet gerado no Python
arquivo_parquet <- "../data/processed/dados_agricultura.parquet"

# Ler o arquivo Parquet para um dataframe
df <- read_parquet(arquivo_parquet)

# Visualizar as primeiras linhas do dataframe para verificar a estrutura
print("Dados de Insumos Agrícolas")
print(head(df))

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
    desvio_padrao_fertilizante_P = sd(insumos_recomendados$fertilizantes$P, na.rm = TRUE)
    ,media_herbicida = mean(insumos_recomendados$herbicida, na.rm = TRUE),
    desvio_padrao_herbicida = sd(insumos_recomendados$herbicida, na.rm = TRUE)
  )

# Exibir as estatísticas
print("Estatísticas básicas por cultura:")
print(estatisticas)

# Exportar as estatísticas para um arquivo CSV
write.csv(estatisticas, '../data/output/estatisticas_culturas.csv', row.names = FALSE)
print("Estatísticas exportadas para 'estatisticas_culturas.csv'.")
