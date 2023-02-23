import yfinance

hist = yfinance.Ticker("AAPL").history(
    period="1d",
    interval="1h",
    start="2022-02-01",
    end="2022-02-03",
    prepost=True
)

print(hist.head())
