import pandas as pd

def testar_estrategia(dados):
    """
    Teste de estratégia com médias móveis.
    Os dados devem conter as colunas:
    'close' (preço de fechamento).
    """
    dados = dados.copy()

    dados["media_9"] = dados["close"].rolling(9).mean()
    dados["media_21"] = dados["close"].rolling(21).mean()

    dados["sinal"] = 0

    compra = (
        (dados["media_9"] > dados["media_21"]) &
        (dados["media_9"].shift(1) <= dados["media_21"].shift(1))
    )

    venda = (
        (dados["media_9"] < dados["media_21"]) &
        (dados["media_9"].shift(1) >= dados["media_21"].shift(1))
    )

    dados.loc[compra, "sinal"] = 1
    dados.loc[venda, "sinal"] = -1

    return dados


if __name__ == "__main__":
    print("Robô Forex: módulo de teste preparado.")
    print("Estratégia: cruzamento de médias móveis 9 e 21.")
    print("Modo: simulação, sem operações reais.")
