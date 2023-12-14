from crypto_data_fetcher import fetch_cryptocurrency_data
from arbitrage_finder import find_arbitrage_opportunities
from utils import log_errors
import ccxt
from utils import log_error

def main():
    print("Crypto Arbitrage Trading Bot")

    exchanges = {
        'Binance': ccxt.binance,
        'Bittrex': ccxt.bittrex,
    }

    try:
        crypto_data = fetch_cryptocurrency_data(exchanges)

        if crypto_data:
            print("Cryptocurrency Market Data:")
            for exchange_name, data in crypto_data.items():
                print(f"{exchange_name} - {data['symbol']}:")
                print(f"Ask Price: {data['ask']}")
                print(f"Bid Price: {data['bid']}")
                print(f"Last Price: {data['last']}")
                print("-" * 30)

            opportunities = find_arbitrage_opportunities(crypto_data)  # Pass crypto_data to the function

            if opportunities:
                print("Arbitrage Opportunities:")
                for opportunity in opportunities:
                    print(opportunity)
            else:
                print("No arbitrage opportunities found.")

        else:
            print("Failed to fetch cryptocurrency data.")

    except ccxt.NetworkError as e:
        log_error(f"Network error: {e}")
    except ccxt.ExchangeError as e:
        log_error(f"Exchange error: {e}")
    except Exception as e:
        log_error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()



def fetch_cryptocurrency_data(exchanges, symbol='BTC/USDT'):
   
    crypto_data = {}

    for exchange_name, exchange_class in exchanges.items():
        try:
            exchange = exchange_class()
            ticker = exchange.fetch_ticker(symbol)
            crypto_data[exchange_name] = {
                'symbol': symbol,
                'ask': ticker['ask'],
                'bid': ticker['bid'],
                'last': ticker['last'],
            }
        except ccxt.NetworkError as e:
            log_error(f"Network error while fetching data from {exchange_name}: {e}")
        except ccxt.ExchangeError as e:
            log_error(f"Exchange error while fetching data from {exchange_name}: {e}")
        except Exception as e:
            log_error(f"An error occurred while fetching data from {exchange_name}: {e}")

    return crypto_data

if __name__ == "__main__":
    exchanges = {
        'Binance': ccxt.binance,
        'Bittrex': ccxt.bittrex,
    }

    crypto_data = fetch_cryptocurrency_data(exchanges)

    if crypto_data:
        print("Cryptocurrency Market Data:")
        for exchange_name, data in crypto_data.items():
            print(f"{exchange_name} - {data['symbol']}:")
            print(f"Ask Price: {data['ask']}")
            print(f"Bid Price: {data['bid']}")
            print(f"Last Price: {data['last']}")
            print("-" * 30)
    else:
        print("Failed to fetch cryptocurrency data.")

    if not crypto_data:
        print("Error fetching cryptocurrency data. Exiting.")

    arbitrage_opportunities = find_arbitrage_opportunities(crypto_data)

    if not arbitrage_opportunities:
        print("No arbitrage opportunities found.")
    else:
        print("Arbitrage Opportunities:")
        for opportunity in arbitrage_opportunities:
            print(f"Opportunity between {opportunity['Exchange1']} and {opportunity['Exchange2']}:")
            print(f"Currency Pair: {opportunity['CurrencyPair']}")
            print(f"Potential Profit Percentage: {opportunity['ProfitPercentage']:.2f}%")
            print("-" * 30)
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        log_error(f"An unexpected error occurred: {str(e)}")