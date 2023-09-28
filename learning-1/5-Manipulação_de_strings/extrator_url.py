import re

# Classe ExtratorURL para manipular URLs
class ExtratorURL:
    def __init__(self, url):
        # Inicializa a instância da classe com uma URL, sanitizando-a e validando-a
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self, url):
        # Remove espaços em branco no início e no final da URL
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        # Valida se a URL não está vazia e segue um padrão específico
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida.")

    def get_url_base(self):
        # Retorna a parte da URL antes do caractere '?', que é a base da URL
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        # Retorna a parte da URL após o caractere '?', que são os parâmetros
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        # Obtém o valor de um parâmetro específico na URL
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        # Sobrescreve o método de tamanho para retornar o tamanho da URL
        return len(self.url)

    def __str__(self):
        # Sobrescreve o método de string para exibir informações da URL
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        # Sobrescreve o método de igualdade para comparar duas instâncias pelo valor da URL
        return self.url == other.url

# Exemplo de uso da classe ExtratorURL
url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)

print("O tamanho da URL é: ", len(extrator_url))
print("URL completa: ", extrator_url)

# Verifica que duas instâncias com a mesma URL são iguais
print("extrator_url == extrator_url_2? ", extrator_url == extrator_url_2)

# Busca o valor do parâmetro quantidade
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print("Valor do parâmetro 'quantidade': ", valor_quantidade)