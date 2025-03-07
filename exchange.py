from order_list import OrderList
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
        """Match orders for the given ticker."""
        while True:
            top_buy = self.buy_orders[ticker].peek_head()
            top_sell = self.sell_orders[ticker].peek_head()
            
            if not top_buy or not top_sell or top_buy.price < top_sell.price:
                break
            
            executed_quantity = min(top_buy.quantity, top_sell.quantity)
            print(f"Matched Order: {executed_quantity} shares of {ticker} at ${top_sell.price}")
            
            if top_buy.quantity > executed_quantity:
                top_buy.quantity -= executed_quantity
            else:
                self.buy_orders[ticker].pop_head()
            
            if top_sell.quantity > executed_quantity:
                top_sell.quantity -= executed_quantity
            else:
                self.sell_orders[ticker].pop_head()