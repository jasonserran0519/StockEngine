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