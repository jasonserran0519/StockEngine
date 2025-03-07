### order.py
class Order:
    import itertools
    order_id_counter = itertools.count()
    
    def __init__(self, order_type, ticker, quantity, price):
        self.order_id = next(Order.order_id_counter)
        self.order_type = order_type  # 'Buy' or 'Sell'
        self.ticker = ticker
        self.quantity = quantity
        self.price = price

class Node:
    def __init__(self, order):
        self.order = order
        self.next = None

### order_list.py
import threading
from order import Node

class OrderList:
    def __init__(self, ascending=True):
        self.head = None
        self.ascending = ascending  # True for Sell (low to high), False for Buy (high to low)
        self.lock = threading.Lock()
    
    def insert_order(self, order):
        """Insert order in sorted order."""
        new_node = Node(order)
        with self.lock:
            if not self.head or (self.ascending and order.price < self.head.order.price) or (not self.ascending and order.price > self.head.order.price):
                new_node.next = self.head
                self.head = new_node
                return
            
            prev, current = None, self.head
            while current and ((self.ascending and order.price >= current.order.price) or (not self.ascending and order.price <= current.order.price)):
                prev, current = current, current.next
            
            prev.next = new_node
            new_node.next = current
    
    def pop_head(self):
        """Remove and return the head order."""
        with self.lock:
            if not self.head:
                return None
            order = self.head.order
            self.head = self.head.next
            return order
    
    def peek_head(self):
        """Return the head order without removing it."""
        return self.head.order if self.head else None

### stock_exchange.py
from order import Order

class StockExchange:
    def __init__(self, num_tickers=1024):
        self.buy_orders = [OrderList(ascending=False) for _ in range(num_tickers)]
        self.sell_orders = [OrderList(ascending=True) for _ in range(num_tickers)]
    
    def add_order(self, order_type, ticker, quantity, price):
        """Add an order and attempt to match."""
        order = Order(order_type, ticker, quantity, price)
        if order_type == 'Buy':
            self.buy_orders[ticker].insert_order(order)
        else:
            self.sell_orders[ticker].insert_order(order)
        self.match_order(ticker)
    
    def match_order(self, ticker):
        """Match orders for the given ticker safely in a multi-threaded environment."""
        while True:
            top_buy = self.buy_orders[ticker].peek_head()
            top_sell = self.sell_orders[ticker].peek_head()

            if not top_buy or not top_sell or top_buy.price < top_sell.price:
                break

            executed_quantity = min(top_buy.quantity, top_sell.quantity)

            print(f"Matched Order: {executed_quantity} shares of {ticker} at ${top_sell.price}")

            # Atomic updates (ensuring safety in multi-threading)
            with threading.Lock():  
                if top_buy.quantity > executed_quantity:
                    top_buy.quantity -= executed_quantity
                else:
                    self.buy_orders[ticker].pop_head()

                if top_sell.quantity > executed_quantity:
                    top_sell.quantity -= executed_quantity
                else:
                    self.sell_orders[ticker].pop_head()


### simulate.py
import random
import time
# from exchange import StockExchange

def simulate_trading(stock_exchange, num_orders=100):
    tickers = list(range(1024))  # 1024 tickers
    for _ in range(num_orders):
        order_type = random.choice(['Buy', 'Sell'])
        ticker = random.choice(tickers)
        quantity = random.randint(1, 100)
        price = random.uniform(10, 500)
        stock_exchange.add_order(order_type, ticker, quantity, price)
        time.sleep(0.01)

### main.py
# from exchange import StockExchange
# from simulate import simulate_trading

if __name__ == "__main__":
    exchange = StockExchange()
    simulate_trading(exchange, 50)