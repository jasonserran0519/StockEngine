# StockEngine
A real-time stock trading engine that efficiently matches **Buy** and **Sell** orders while ensuring thread safety and avoiding dictionary-based data structures.

## Features
- Supports **1,024 tickers** (stocks).
- Implements an **O(n) order matching** algorithm.
- Uses **lock-free data structures** to prevent race conditions.
- Simulates real-time stock transactions dynamically.

---

## How It Works

### 1. Order Management (`order.py`, `order_list.py`)
- `Order`: Represents a **Buy** or **Sell** order with a ticker, quantity, and price.
- `OrderList`: A **linked list-based queue** that manages orders in FIFO order.

### 2. Stock Exchange (`exchange.py`)
- `StockExchange`: Handles order book operations.
- `add_order(order_type, ticker, quantity, price)`: Adds a **Buy** or **Sell** order.
- `match_order(ticker)`: Matches orders efficiently:
  - Finds the **highest Buy** and **lowest Sell** orders.
  - Matches them if `buy_price >= sell_price`.
  - Updates/removes orders accordingly.

### 3. Simulation (`simulate.py`)
- **Randomly generates** Buy/Sell orders for different stocks.
- Simulates **real-time trading** by executing orders dynamically.

### 4. Main Execution (`main.py`)
- Runs **unit tests** to validate order matching.
- Starts a **live trading simulation** with `simulate_trading()`.

---

## How to Run
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/StockEngine.git
   cd StockEngine
   ```  
2. Run the simulation:
   ```sh
   python3 main.py
   ```  
3. Expected output:
   ```
   Starting stock trading simulation...
   Matched Order: 10 shares of 0 at $98
   Matched Order: 5 shares of 0 at $105
   Simulation complete.
   ```

---

## Future Improvements
- Enhance **multi-threading efficiency** with lock-free queues.
- Implement a **persistent database** for order tracking.
- Add **order cancellation & modification** support.
- Improve **order matching algorithm** for higher efficiency.

