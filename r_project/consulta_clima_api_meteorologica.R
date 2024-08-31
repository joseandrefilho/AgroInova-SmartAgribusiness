# Instalar pacotes se não estiverem instalados
if (!require(httr)) install.packages("httr")
if (!require(jsonlite)) install.packages("jsonlite")

# Carregar os pacotes
library(httr)
library(jsonlite)

# Defina sua chave de API
api_key <- "73caffe41a1645cd872151857243108"  # Substitua "sua_chave_api" pela chave que você obteve

# Defina a localização para a qual deseja obter os dados meteorológicos (por exemplo, São Paulo, Brasil)
cidade <- "São Paulo"

# Construa a URL da requisição
url <- URLencode(paste0("http://api.weatherapi.com/v1/current.json?key=", api_key, "&q=", cidade, "&lang=pt"))

# Verifique a URL gerada (opcional)
cat("URL gerada:", url, "\n")

# Faça a requisição para a API
response <- GET(url)

# Verifique se a requisição foi bem-sucedida
if (status_code(response) == 200) {
  # Converta o conteúdo da resposta para formato JSON com UTF-8 explicitamente definido
  dados_meteorologicos <- fromJSON(content(response, as = "text", encoding = "UTF-8"))
  
  # Extraia as informações principais da localização
  cidade <- dados_meteorologicos$location$name
  regiao <- dados_meteorologicos$location$region
  pais <- dados_meteorologicos$location$country
  latitude <- dados_meteorologicos$location$lat
  longitude <- dados_meteorologicos$location$lon
  fuso_horario <- dados_meteorologicos$location$tz_id
  hora_local <- dados_meteorologicos$location$localtime
  
  # Extraia as informações principais do clima atual
  temperatura <- dados_meteorologicos$current$temp_c
  descricao <- dados_meteorologicos$current$condition$text
  umidade <- dados_meteorologicos$current$humidity
  vento_kph <- dados_meteorologicos$current$wind_kph
  vento_dir <- dados_meteorologicos$current$wind_dir
  pressao <- dados_meteorologicos$current$pressure_mb
  precipitacao <- dados_meteorologicos$current$precip_mm
  nuvens <- dados_meteorologicos$current$cloud
  sensacao_termica <- dados_meteorologicos$current$feelslike_c
  ponto_orvalho <- dados_meteorologicos$current$dewpoint_c
  visibilidade <- dados_meteorologicos$current$vis_km
  uv_index <- dados_meteorologicos$current$uv
  rajada_vento <- dados_meteorologicos$current$gust_kph
  
  # Exiba os dados processados no terminal de forma amigável
  cat("----- Informações da Localização -----\n")
  cat("Cidade: ", cidade, "\n")
  cat("Região: ", regiao, "\n")
  cat("País: ", pais, "\n")
  cat("Latitude: ", latitude, "\n")
  cat("Longitude: ", longitude, "\n")
  cat("Fuso Horário: ", fuso_horario, "\n")
  cat("Hora Local: ", hora_local, "\n")
  
  cat("\n----- Condições Climáticas Atuais -----\n")
  cat("Temperatura: ", temperatura, "°C\n")
  cat("Descrição: ", descricao, "\n")
  cat("Umidade: ", umidade, "%\n")
  cat("Velocidade do Vento: ", vento_kph, "km/h (", vento_dir, ")\n")
  cat("Pressão Atmosférica: ", pressao, " mb\n")
  cat("Precipitação: ", precipitacao, " mm\n")
  cat("Cobertura de Nuvens: ", nuvens, "%\n")
  cat("Sensação Térmica: ", sensacao_termica, "°C\n")
  cat("Ponto de Orvalho: ", ponto_orvalho, "°C\n")
  cat("Visibilidade: ", visibilidade, " km\n")
  cat("Índice UV: ", uv_index, "\n")
  cat("Rajada de Vento: ", rajada_vento, " km/h\n")
  
  cat("\n----- Informações Adicionais -----\n")
  cat("Dados atualizados em: ", dados_meteorologicos$current$last_updated, "\n")
  
} else {
  cat("Erro ao obter os dados da API. Código de status:", status_code(response), "\n")
}

      

