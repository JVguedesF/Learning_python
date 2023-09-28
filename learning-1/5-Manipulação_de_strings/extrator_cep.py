# Importa o módulo re para lidar com expressões regulares
import re

# Define o endereço a ser analisado
endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

# Define o padrão RegEx para buscar CEPs no formato 5 dígitos + hífen (opcional) + 3 dígitos
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

# Realiza uma busca no texto do endereço usando o padrão definido
busca = padrao.search(endereco)  # Encontra o primeiro CEP correspondente

# Verifica se houve uma correspondência
if busca:
    # Obtém o CEP correspondente encontrado
    cep = busca.group()
    print(cep)  # Exibe o CEP encontrado