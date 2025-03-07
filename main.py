from stock_exchange import StockExchange
from simulate import simulate_trading

if __name__ == "__main__":
    exchange = StockExchange()
    print("Starting stock trading simulation...\n")
    simulate_trading(exchange, num_orders=50)
    print("\nSimulation complete.")