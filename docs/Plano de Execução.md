# HashSimPy: Conceitos, Arquitetura e Decisões

## 1. Conceitos Fundamentais

### 1.1 Hashing

- **Definição**: Processo de aplicar uma função hash a dados de tamanho arbitrário, gerando um valor de tamanho fixo (digest).
- **Propriedades:** determinístico; avalanche(); uniformidade; colisões possíveis.
- **Uso no HashSimPy:** converter shingles (cadeias de caracteres) em inteiros para indexação eficiente.
- **Exemplo em Python:**
  ```python
  import hashlib
  def hash_shingle(shingle: str) -> int:
      return int(hashlib.sha1(shingle.encode('utf-8')).hexdigest(), 16)
  ```

### 1.2 Shingling

- **Definição**: Técnica para gerar “k-shingles”, que são sequências de k tokens (caracteres ou palavras) sobrepostas.
- **Objetivo**: Capturar a ordem local de tokens e transformar texto em conjuntos.
- **Impacto de k**:
  - k pequeno: mais sensível a coincidências pontuais; conjuntos maiores; mais falsos positivos.
  - k grande: mais seletivo; detecta apenas correspondências exatas maiores; conjuntos menores.
- **Exemplo em Python** (shingles de palavras):
  ```python
  def gerar_shingles(texto: str, k: int) -> set[str]:
      tokens = texto.split()
      return {" ".join(tokens[i:i+k]) for i in range(len(tokens)-k+1)}
  ```

### 1.3 Índice de Jaccard

- **Fórmula:** \(J(A,B) = \frac{|A \cap B|}{|A \cup B|}\)
- **Intervalo:** 0 (sem sobreposição) a 1 (conjuntos idênticos).
- **Uso:** medir similaridade entre conjuntos de shingles de dois documentos.
- **Implementação simples:**
  ```python
  def jaccard(A: set, B: set) -> float:
      return len(A & B) / len(A | B)
  ```

### 1.4 MinHashing

- **Motivação:** aproximar o Jaccard de forma eficiente em conjuntos grandes.
- **Passos principais:**
  1. Definir k funções hash independentes (e.g., h\_i(x) = (a\_i \* x + b\_i) mod p).
  2. Para cada documento, calcular a **assinatura**: vetor dos mínimos hashes de cada função sobre seus shingles.
  3. Estimar Jaccard como a fração de componentes iguais entre duas assinaturas.
- **Vantagem:** reduz custo de comparação de O(|Shingles|) para O(k).
- **Exemplo de geração de assinaturas:**
  ```python
  import random
  P = 4294967311
  def gerar_funcoes_hash(k: int) -> list[callable]:
      funcs = []
      for _ in range(k):
          a, b = random.randint(1, P-1), random.randint(0, P-1)
          funcs.append(lambda x, a=a, b=b: (a*x + b) % P)
      return funcs

  def assinatura_minhash(shingles: set[int], hash_funcs: list[callable]) -> list[int]:
      return [min(h(s) for s in shingles) for h in hash_funcs]
  ```

## 2. Arquitetura do Sistema

```
hashsimpy/
├── leitor.py           # Funções para carregar arquivos .txt
├── pre_processador.py  # Normalização (lowercase, remoção de pontuação/números)
├── shingles.py         # Geração de k-shingles
├── minhash.py          # Geração de funções hash e assinaturas
├── comparador.py       # Cálculo de similaridade (Jaccard e MinHash)
└── cli.py              # Interface de linha de comando (argparse)
```

- **Módulos independentes:** facilitam testes unitários e manutenção.
- **Fluxo de execução:**
  1. CLI recebe caminhos de arquivos.
  2. `leitor.py` carrega o texto bruto.
  3. `pre_processador.py` normaliza e limpa o texto.
  4. `shingles.py` gera conjuntos de shingles.
  5. `minhash.py` cria assinaturas MinHash.
  6. `comparador.py` compara assinaturas e/ou calcula Jaccard.
  7. CLI exibe resultado formatado.

## 3. Decisões de Implementação

| Decisão                      | Impacto na Ferramenta                                          |
| ---------------------------- | -------------------------------------------------------------- |
| Tamanho do shingle (5)       | Granularidade da similaridade; velocidade vs. sensibilidade.   |
| Nº de funções hash (100)    | Precisão da estimação MinHash vs. custo computacional.         |
| Uso de `hashlib`             | Funções hash confiáveis; evita colisões frequentes.            |
| Modularização por arquivo    | Organização, legibilidade, testes unitários e extensibilidade. |
| `argparse` na CLI            | Uso padronizado e robusto de argumentos na linha de comando.   |
| Remoção de pontuação/números | Evita ruído; foca apenas em tokens alfabéticos significativos. |

**Resumo dos trade-offs:**

- **k menor** + **k' menor**: mais rápido, porém menos preciso.
- **k maior** + **k' maior**: mais preciso, porém consome mais tempo e memória.
