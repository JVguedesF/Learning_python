# Arquivo utilizado até a aula 3, quando então passamos a utilizar a classe
# ExtratorURL no arquivo extrator_url.py

# Definição da URL
url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"

# Sanitização da URL, removendo espaços em branco no início e no final
url = url.strip()

# Validação da URL: lança um erro se a URL estiver vazia
if url == "":
    raise ValueError("A URL está vazia")

# Separação da base da URL e dos parâmetros
indice_interrogacao = url.find('?')
url_base = url[:indice_interrogacao]
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca o valor de um parâmetro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&', indice_valor)

# Verificação se o valor do parâmetro termina com '&' ou não
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]

print(valor)