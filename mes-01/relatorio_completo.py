# relatorio_completo.py
# Coleta dados pessoais com validação e exibe relatório formatado.

# 1. Validação de nome (não pode estar vazio)
nome = input("Digite seu nome: ").strip()
while nome == "":
    print("Nome não pode estar vazio.")
    nome = input("Digite seu nome: ").strip()

# 2. Validação de idade (deve ser um número inteiro positivo)
idade_str = input("Digite sua idade: ").strip()
while True:
    if idade_str.isdigit():  # Verifica se contém apenas dígitos
        idade = int(idade_str)
        if idade > 0:
            break
        else:
            print("Idade deve ser um número positivo.")
    else:
        print("Idade deve ser um número inteiro.")
    idade_str = input("Digite sua idade: ").strip()

# 3. Validação de altura (deve ser um número decimal positivo)
altura_str = input("Digite sua altura em metros (ex: 1.75): ").strip()
while True:
    # Verifica se é um número válido (permite ponto decimal)
    if altura_str.count('.') <= 1:
        parte_numerica = altura_str.replace('.', '')
        if parte_numerica.isdigit() and altura_str != "":
            altura = float(altura_str)
            if altura > 0:
                break
            else:
                print("Altura deve ser um número positivo.")
        else:
            print("Altura deve ser um número válido (ex: 1.75).")
    else:
        print("Altura deve ter apenas um ponto decimal.")
    altura_str = input("Digite sua altura em metros: ").strip()

# 4. Validação de estudante (sim/não)
estudante_str = input("É estudante? (sim/não): ").strip().lower()
while estudante_str not in ["sim", "não", "nao"]:
    print("Resposta inválida. Digite 'sim' ou 'não'.")
    estudante_str = input("É estudante? (sim/não): ").strip().lower()
eh_estudante = estudante_str == "sim"

# 5. Cálculo do IMC (índice de massa corporal)
imc = idade / (altura ** 2)  # Fórmula didática, não clínica

# 6. Exibição do relatório
print("\n" + "="*40)
print("RELATÓRIO COMPLETO DO USUÁRIO")
print("="*40)
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print(f"Altura: {altura:.2f} m")
print(f"Estudante: {'Sim' if eh_estudante else 'Não'}")
print(f"IMC (fórmula didática): {imc:.2f}")
print(f"Tipo de cada campo:")
print(f"  - nome: {type(nome).__name__}")
print(f"  - idade: {type(idade).__name__}")
print(f"  - altura: {type(altura).__name__}")
print(f"  - estudante: {type(eh_estudante).__name__}")
print("="*40)