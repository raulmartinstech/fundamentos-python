### 1. `saudacao.py` — Primeiros passos com entrada e saída
**Objetivo:** Demonstrar o uso de `print()`, `input()` e conversão de tipos.

- Solicita o nome e a idade do usuário.
- Converte a idade (string) para inteiro com `int()`.
- Calcula o ano de nascimento com base no ano atual (2026).
- Exibe uma saudação personalizada.

**Exemplo de execução:**
```

Qual é o seu nome? Raul
Qual é a sua idade? 19
Olá, Raul! Você nasceu aproximadamente em 2007.

```

---

### 2. `medias.py` — Cálculo de média com lógica de aprovação
**Objetivo:** Trabalhar com números decimais (`float`), operações aritméticas e estruturas condicionais (`if`, `elif`, `else`).

- Solicita três notas do aluno (valores decimais).
- Calcula a média aritmética.
- Classifica o status do aluno conforme a tabela abaixo:

| Média | Status |
| :--- | :--- |
| ≥ 7.0 | Aprovado |
| ≥ 5.0 | Recuperação |
| < 5.0 | Reprovado |

- Exibe o resultado com formatação de 2 casas decimais (`:.2f`).

**Exemplo de execução:**
```

Digite a primeira nota: 8.5
Digite a segunda nota: 6.0
Digite a terceira nota: 7.0
A média final do aluno é 7.17. Status: Recuperação.

```

---

### 3. `investimento.py` — Calculadora de Juros Compostos
**Objetivo:** Aplicar operadores aritméticos, exponenciação (`**`) e formatação de saída em um contexto financeiro.

- Solicita o capital inicial, a taxa de juros mensal (em percentual) e o número de meses.
- Calcula o montante final usando a fórmula:
  
  \[
  M = C * (1 + i/100) ** t
  \]
  
  Onde:
  - `M` = Montante final
  - `C` = Capital inicial
  - `i` = Taxa de juros mensal (%)
  - `t` = Número de meses

- Exibe o resultado formatado com duas casas decimais.

**Exemplo de execução:**
```

Capital inicial: R$ 1000.00
Taxa mensal: 5.0%
Meses: 12
Montante final: R$ 1795.86

```

---

## 🛠️ Tecnologias Utilizadas
- **Python 3.12+** — Linguagem de programação.
- **Git e GitHub** — Controle de versão e repositório remoto.

---

## 💡 Aprendizados Consolidados

- Configuração do ambiente de desenvolvimento (VS Code + extensões).
- Uso das funções `print()` (saída) e `input()` (entrada).
- Conversão explícita de tipos: `int()` e `float()`.
- Operadores aritméticos básicos e exponenciação (`**`).
- Estruturas condicionais (`if`, `elif`, `else`) para tomada de decisão.
- Formatação de strings com f-strings e especificadores de formato (`:.2f`).
- Inicialização de repositório Git e commits semânticos (`feat:`, `docs:`).
- Envio de código para o GitHub com `git push`.

---

## ▶️ Como Executar os Projetos

1. Certifique-se de ter o Python 3.12+ instalado.
2. Clone este repositório ou baixe os arquivos.
3. No terminal, navegue até a pasta `mes-01`.
4. Execute o programa desejado:

```bash
python saudacao.py
python medias.py
python investimento.py
```

---

Autor: Raul Martins
Data: Agosto de 2026

```