import csv

class Item:
     pay_rate = 0.8  # The pay rate after 20% discount
     all = []



    
     def __init__(self, name: str, price: float, quantity=0):
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

     def calculate_total_price(self):
        return self.price * self.quantity
    
     def apply_discount(self):
        self.price = self.price * self.pay_rate

          

     @classmethod
     def instantiate_from_csv(cls):
        with open('items.csv', 'r') as f:
            reader = csv.DictReader(f)
    #           items = list(reader)

            for row in reader:
                 cls(
                      name=row[name[0]],
                      price=float(row['price']),
                      quantity=int(row['quantity']),
       )  
     def __repr__(self):
        return f"Item('{self.name}', '{self.price:.2f}', '{self.quantity}')"   


Item.instantiate_from_csv()