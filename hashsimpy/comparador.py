def similaridade_jaccard(assinatura1, assinatura2):

    if len(assinatura1) != len(assinatura2):
        raise ValueError("Assinaturas de tamanhos diferentes.")

    iguais = sum(1 for a, b in zip(assinatura1, assinatura2) if a == b)
    return iguais / len(assinatura1)