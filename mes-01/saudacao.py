# saudacao.py - primeiro programa de Raul Martins.
# Esse arquivo demostra o uso da entrada (imput) e saída (print).

# 1. A função input () exibe uma mensagem no terminal e aguarda o usúario digita algo + Enter.
# O que for digitado é retornado como string (texto) e armazenado na variável "nome".
nome = input ("Qual é o seu nome? ")

# 2. Novamente usamos input(), mas agora quremos um número.
# A entrada do input() sempre é string. Para tratar como número, usamos int() para converter.

idade = int(input("Qual é a sua idade?" )) # Conversão explícita de string para inteiro.

# 3. Definimos o ano atual como constante (valor fixo do programa).
ano_atual = 2026

# 4. Cálculo aritmético simples.
ano_nascimento = ano_atual - idade 

# 5. A função print() exibe as informações no terminal.
# Usamos f-string (string formatada) com o prefixo "f" para inserir variáveis diretamente.
print(f"Olá, {nome}! Você nasceu aproximadamente em {ano_nascimento}.")



