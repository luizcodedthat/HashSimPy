import hashlib

# Número de funções hash simuladas (semente)
NUMERO_HASHES = 100

def hash_shingles(shingle: str, semente: int) -> int:
    """
    Gera um valor hash inteiro a partir de um n-grama e uma semente.
    
    Args:
        shingle (str): O shingle a ser hasheado.
        semente (int): Um número usado como variação (para simular múltiplas funções hash).

    Returns:
        int: Valor hash como inteiro.
    """
    entrada = (shingle + str(semente)).encode('utf-8')
    hash_md5 = hashlib.md5(entrada).hexdigest()
    return int(hash_md5, 16)


def calcular_assinatura_minhash(conjunto_shingles: set[str]) -> list[int]:
    """
    Calcula a assinatura MinHash de um conjunto de shingles.

    Args:
        conjunto_shingles (set[str]): Conjunto de shingles extraídos de um texto.

    Returns:
        list[int]: Lista com a assinatura MinHash.
    """
    assinatura = []

    for semente in range(NUMERO_HASHES):
        menor_hash = min(hash_shingles(shingle, semente) for shingle in conjunto_shingles)
        assinatura.append(menor_hash)

    return assinatura
