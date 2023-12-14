import requests

def fetch_cryptocurrency_data():
    
    exchange1_url = "https://api.pro.coinbase.com/products/BTC-USD/ticker"
    exchange2_url = "https://api.pro.coinbase.com/products/ETH-USD/ticker"


    try:
        data_exchange1 = requests.get(exchange1_url).json()
        data_exchange2 = requests.get(exchange2_url).json()

        crypto_data = {
            'exchange1': {
                'btc_usd': data_exchange1['btc_usd'],
                'eth_usd': data_exchange1['eth_usd'],
            },
            'exchange2': {
                'btc_usd': data_exchange2['btc_usd'],
                'eth_usd': data_exchange2['eth_usd'],
            },
        }

        return crypto_data

    except requests.RequestException as e:
        print(f"Error fetching cryptocurrency data: {e}")
        return None

if __name__ == "__main__":
    crypto_data = fetch_cryptocurrency_data()
    print(crypto_data)
