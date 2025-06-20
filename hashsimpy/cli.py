import argparse
from .leitor import ler_arquivo
from .pre_processador import preprocessar_texto
from .shingles import gerar_shingles
from .minhash import calcular_assinatura_minhash
from .comparador import similaridade_jaccard


def main():
    parser = argparse.ArgumentParser(description="Verifica similaridade entre dois documentos de texto.")
    parser.add_argument("arquivo1", help="Caminho para o primeiro arquivo de texto")
    parser.add_argument("arquivo2", help="Caminho para o segundo arquivo de texto")
    argumentos = parser.parse_args()

    texto1 = preprocessar_texto(ler_arquivo(argumentos.arquivo1))
    texto2 = preprocessar_texto(ler_arquivo(argumentos.arquivo2))

    shingles1 = gerar_shingles(texto1)
    shingles2 = gerar_shingles(texto2)

    assinatura1 = calcular_assinatura_minhash(shingles1)
    assinatura2 = calcular_assinatura_minhash(shingles2)

    similaridade = similaridade_jaccard(assinatura1, assinatura2)
    print(f"Similaridade estimada: {similaridade:.2f}")
