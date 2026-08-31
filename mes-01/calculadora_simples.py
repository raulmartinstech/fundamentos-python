# calculadora_simples.py
# Calculadora com validação básica de entrada.

# 1. Função auxiliar para limpar e validar um número (ainda sem try/except)
def validar_numero(texto):
    # Remove espaços das extremidades
    texto_limpo = texto.strip()
    
    # Verifica se a string está vazia
    if texto_limpo == "":
        return None, "Número vazio"
    
    # Verifica se é um número inteiro ou decimal
    # Estratégia: contar pontos decimais e verificar se os caracteres restantes são dígitos
    if texto_limpo.count('.') <= 1:
        # Substitui ponto por vazio e verifica se o resto é dígito
        parte_numerica = texto_limpo.replace('.', '')
        if parte_numerica.isdigit():
            # Se há ponto, converte para float; senão, para int
            if '.' in texto_limpo:
                return float(texto_limpo), None
            else:
                return int(texto_limpo), None
    
    # Se passou por todas as verificações sem retornar, é inválido
    return None, "Número inválido"

# 2. Coleta e validação dos dados
while True:
    num1_str = input("Digite o primeiro número: ")
    num1, erro1 = validar_numero(num1_str)
    if erro1:
        print(f"Erro no primeiro número: {erro1}. Tente novamente.")
        continue
    break

while True:
    num2_str = input("Digite o segundo número: ")
    num2, erro2 = validar_numero(num2_str)
    if erro2:
        print(f"Erro no segundo número: {erro2}. Tente novamente.")
        continue
    break

# 3. Coleta da operação
operacao = input("Digite a operação (+, -, *, /): ").strip()

# 4. Processamento e saída
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 == 0:
        print("Erro: Divisão por zero não é permitida.")
        resultado = None
    else:
        resultado = num1 / num2
else:
    print("Operação inválida.")
    resultado = None

if resultado is not None:
    # Formatação condicional: se for inteiro, exibe sem casas decimais
    if isinstance(resultado, int):
        print(f"Resultado: {resultado}")
    else:
        print(f"Resultado: {resultado:.2f}")