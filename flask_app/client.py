import requests
class Stock(object):
    def __init__(self, data, detailed=False):
        self.symbol = data.get("symbol", "")
        self.name = data.get("name", "")
        self.exchange = data.get("exchange", "")
        self.currency = data.get("currency", "USD")
        self.type = "Stock"
        self.is_market_open = data.get("is_market_open", False)
        self.datetime = data.get("datetime", "")
        self.open = data.get("open", 0)
        self.high = data.get("high", 0)
        self.low = data.get("low", 0)
        self.close = data.get("close", 0)
        self.previous_close = data.get("previous_close", 0)
        self.volume = data.get("volume", 0)
        self.change = data.get("change", 0)
        self.change_percent = data.get("percent_change", 0)
        self.average_volume = data.get("average_volume", 0)

    def __repr__(self):
        return f"{self.symbol} ({self.name})"
class StockClient(object):
    def __init__(self, api_key):
        self.sess = requests.Session()
        self.base_url = "https://api.twelvedata.com"
        self.api_key = api_key

    def get_stock_details(self, symbol): 
        try:
            # Quote endpoint
            # This contains basically all the numerical data
            quote_url = f"{self.base_url}/quote?symbol={symbol}&apikey={self.api_key}"
            quote_resp = self.sess.get(quote_url)
            if quote_resp.status_code != 200:
                raise ValueError("QuoteAPI request failed")
            quote_data = quote_resp.json()

            # Stocks endpoint
            # This contains other stuff like company name, exchange, etc
            stocks_url = f"{self.base_url}/stocks?symbol={symbol}&apikey={self.api_key}"
            stocks_resp = self.sess.get(stocks_url)
            if stocks_resp.status_code != 200:
                raise ValueError("Stocks API request failed")
            stocks_data = stocks_resp.json()

            # Combine data from both endpoints
            data = quote_data.copy()
            data.update(stocks_data["data"][0])

            return Stock(data, detailed=True)
            
        except Exception as e:
            raise ValueError(f"Error: {str(e)}")

## -- Example usage -- ###
if __name__ == "__main__":
    import os
    
    client = StockClient(os.environ.get("TWELVE_DATA_API_KEY"))
    stock_details = client.get_stock_details("QLYS")
    print(f"Name: {stock_details.name}")
    print(f"Symbol: {stock_details.symbol}")
    print(f"Exchange: {stock_details.exchange}")
    print(f"Currency: {stock_details.currency}")
    print(f"Datetime: {stock_details.datetime}")
    print(f"Open: {stock_details.open}")
    print(f"High: {stock_details.high}")
    print(f"Low: {stock_details.low}")
    print(f"Close: {stock_details.close}")
    print(f"Volume: {stock_details.volume}")
    print(f"Previous Close: {stock_details.previous_close}")
    print(f"Change: {stock_details.change}")
    print(f"Change Percent: {stock_details.change_percent}")
    print(f"Average Volume: {stock_details.average_volume}")
    print(f"Market Open: {stock_details.is_market_open}")