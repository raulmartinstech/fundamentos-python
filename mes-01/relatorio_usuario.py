# relatorio_usuario.py
# Coleta dados do usuário, converte e exibe um relatório formatado.

# 1. Coleta de dados
nome = input("Digite seu nome: ")
idade_texto = input("Digite sua idade: ")
altura_texto = input("Digite sua altura em metros (ex: 1.75): ")
eh_estudante_texto = input("É estudante? (Digite sim ou não): ")

# 2. Conversão de tipos
idade = int(idade_texto)
altura = float(altura_texto)
eh_estudante = eh_estudante_texto.lower() == "sim"

# 3. Exibição do relatório com formatação e uso de type()
print("\n--- RELATÓRIO DO USUÁRIO ---")
print(f"Nome: {nome} (tipo: {type(nome).__name__})")
print(f"Idade: {idade} anos (tipo: {type(idade).__name__})")
print(f"Altura: {altura:.2f} m (tipo: {type(altura).__name__})")
print(f"É estudante: {eh_estudante} (tipo: {type(eh_estudante).__name__})")
print(f"Idade é maior que 18? {idade > 18} (tipo: {type(idade > 18).__name__})")