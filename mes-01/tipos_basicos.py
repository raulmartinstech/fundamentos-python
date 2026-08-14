# tipos_basicos.py
# Demonstração dos tipos primitivos e da função type()

# 1. Atribuição de valores a variáveis
idade = 19                            # int (número inteiro)
altura = 1.75                         # float (número com ponto decimal)
nome = "Raul"                         # str (sequência de caracteres)
estudante = True                      # bool (booleano : True ou False)

# 2. A função type() retorna o tipo da variável.
#    Usamos print() para exibir esse resultado.
print("Tipo de 'idade':", type(idade))
print("Tipo de 'altura':", type(altura))
print("Tipo de 'nome':", type(nome))
print("Tipo de 'estudante':", type(estudante))

# --- Conversões Explícitas ---

# Conversão de float para int: a parte decimal é truncada (cortada),
# não arredondada. Isso é um comportamento importante e intencional.
numero_float = 3.99
numero_int = int(numero_float)

print(f"float 3.99 convertido para int: {numero_int}")  # 3

# Conversão de string númerica para float
# Observe que o ponto decimal é obrigatório para a separação.
valor_str = "19.95" 
valor_float = float(valor_str)
print(f"string '19.95' convertida para float: {valor_float}")  # 19.95

# Conversão de string númerica para int
# Isso só funciona se a string representar um número inteiro.
# Se houver ponto decimal, ocorre um ValuErrror.
idade_str = "25"
idade_int = int(idade_str)
print(f"string '25' convertida para int: {idade_int}")  #25

# --- Conversões para Booleano (bool)

# A função bool() avalia se um valor é "verdadeiro" ou "falso"
# A regra fundamental: valores "vazios" ou "nulos" são False.
# Valores "preenchidos" ou "não-nulos" são True.

print("bool(0):", bool(0))                 # False (zero é falso)
print("bool(1):", bool(1))                 # True (qualquer número diferente de zero é verdadeiro)
print("bool(-5):", bool(-5))               # True (mesmos números negativos são True)
print("bool(0.0):", bool(0.0))             # False (zero float também é falso)
print("bool('0'):", bool("0"))            # True (é uma string com um caractere dento, não está vazia)

print("bool(''):", bool(''))               # False (string vazia é falsa)
print("bool(' '):", bool(' '))             # True (string com espaço é preenchida, então é True)
print("bool('Python'):", bool("Python"))   # True (texto é True)

print("bool(None):", bool(None))           # False (None representa ausêcia de valor)

# ---Atenção: Armadilha clássica! ---
# A string "False" é uma string não vazia, portanto é True.
print("bool('False'):", bool("False"))     # True
