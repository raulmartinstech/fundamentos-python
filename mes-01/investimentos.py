# investimentos.py - Calculadora de Juros Compostos

# 1. Solicita e captura o capital inicial
capital = float(input("Insira o seu capital inicial: "))

# 2. Solicita e captura a taxa de juros mensal
taxa = float(input("Insira a taxa de juros menssal: "))

# 3. Solicita e captura o número de meses
tempo = int(input("Insira o número de meses: "))

# 4. Calcula o montante usando a fómula M = C * (1 + i/100) ** t
montante = capital * (1 + taxa/100) ** tempo

# 5. Exibe o resultado formatado 
print(f"Capital inicial: R$ {capital:.2f}\nTaxa mensal: {taxa}%\nMeses: {tempo}\nMontante final: R$ {montante:.2f}")

