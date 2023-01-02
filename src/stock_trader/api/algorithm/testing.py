# import necessary libraries
import pandas as pd
import yfinance as yf

nvda = yf.Ticker("NVDA")

# get 1 month of nvda dat
nvda_data = nvda.history(period="id", interval="1200m")

def backtest_200SMA():
    # load the data into a pandas DataFrame
    df = pd.read_csv("data.csv")

    # create a column for the 200 day moving average
    df["200d"] = df["close"].rolling(window=200).mean()

    # create a column for the strategy's position (1 for long, -1 for short)
    df["position"] = None

    # iterate through the DataFrame and determine the strategy's position
    for index, row in df.iterrows():
    if df["close"].iloc[index] > df["200d"].iloc[index]:
        df["position"].iloc[index] = 1
    else:
        df["position"].iloc[index] = -1

    # calculate the strategy's return
    df["return"] = df["close"].pct_change() * df["position"].shift(1)
    strategy_return = df["return"].sum()
    print("Strategy return: ", strategy_return)

def forward_testing():
    return False

def optimize_SMA():
    # calculate the strategy's return
    df["return"] = df["close"].pct_change() * df["position"].shift(1)
    return df["return"].sum()

    # define a list of window sizes to test
    window_sizes = [5, 10, 20, 50, 100, 200, 1400]

    # create an empty dictionary to store the results
    results = {}

    # iterate through the window sizes and calculate the strategy's return for each one
    for window in window_sizes:
    strategy_return = calc_strategy_return(window)
    results[window] = strategy_return

    # print the results
    print(results)

        # print the results
        print(results)

def calc_strategy_return(window):
    # create a column for the moving average
    df["ma"] = df["close"].rolling(window=window).mean()

    # create a column for the strategy's position (1 for long, -1 for short)
    df["position"] = None

    # iterate through the DataFrame and determine the strategy's position
    for index, row in df.iterrows():
        if df["close"].iloc[index] > df["ma"].iloc[index]:
        df["position"].iloc[index] = 1
        else:
        df["position"].iloc[index] = -1
