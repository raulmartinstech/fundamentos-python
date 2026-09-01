# analisador_credito.py
# Sistema de análise de crédito com operadores lógicos

# Função para validar número (já conhecida)
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

# Coleta de dados
print("=== SISTEMA DE ANÁLISE DE CRÉDITO ===\n")

# Idade
while True:
    idade_str = input("Digite sua idade: ")
    idade, erro = validar_numero(idade_str)
    if erro:
        print(f"Erro: {erro}. Tente novamente.")
        continue
    if idade < 0:
        print("Idade não pode ser negativa. Tente novamente.")
        continue
    break

# Renda mensal
while True:
    renda_str = input("Digite sua renda mensal (R$): ")
    renda, erro = validar_numero(renda_str)
    if erro:
        print(f"Erro: {erro}. Tente novamente.")
        continue
    if renda < 0:
        print("Renda não pode ser negativa. Tente novamente.")
        continue
    break

# Pontuação de crédito (score)
while True:
    score_str = input("Digite sua pontuação de crédito (0 a 1000): ")
    score, erro = validar_numero(score_str)
    if erro:
        print(f"Erro: {erro}. Tente novamente.")
        continue
    if not (0 <= score <= 1000):
        print("Pontuação deve estar entre 0 e 1000. Tente novamente.")
        continue
    break

# Validação de dados booleanos (já são)
print("\n" + "="*50)
print("RESULTADO DA ANÁLISE")
print("="*50)

# Critérios individuais (operadores relacionais)
idade_ok = idade >= 18
renda_ok = renda >= 2000
score_ok = score >= 700

print(f"Idade ok (>= 18)? {idade_ok}")
print(f"Renda ok (>= R$ 2000)? {renda_ok}")
print(f"Score ok (>= 700)? {score_ok}")

# Combinação com operadores lógicos
aprovado = idade_ok and renda_ok and score_ok

# Aprovação com regras alternativas (or)
aprovado_com_garantia = (renda_ok and score_ok) or (renda >= 5000)

print("\n--- DECISÃO ---")
print(f"Aprovado? {aprovado}")

if aprovado:
    print("Parabéns! Seu crédito foi aprovado.")
else:
    print("Infelizmente, seu crédito não foi aprovado.")
    
    # Mensagem específica para orientar o usuário
    if not idade_ok:
        print("Motivo: Idade inferior a 18 anos.")
    elif not renda_ok:
        print("Motivo: Renda inferior a R$ 2.000.")
    elif not score_ok:
        print("Motivo: Pontuação de crédito inferior a 700.")
    else:
        print("Motivo: Não se enquadra nos critérios.")

print("="*50)