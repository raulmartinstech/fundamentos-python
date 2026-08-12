# medias.py - Versão com aprovação/recuperação/reprovação

# 1. Entrada das notas
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a sugunda nota: "))
n3 = float(input("Digite a terceira nota: "))

# 2. processamento (cálculo da média)
media = (n1 + n2 + n3) / 3

# 3. Lógica de decisão
if media >= 7.0:
    status = "Aprovado"
elif media >= 5.0:
    status = "Recuperação"
else:
    status = "Reprovado"

# 4. Saída formatada
print(f"A média final do aluno é {media:.2f}. status: {status}. ")

