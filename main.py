from exchange import StockExchange
from simulate import simulate_trading

def test_stock_exchange():
    exchange = StockExchange()

    # Adding Buy orders
    exchange.add_order('Buy', 0, 10, 100)  # Buy 10 shares at $100
    exchange.add_order('Buy', 0, 5, 105)   # Buy 5 shares at $105 (higher price, should be prioritized)

    # Adding Sell orders
    exchange.add_order('Sell', 0, 10, 98)  # Sell 10 shares at $98 (should match immediately)
    
    print("\n=== Running Test Case ===")
    exchange.match_order(0)  # Ensure it matches properly
    print("\n=== Test Case Complete ===")

def print_order_book(exchange, ticker):
    """ Print the order book for debugging. """
    print(f"\nFinal Order Book for Ticker {ticker}:")

    print("\nBuy Orders:")
    buy = exchange.buy_orders[ticker].head
    while buy:
        print(f"Buy {buy.order.quantity} shares at ${buy.order.price}")
        buy = buy.next

    print("\nSell Orders:")
    sell = exchange.sell_orders[ticker].head
    while sell:
        print(f"Sell {sell.order.quantity} shares at ${sell.order.price}")
        sell = sell.next

if __name__ == "__main__":
    exchange = StockExchange()
    print("Starting stock trading simulation...\n")
    simulate_trading(exchange, num_orders=100, num_threads=5)
    print("\nSimulation complete.")

    # Check final state of order book for ticker 0
    print_order_book(exchange, 0)
