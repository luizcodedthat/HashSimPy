import argparse
from .leitor import ler_arquivo
from .pre_processador import preprocessar_texto
from .shingles import gerar_shingles
from .minhash import calcular_assinatura_minhash
from .comparador import similaridade_jaccard, similaridade_exata


def main():
    parser = argparse.ArgumentParser(
        description="Compara dois documentos de texto (Jaccard exata + MinHash)."
    )
    parser.add_argument("arquivo1", help="Caminho para o primeiro arquivo de texto")
    parser.add_argument("arquivo2", help="Caminho para o segundo arquivo de texto")
    args = parser.parse_args()

    texto1 = preprocessar_texto(ler_arquivo(args.arquivo1))
    texto2 = preprocessar_texto(ler_arquivo(args.arquivo2))
    print("[✓] Arquivos lidos e pré-processados.")

    shingles1 = gerar_shingles(texto1)
    shingles2 = gerar_shingles(texto2)
    print("[✓] Shingles gerados (k=5).")

    jaccard_exata = similaridade_exata(shingles1, shingles2)

    assinatura1 = calcular_assinatura_minhash(shingles1)
    assinatura2 = calcular_assinatura_minhash(shingles2)
    print("[✓] Assinaturas MinHash calculadas.")

    minhash_estimate = similaridade_jaccard(assinatura1, assinatura2)

    print("[✓] Comparação final:\n")

    largura = 50
    print("=" * largura)
    print(" COMPARAÇÃO DE DOCUMENTOS ".center(largura, "="))
    print("=" * largura + "\n")

    print(f"{'Método':<30}{'Similaridade':>20}")
    print("-" * largura)
    print(f"{'Jaccard exata':<30}{jaccard_exata:>19.2%}")
    print(f"{'Estimativa MinHash':<30}{minhash_estimate:>19.2%}")
    print("\n" + "=" * largura + "\n")


if __name__ == "__main__":
    main()
