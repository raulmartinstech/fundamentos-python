# saque_caixa.py
# Simulador de saque em caixa eletrônico com validação e cálculo de cédulas

# -------------------------------------------------
# 1. FUNÇÃO PARA VALIDAR NÚMERO INTEIRO POSITIVO
# -------------------------------------------------
def validar_numero(texto):
    """
    Valida se o texto pode ser convertido em um número inteiro positivo.
    Retorna (valor, erro) onde 'erro' é None se a validação for bem-sucedida.
    """
    # Remove espaços das bordas
    texto_limpo = texto.strip()
    
    # Verifica se está vazio
    if texto_limpo == "":
        return None, "Valor não pode estar vazio."
    
    # Verifica se contém APENAS dígitos (sem sinal, sem ponto, sem letras)
    # Isso já barra números negativos (-5), decimais (5.5) e letras (abc)
    if not texto_limpo.isdigit():
        return None, "Digite apenas números inteiros positivos (ex: 100, 50, 287)."
    
    # Converte para inteiro
    valor = int(texto_limpo)
    
    # Verifica se é maior que zero (ninguém saca R$ 0)
    if valor == 0:
        return None, "O valor do saque deve ser maior que zero."
    
    # Se passou por todas as validações, retorna o valor e nenhum erro
    return valor, None


# -------------------------------------------------
# 2. PROGRAMA PRINCIPAL
# -------------------------------------------------
print("="*50)
print("          CAIXA ELETRÔNICO - SIMULADOR")
print("="*50)
print("Cédulas disponíveis: R$ 100, R$ 50, R$ 20, R$ 10, R$ 5, R$ 2\n")

# --- 2.1 COLETA E VALIDAÇÃO DO VALOR ---
while True:
    valor_str = input("Digite o valor para saque (R$): ")
    valor, erro = validar_numero(valor_str)
    
    if erro:
        print(f"Erro: {erro}. Tente novamente.\n")
        continue  # Volta para o início do loop
    
    # Se não tem erro, sai do loop
    break

# --- 2.2 PROCESSAMENTO DAS CÉDULAS ---
# Inicializa a variável que vai guardar o valor restante a cada passo
resto = valor

# Cédulas de R$ 100
cedulas_100 = resto // 100
resto = resto % 100

# Cédulas de R$ 50
cedulas_50 = resto // 50
resto = resto % 50

# Cédulas de R$ 20
cedulas_20 = resto // 20
resto = resto % 20

# Cédulas de R$ 10
cedulas_10 = resto // 10
resto = resto % 10

# Cédulas de R$ 5
cedulas_5 = resto // 5
resto = resto % 5

# Cédulas de R$ 2
cedulas_2 = resto // 2
resto = resto % 2

# --- 2.3 EXIBIÇÃO DOS RESULTADOS ---
print("\n" + "="*50)
print("           RESULTADO DO SAQUE")
print("="*50)

# Contador para verificar se pelo menos uma cédula foi entregue
alguma_cedula = False

if cedulas_100 > 0:
    print(f"  {cedulas_100} cédula(s) de R$ 100")
    alguma_cedula = True

if cedulas_50 > 0:
    print(f"  {cedulas_50} cédula(s) de R$ 50")
    alguma_cedula = True

if cedulas_20 > 0:
    print(f"  {cedulas_20} cédula(s) de R$ 20")
    alguma_cedula = True

if cedulas_10 > 0:
    print(f"  {cedulas_10} cédula(s) de R$ 10")
    alguma_cedula = True

if cedulas_5 > 0:
    print(f"  {cedulas_5} cédula(s) de R$ 5")
    alguma_cedula = True

if cedulas_2 > 0:
    print(f"  {cedulas_2} cédula(s) de R$ 2")
    alguma_cedula = True

# Se nenhuma cédula foi entregue (ex: valor = 1, que não pode ser sacado)
if not alguma_cedula:
    print("  Nenhuma cédula disponível para este valor.")

# --- 2.4 TRATAMENTO DO RESTO NÃO SACÁVEL ---
if resto > 0:
    print("\n" + "-"*50)
    print(f"⚠️  ATENÇÃO: Restante não sacável: R$ {resto},00")
    print("   O caixa eletrônico não possui cédulas para este valor.")
    print("   Sugestão: Saque um valor múltiplo de R$ 2.")
else:
    print("\n" + "-"*50)
    print("✅ Saque realizado com sucesso! Retire seu dinheiro.")

print("="*50)