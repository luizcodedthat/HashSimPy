import re

def ler_arquivo_txt(caminho):
    """Lê um arquivo .txt e retorna seu conteúdo como uma string."""
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        return arquivo.read()

def preprocessar_texto(texto):
    """
    Aplica pré-processamento:
    - Converte para minúsculas
    - Remove pontuação e números usando regex
    """
    texto = texto.lower()
    texto = re.sub(r'[^a-z\s]', '', texto)  # Mantém apenas letras e espaços
    texto = re.sub(r'\s+', ' ', texto)      # Remove espaços duplicados
    return texto.strip()

def gerar_shingles(texto, k=3):
    """
    Gera conjuntos de shingles de tamanho k a partir do texto.
    Cada shingle é uma sequência de k caracteres consecutivos.
    """
    return {texto[i:i+k] for i in range(len(texto) - k + 1)}

# Exemplo de uso para testes manuais
if __name__ == "__main__":
    caminho = "examples/exemplo1.txt"  # ou exemplo2.txt / exemplo3.txt
    texto = ler_arquivo_txt(caminho)
    texto_processado = preprocessar_texto(texto)
    shingles = gerar_shingles(texto_processado, k=3)

    print("Texto Original:\n", texto)
    print("\nTexto Processado:\n", texto_processado)
    print("\nShingles (k=3):\n", shingles)

