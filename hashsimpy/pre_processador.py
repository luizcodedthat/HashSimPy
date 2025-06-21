import re

def preprocessar_texto(texto: str) -> str:
    """
    Realiza o pré-processamento de um texto para preparação de análise de similaridade.

    As etapas incluem:
    1. Conversão para minúsculas.
    2. Remoção de pontuação e dígitos, mantendo apenas letras (a–z) e espaços.
    3. Normalização de espaços em branco, reduzindo múltiplos espaços a um único espaço.

    Args:
        texto (str): Texto bruto de entrada.

    Returns:
        str: Texto pré-processado, com apenas letras minúsculas e espaços simples, sem pontuação ou números.
    """
    texto = texto.lower()
    texto = re.sub(r'[^a-z\s]', '', texto) # Remove tudo que não for letra a–z ou espaço
    texto = re.sub(r'\s+', ' ', texto) # Substitui múltiplos espaços por somente um
    return texto.strip()
