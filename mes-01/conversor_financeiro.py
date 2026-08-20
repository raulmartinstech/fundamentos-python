# conversor_financeiro.py
# Conversor de BRL para USD com análise booleana

# 1. Entrada
# Pergunta ao usuário um valor em reais (BRL) e o valor da cotação em reais (BRL)
reais = float(input("Digite o valor em reais (BRL): "))
cotacao = float(input("Digite o valor da cotação do dólar (USD) em reais: "))

# 2. Cálculo para achar o valor do dólar (USD)
dolar = reais / cotacao

# Análise booleana 
acima_de_1000 = dolar > 1000

# Saída
print(f"Valor em dólares: USD {dolar:.2f}")
print(f"Valor acima de 1000 USD? {acima_de_1000} (tipo: {type(acima_de_1000).__name__})")