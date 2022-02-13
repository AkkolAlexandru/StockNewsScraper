import requests
from datetime import datetime
from reddit import reddit_signal
from investopedia import investopedia_signal

trades = []
def run_engine():

    news = list()
    out=[]
    def open_trade(ticker, decision, sentence):
        global trades
        list_of_active = [list(item.keys()) for item in trades]
        list_of_active = [item for sublist in list_of_active for item in sublist]
        now = datetime.now()
        minute = now.strftime("%M")
        if ticker not in list_of_active:
            # get current ticker price
            # get api key from iexcloud.io
            apikey = "pk_d40b5f30ace045d9b25f7fc9cac8b0fd"
            headers = {'Content-Type': 'application/json'}
            url = f"https://cloud.iexapis.com/stable/stock/{ticker}/quote?token={apikey}"
            response = requests.get(url, headers=headers)
            if response.ok is False:
                return None
            price = response.json()["latestPrice"]
            trades.append({ticker:[decision, f"{datetime.now().hour}:{minute}", price, sentence]})
        # returns global 'trades'

    signals = investopedia_signal()

    for combo in signals:
        open_trade(list(combo[0].keys())[0], list(combo[0].values())[0], combo[1])
    return trades