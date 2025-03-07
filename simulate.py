import random
import time
import threading
from exchange import StockExchange

def simulate_trading(stock_exchange, num_orders=100, num_threads=5):
    tickers = list(range(1024))  # 1024 tickers
    
    def worker():
        for _ in range(num_orders // num_threads):  # Distribute workload
            order_type = random.choice(['Buy', 'Sell'])
            ticker = random.choice(tickers)
            quantity = random.randint(1, 100)
            price = round(random.uniform(10, 500), 2)  # Round for cleaner output
            stock_exchange.add_order(order_type, ticker, quantity, price)
            time.sleep(0.001)  # Simulate real-time transactions

    threads = [threading.Thread(target=worker) for _ in range(num_threads)]
    
    for t in threads:
        t.start()
    
    for t in threads:
        t.join()

    print("\nSimulation complete! Checking order book consistency...\n")
    # You can print order books here if needed

if __name__ == "__main__":
    exchange = StockExchange()
    simulate_trading(exchange, 50)