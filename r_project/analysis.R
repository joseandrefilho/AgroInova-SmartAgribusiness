# /r_project/analysis.R

# Carregar os pacotes necessários
library(arrow)
library(dplyr)

# Carregar os dados do arquivo Parquet
dados <- read_parquet('data/processed/dados_agricultura.parquet')

# Visualizar os dados carregados
print("Dados carregados:")
print(dados)

# Calcular estatísticas básicas para cada cultura
estatisticas <- dados %>%
  group_by(cultura) %>%
  summarise(
    media_area = mean(area),
    desvio_padrao_area = sd(area),
    media_fertilizante = mean(quantidade_fertilizante),
    desvio_padrao_fertilizante = sd(quantidade_fertilizante),
    media_herbicida = mean(quantidade_herbicida),
    desvio_padrao_herbicida = sd(quantidade_herbicida)
  )

# Exibir as estatísticas
print("Estatísticas básicas por cultura:")
print(estatisticas)

# Exportar as estatísticas para um arquivo CSV (opcional)
write.csv(estatisticas, 'data/output/estatisticas_culturas.csv', row.names = FALSE)
print("Estatísticas exportadas para 'estatisticas_culturas.csv'.")

# Gerar gráficos (opcional)
# Exemplo: Gráfico de barras para a quantidade média de fertilizante por cultura
library(ggplot2)

ggplot(estatisticas, aes(x = cultura, y = media_fertilizante, fill = cultura)) +
  geom_bar(stat = "identity") +
  labs(title = "Média de Fertilizante por Cultura", x = "Cultura", y = "Média de Fertilizante (litros)") +
  theme_minimal()

# Salvar o gráfico
ggsave("data/output/media_fertilizante_por_cultura.png")
print("Gráfico salvo como 'media_fertilizante_por_cultura.png'.")
