import yfinance


def extrai_dados(ticker, start_date, end_date):

    caminho = f"/home/alura/Documents/Financeiro/test/csv/{ticker}.csv"
    hist = yfinance.Ticker(ticker).history(
        period="1d",
        interval="1h",
        start=start_date,
        end=end_date,
        prepost=True
    ).to_csv(caminho)


extrai_dados("AAPL", '2023-01-03', '2023-01-10')
extrai_dados("GOOG", '2023-01-03', '2023-01-10')
