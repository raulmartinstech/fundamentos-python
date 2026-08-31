# conversor_temperatura.py
# Conversor de temperaturas com validação robusta

# -------------------------------------------------
# 1. FUNÇÃO PARA VALIDAR TEMPERATURA (Número)
# -------------------------------------------------
def validar_temperatura(texto):
    # Remove espaços das bordas
    texto_limpo = texto.strip()
    
    # Verifica se está vazio
    if texto_limpo == "":
        return None, "Temperatura não pode estar vazia."
    
    # --- TRATAMENTO PARA NÚMEROS NEGATIVOS ---
    # Remove o sinal de menos (se houver) APENAS para a verificação
    # Ex: "-5.5" vira "5.5" para testar; "5.5" continua "5.5"
    texto_sem_sinal = texto_limpo.lstrip('-')
    
    # Se depois de remover o sinal ficou vazio (ex: usuário digitou apenas "-")
    if texto_sem_sinal == "":
        return None, "Número inválido (apenas sinal?)."
    
    # Verifica se há no máximo um ponto decimal
    if texto_sem_sinal.count('.') <= 1:
        # Remove os pontos TEMPORARIAMENTE para testar se o resto são dígitos
        parte_numerica = texto_sem_sinal.replace('.', '')
        if parte_numerica.isdigit():
            # Se passou, converte o texto ORIGINAL (com o sinal, se tiver)
            # Se houver ponto, converte para float; senão, para int
            if '.' in texto_sem_sinal:
                return float(texto_limpo), None
            else:
                return int(texto_limpo), None
    
    # Se chegou até aqui, algo deu errado
    return None, "Número inválido. Use apenas números e um ponto decimal (ex: -5.5 ou 25)."

# -------------------------------------------------
# 2. FUNÇÃO PARA VALIDAR UNIDADE (C ou F)
# -------------------------------------------------
def validar_unidade(texto):
    # Remove espaços e converte para maiúsculo
    texto_limpo = texto.strip().upper()
    
    if texto_limpo == "":
        return None, "Unidade não pode estar vazia."
    
    if texto_limpo in ["C", "F"]:
        return texto_limpo, None
    else:
        return None, f"Unidade '{texto_limpo}' inválida. Digite C ou F."

# -------------------------------------------------
# 3. PROGRAMA PRINCIPAL
# -------------------------------------------------

# --- VALIDAÇÃO DA TEMPERATURA ---
while True:
    temp_str = input("Digite a temperatura: ")
    temperatura, erro = validar_temperatura(temp_str)
    if erro:
        print(f"Erro: {erro}. Tente novamente.")
        continue
    break

# --- VALIDAÇÃO DA UNIDADE DE ORIGEM ---
while True:
    origem_str = input("Digite a unidade de origem (C ou F): ")
    origem, erro = validar_unidade(origem_str)
    if erro:
        print(f"Erro: {erro}. Tente novamente.")
        continue
    break

# --- VALIDAÇÃO DA UNIDADE DE DESTINO ---
while True:
    destino_str = input("Digite a unidade de destino (C ou F): ")
    destino, erro = validar_unidade(destino_str)
    if erro:
        print(f"Erro: {erro}. Tente novamente.")
        continue
    break

# --- CÁLCULO E EXIBIÇÃO ---
print("\n" + "="*40)
print("RESULTADO DA CONVERSÃO")
print("="*40)

if origem == destino:
    print(f"A temperatura permanece a mesma: {temperatura:.2f}°{origem}")

elif origem == "C" and destino == "F":
    resultado = (temperatura * 9/5) + 32
    print(f"{temperatura:.2f}°C equivale a {resultado:.2f}°F")

elif origem == "F" and destino == "C":
    resultado = (temperatura - 32) * 5/9
    print(f"{temperatura:.2f}°F equivale a {resultado:.2f}°C")

# Esta linha nunca deve ser alcançada, mas é uma segurança
else:
    print("Erro inesperado: combinação de unidades inválida.")

print("="*40)