#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.last_item = None
  def add_item(self, title, price, quantity=1):
    titles = [title] * quantity
    self.items.extend(titles)
    price *= quantity
    self.total += price
    self.last_item = (price, quantity)
    return self.items

  def apply_discount(self):
      if self.total > 0:
         self.total = int(self.total * (1 - (self.discount / 100)))
         print(f'After the discount, the total comes to ${self.total}.')
      else:
         print('There is no discount to apply.')
  def void_last_transaction(self):
     if self.last_item:
            price, quantity = self.last_item
            self.total -= price
            self.items = self.items[:-quantity]
            self.last_item = None
     else:
            print('No items to void.')