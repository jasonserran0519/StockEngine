import random
import time
from stock_exchange import StockExchange

def simulate_trading(stock_exchange, num_orders=100):
    tickers = list(range(1024))  # 1024 tickers
    for _ in range(num_orders):
        order_type = random.choice(['Buy', 'Sell'])
        ticker = random.choice(tickers)
        quantity = random.randint(1, 100)
        price = round(random.uniform(10, 500), 2)  # Round for cleaner output
        stock_exchange.add_order(order_type, ticker, quantity, price)
        time.sleep(0.01)  # Simulate real-time transactions

if __name__ == "__main__":
    exchange = StockExchange()
    simulate_trading(exchange, 50)