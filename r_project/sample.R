# Instalar os pacotes necessários, se ainda não estiverem instalados
#install.packages("arrow")

# Carregar o pacote necessário
library(arrow)

rm(list = ls())

# Ler o arquivo CSV
dados <- read_parquet("../data/processed/novo_dados_agricultura.parquet")


