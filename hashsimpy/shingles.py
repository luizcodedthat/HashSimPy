def gerar_shingles(texto: str, k: int = 5) -> set:
    """
    Gera um conjunto de shingles (substrings consecutivas) a partir do texto.

    Args:
        texto (str): Texto pré-processado.
        k (int): Tamanho dos shingles.

    Returns:
        set: Conjunto de shingles únicos.
    """
    if len(texto) < k:
        return set()

    return set(texto[i:i+k] for i in range(len(texto) - k + 1))