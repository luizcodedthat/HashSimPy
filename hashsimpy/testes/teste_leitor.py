from ..leitor import ler_arquivo

def test_ler_arquivo(caminho_tmp):
    caminho_teste = caminho_tmp / "exemplo.txt"
    caminho_teste.write_text("Teste de leitura")
    assert ler_arquivo(caminho_teste) == "Teste de leitura"
