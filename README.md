
# 🧠 HASHSIMPY – Comparador de Similaridade de Textos com MinHash

Projeto para identificar a **similaridade entre documentos de texto (.txt)** utilizando as técnicas de **Shingling**, **MinHashing** e **Jaccard Similarity**. A interface é feita via linha de comando (CLI), e os módulos são organizados de forma limpa e modular em Python.

---

## 📁 Estrutura do Projeto

```
HASHSIMPY/
│
├── assets/                  # Textos de entrada (.txt)
│   ├── poema1.txt
│   ├── poema2.txt
│   └── ...
│
├── docs/                    # Documentação e imagens
│
├── hashsimpy/               # Pacote principal
│   ├── cli.py               # Interface de linha de comando
│   ├── leitor.py            # Leitura de arquivos
│   ├── pre_processador.py   # Limpeza e normalização dos textos
│   ├── shingles.py          # Geração de shingles 
│   ├── minhash.py           # MinHashing
│   ├── comparador.py        # Comparação Jaccard e MinHash
│   ├── testes/              # Testes manuais e automatizados
│   └── __init__.py
│
├── .gitignore
└── README.md
```

---

## 👨‍💻 Como Usar

1. **Rode a ferramenta na linha de comando**:

```bash
python -m hashsimpy assets/poema1.txt assets/poema3.txt
```

---

## 💡 Exemplo de Saída

```
> python -m hashsimpy.cli assets/poema1.txt assets/poema2.txt

[✓] Arquivos lidos e pré-processados.
[✓] Shingles gerados (k=5).
[✓] Assinaturas MinHash calculadas.
[✓] Comparação final:

==================================================
============== COMPARAÇÃO DE DOCUMENTOS ==========
==================================================

Método                          Similaridade
--------------------------------------------------
Jaccard exata                       75.00%
Estimativa MinHash                  72.00%

==================================================

```

---

## 📌 Técnicas Utilizadas

- **Shingling**: Quebra de texto em substrings consecutivas
- **Jaccard Similarity**: Índice de interseção entre conjuntos
- **MinHashing**: Estimativa rápida da similaridade entre grandes conjuntos
- **CLI com `argparse`**: Interface para facilitar o uso no terminal

---

## 👥 Equipe

| Pessoa | Responsável por |
|--------|------------------|
| Pessoa A (Carol Silva)| Leitura de arquivos, pré-processamento e CLI |
| Pessoa B (Lucas Gomes) | Geração de shingles e README |
| Pessoa C (Luiz Eduardo) | MinHashing e apresentação |
| Pessoa D (Pedro/MarcaPasso) | Comparação, integração dos módulos e fluxo final |

---

## ✅ Tarefas Concluídas

- [x] Leitura e limpeza de arquivos
- [x] Geração de shingles 
- [x] Implementação do MinHash
- [x] Comparação com Jaccard e assinatura
- [x] Interface CLI funcional
- [x] Testes manuais
- [x] Organização do repositório no GitHub
- [x] Documentação

---


