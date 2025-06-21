from pre_processador import ler_arquivo, preprocessar_texto
from shingles import gerar_shingles
from minhash import MinHash
from comparador import calcular_similaridade_jaccard

def pipeline_similaridade(caminho1, caminho2, k=3, num_hashes=100):
    # Leitura e pré-processamento
    texto1 = preprocessar_texto(ler_arquivo(caminho1))
    texto2 = preprocessar_texto(ler_arquivo(caminho2))

    # Geração dos shingles
    shingles1 = gerar_shingles(texto1, k)
    shingles2 = gerar_shingles(texto2, k)

    # Aplicação do MinHash
    minhash = MinHash(num_hashes)
    assinatura1 = minhash.gerar_assinatura(shingles1)
    assinatura2 = minhash.gerar_assinatura(shingles2)

    # Comparação de similaridade
    similaridade = calcular_similaridade_jaccard(assinatura1, assinatura2)
    return similaridade


if __name__ == "__main__":
    # Exemplo simples (substituir pelos caminhos dos arquivos reais)
    doc1 = "documento1.txt"
    doc2 = "documento2.txt"
    
    similaridade = pipeline_similaridade(doc1, doc2)
    print(f"Similaridade estimada entre os documentos: {similaridade:.2f}")