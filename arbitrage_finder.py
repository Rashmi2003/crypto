def find_arbitrage_opportunities(crypto_data, arbitrage_threshold=0.02):
 
    arbitrage_opportunities = []

    exchange_pairs = [(base_exchange, comparison_exchange) for base_exchange in crypto_data for comparison_exchange in crypto_data if base_exchange != comparison_exchange]

    for base_exchange, comparison_exchange in exchange_pairs:
        for currency_pair in crypto_data[base_exchange]:
            if currency_pair in crypto_data[comparison_exchange]:
                price_base_exchange = crypto_data[base_exchange][currency_pair]
                price_comparison_exchange = crypto_data[comparison_exchange][currency_pair]

                if (price_base_exchange / price_comparison_exchange - 1) > arbitrage_threshold:
                    opportunity = {
                        'BaseExchange': base_exchange,
                        'ComparisonExchange': comparison_exchange,
                        'CurrencyPair': currency_pair,
                        'ProfitPercentage': ((price_base_exchange / price_comparison_exchange) - 1) * 100,
                    }
                    arbitrage_opportunities.append(opportunity)

    return arbitrage_opportunities

if __name__ == "__main__":
    example_crypto_data = {
        'exchange1': {'btc_usd': 50000, 'eth_usd': 3000},
        'exchange2': {'btc_usd': 49000, 'eth_usd': 2900},
    }

    opportunities = find_arbitrage_opportunities(example_crypto_data)

    if opportunities:
        print("Arbitrage Opportunities:")
        for opportunity in opportunities:
            print(opportunity)
    else:
        print("No arbitrage opportunities found.")
