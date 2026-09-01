# classificador_idade.py
# Classifica uma pessoa por idade e verifica direitos (votar e dirigir)

# -------------------------------------------------
# 1. CONSTANTES (facilita manutenção)
# -------------------------------------------------
IDADE_MINIMA_VOTO = 16
IDADE_MINIMA_DIRECAO = 18
IDADE_IDOSO = 60

# -------------------------------------------------
# 2. FUNÇÃO PARA VALIDAR NÚMERO INTEIRO (>= 0)
# -------------------------------------------------
def validar_idade(texto):
    """
    Valida se o texto pode ser convertido em um número inteiro >= 0.
    Retorna (valor, erro) onde 'erro' é None se a validação for bem-sucedida.
    """
    texto_limpo = texto.strip()
    
    if texto_limpo == "":
        return None, "Valor não pode estar vazio."
    
    # Verifica se contém APENAS dígitos (sem sinal, sem ponto, sem letras)
    if not texto_limpo.isdigit():
        return None, "Digite apenas números inteiros (sem ponto, sem sinal)."
    
    valor = int(texto_limpo)
    
    # Qualquer inteiro >= 0 é aceito (0 é válido para recém-nascido)
    if valor < 0:
        return None, "A idade não pode ser negativa."
    
    return valor, None


# -------------------------------------------------
# 3. PROGRAMA PRINCIPAL
# -------------------------------------------------
print("="*50)
print("          CLASSIFICADOR DE IDADE")
print("="*50)
print("Classifica a pessoa em Recém-nascido, Criança, Adolescente, Adulto ou Idoso.")
print("Também verifica direito a voto e direção.\n")

# --- 3.1 COLETA E VALIDAÇÃO DA IDADE ---
while True:
    idade_str = input("Digite sua idade: ")
    idade, erro = validar_idade(idade_str)
    
    if erro:
        print(f"Erro: {erro}. Tente novamente.\n")
        continue
    
    break

# --- 3.2 CLASSIFICAÇÃO POR FAIXA ETÁRIA ---
if idade == 0:
    categoria = "Recém-nascido"
elif idade <= 12:
    categoria = "Criança"
elif idade <= 17:
    categoria = "Adolescente"
elif idade < IDADE_IDOSO:  # 18 a 59
    categoria = "Adulto"
else:  # idade >= 60
    categoria = "Idoso"

# --- 3.3 VERIFICAÇÃO DE DIREITOS ---
pode_votar = idade >= IDADE_MINIMA_VOTO
pode_dirigir = idade >= IDADE_MINIMA_DIRECAO

# --- 3.4 EXIBIÇÃO DO RELATÓRIO ---
print("\n" + "="*50)
print("           RELATÓRIO DO USUÁRIO")
print("="*50)

print(f"Idade informada: {idade} anos")
print(f"Classificação: {categoria}")

print("\n--- DIREITOS ---")
print(f"Pode votar? {'Sim' if pode_votar else 'Não'} (idade >= {IDADE_MINIMA_VOTO})")
print(f"Pode dirigir? {'Sim' if pode_dirigir else 'Não'} (idade >= {IDADE_MINIMA_DIRECAO})")

# --- 3.5 ANÁLISE ADICIONAL (OPERADORES LÓGICOS) ---
maior_e_pode_dirigir = (idade >= IDADE_MINIMA_DIRECAO) and pode_dirigir
print(f"\nÉ maior de idade E pode dirigir? {maior_e_pode_dirigir}")

# Usando 'or' para faixa jovem (reutilizando a categoria)
eh_jovem = categoria in ("Criança", "Adolescente", "Recém-nascido")
print(f"Pertence à faixa jovem (até 17 anos)? {eh_jovem}")

# Usando 'not' para inverter
nao_pode_votar = not pode_votar
print(f"NÃO pode votar? {nao_pode_votar}")

print("="*50)