# comparador_numeros.py
# Demonstração de operadores relacionais e lógicos

# Reutilizamos a função de validação já consolidada
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

# Coleta e validação dos números
print("=== COMPARADOR DE NÚMEROS ===\n")

while True:
    num1_str = input("Digite o primeiro número: ")
    num1, erro = validar_numero(num1_str)
    if erro:
        print(f"Erro: {erro}. Tente novamente.")
        continue
    break

while True:
    num2_str = input("Digite o segundo número: ")
    num2, erro = validar_numero(num2_str)
    if erro:
        print(f"Erro: {erro}. Tente novamente.")
        continue
    break

# Exibição das comparações relacionais
print("\n" + "="*50)
print("COMPARAÇÕES RELACIONAIS:")
print("="*50)

print(f"{num1} == {num2}  -> {num1 == num2}")
print(f"{num1} != {num2}  -> {num1 != num2}")
print(f"{num1} >  {num2}  -> {num1 > num2}")
print(f"{num1} <  {num2}  -> {num1 < num2}")
print(f"{num1} >= {num2}  -> {num1 >= num2}")
print(f"{num1} <= {num2}  -> {num1 <= num2}")

# Análise combinada com operadores lógicos
print("\n" + "="*50)
print("ANÁLISE COMBINADA (LÓGICA):")
print("="*50)

# Verifica se ambos são positivos
ambos_positivos = num1 > 0 and num2 > 0
print(f"Ambos são positivos? -> {ambos_positivos}")

# Verifica se pelo menos um é par (válido apenas para inteiros)
# Como o usuário pode digitar float, precisamos verificar se são inteiros
if isinstance(num1, int) and isinstance(num2, int):
    pelo_menos_um_par = (num1 % 2 == 0) or (num2 % 2 == 0)
    print(f"Pelo menos um é par? -> {pelo_menos_um_par}")
else:
    print("Pelo menos um é par? -> Não se aplica (números não inteiros)")

# Verifica se o primeiro é maior que o segundo e ambos são diferentes de zero
condicao_especial = (num1 > num2) and (num1 != 0) and (num2 != 0)
print(f"{num1} > {num2} e ambos não são zero? -> {condicao_especial}")

# Usando o operador not
nao_eh_zero = not (num1 == 0)
print(f"O primeiro número NÃO é zero? -> {nao_eh_zero}")

print("="*50)