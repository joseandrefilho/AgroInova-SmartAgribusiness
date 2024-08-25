# /r_project/requirements.R

# Instalar e carregar pacotes necessários

# Pacote para leitura de arquivos Parquet
if (!requireNamespace("arrow", quietly = TRUE)) {
  install.packages("arrow")
}
library(arrow)

# Pacote para manipulação de dados
if (!requireNamespace("dplyr", quietly = TRUE)) {
  install.packages("dplyr")
}
library(dplyr)

# Pacote para visualização de dados (gráficos)
if (!requireNamespace("ggplot2", quietly = TRUE)) {
  install.packages("ggplot2")
}
library(ggplot2)

# Opcional: Pacote para leitura/escrita de arquivos CSV
if (!requireNamespace("readr", quietly = TRUE)) {
  install.packages("readr")
}
lib
