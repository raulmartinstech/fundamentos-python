# calculadora_operadores.py
# Demonstração de todos os operadores aritméticos com validação

# -------------------------------------------------
# 1. FUNÇÃO PARA VALIDAR NÚMERO (já conhecida)
# -------------------------------------------------
def validar_numero(texto):
    texto_limpo = texto.strip()
    if texto_limpo == "":
        return None, "Número vazio."
    
    texto_sem_sinal = texto_limpo.lstrip('-')
    if texto_sem_sinal == "":
        return None, "Número inválido (apenas sinal)."
    
    if texto_sem_sinal.count('.') <= 1:
        parte_numerica = texto_sem_sinal.replace('.', '')
        if parte_numerica.isdigit():
            if '.' in texto_sem_sinal:
                return float(texto_limpo), None
            else:
                return int(texto_limpo), None
    
    return None, "Número inválido. Use números, ponto decimal e sinal."

# -------------------------------------------------
# 2. PROGRAMA PRINCIPAL
# -------------------------------------------------
print("=== CALCULADORA DE OPERADORES ===\n")

# Coleta e validação do primeiro número
while True:
    num1_str = input("Digite o primeiro número: ")
    num1, erro = validar_numero(num1_str)
    if erro:
        print(f"Erro: {erro}. Tente novamente.")
        continue
    break

# Coleta e validação do segundo número
while True:
    num2_str = input("Digite o segundo número: ")
    num2, erro = validar_numero(num2_str)
    if erro:
        print(f"Erro: {erro}. Tente novamente.")
        continue
    break

# Exibição dos resultados com formatação condicional
print("\n" + "="*50)
print("RESULTADOS:")
print("="*50)

# Adição
print(f"{num1} + {num2} = {num1 + num2}")

# Subtração
print(f"{num1} - {num2} = {num1 - num2}")

# Multiplicação
print(f"{num1} * {num2} = {num1 * num2}")

# Divisão exata (sempre retorna float)
if num2 == 0:
    print(f"{num1} / {num2} = (Divisão por zero não permitida)")
else:
    print(f"{num1} / {num2} = {num1 / num2}")

# Divisão inteira (quantas vezes cabe inteiro)
if num2 == 0:
    print(f"{num1} // {num2} = (Divisão por zero não permitida)")
else:
    # A divisão inteira funciona com números negativos arredondando para baixo.
    print(f"{num1} // {num2} = {num1 // num2}")

# Módulo (resto da divisão)
if num2 == 0:
    print(f"{num1} % {num2} = (Divisão por zero não permitida)")
else:
    print(f"{num1} % {num2} = {num1 % num2}")

# Exponenciação
print(f"{num1} ** {num2} = {num1 ** num2}")

print("="*50)