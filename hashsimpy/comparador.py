def similaridade_jaccard(assinatura1: list[int], assinatura2: list[int]) -> float:
    """
    Calcula a similaridade de Jaccard entre duas assinaturas MinHash.

    Args:
        assinatura1 (list[int]): Lista de valores inteiros da assinatura MinHash do primeiro documento.
        assinatura2 (list[int]): Lista de valores inteiros da assinatura MinHash do segundo documento.

    Returns:
        float: Estimativa da similaridade de Jaccard, dado pela fração de hashes iguais.

    Raises:
        ValueError: Se as duas assinaturas tiverem tamanhos diferentes.
    """
    if len(assinatura1) != len(assinatura2):
        raise ValueError("Assinaturas de tamanhos diferentes.")

    iguais = sum(1 for a, b in zip(assinatura1, assinatura2) if a == b)
    return iguais / len(assinatura1)


def similaridade_exata(shingles1: set[str], shingles2: set[str]) -> float:
    """
    Calcula a similaridade exata de Jaccard entre dois conjuntos de shingles.

    A fórmula utilizada é:
        J(S1, S2) = |S1 ∩ S2| / |S1 ∪ S2|

    Args:
        shingles1 (set[str]): Conjunto de shingles do primeiro documento.
        shingles2 (set[str]): Conjunto de shingles do segundo documento.

    Returns:
        float: Valor exato da similaridade de Jaccard. Retorna 0.0 se ambos os conjuntos estiverem vazios.
    """
    intersecao = shingles1.intersection(shingles2)
    uniao = shingles1.union(shingles2)
    if not uniao:
        return 0.0
    return len(intersecao) / len(uniao)
