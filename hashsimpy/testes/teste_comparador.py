from ..comparador import similaridade_jaccard

def test_similaridade_jaccard():
    assinatura1 = [1, 2, 3, 4, 5]
    assinatura2 = [1, 2, 0, 4, 0]
    assert similaridade_jaccard(assinatura1, assinatura2) == 3/5
