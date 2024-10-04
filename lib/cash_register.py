#!/usr/bin/env python3
import ipdb

class CashRegister:
    
    def __init__(self,discount=0, total=0):
        self.discount = discount
        self.total = total
        self.items = []
        self.last_transaction = []

    def add_item(self, item, price, qty=1):
        for each in range(qty):
            self.items.append(item)
        self.last_transaction.append({"item_name": item, "price": price, "qty": qty})
        self.total += float(price) * qty

    # ipdb.set_trace()

    def apply_discount(self, discount=0):
        if self.discount:
            discount = self.total * (self.discount/100)
            self.total -= discount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")
 

    def void_last_transaction(self):
        self.total -= self.last_transaction[-1]["qty"] * self.last_transaction[-1]["price"]
        self.last_transaction.pop(-1)
        