class CoffeeShop():
    def __init__(self, name, menu, orders):
        self.name = name
        self.menu = menu
        self.orders = orders

    def add_order(self, order_name):
        menu_items = []
        for item in self.menu:
            menu_items.append(item["item"])
        if order_name not in menu_items:
            return "This item is currently unavailable!"
        else:
            self.orders.append(order_name)
            return f"Order added: {order_name}"
    
    def fulfill_orders(self):
        if not self.orders:
            return f"the item is ready"
        else:
            return "All orders have been fulfilled!"
    
    def list_orders(self):
        if not self.orders:
            return "an empty list"
        else:
            return self.orders
    
    def due_amount(self):  # همشي علي كل ال ليست وهشوف هل الليسته ده هي ال موجوده في الديشكنري لو اه اعمل لدد ببلرايس في ال توتال برايس 
        total_price = 0
        for order in self.orders:
            for item in self.menu:
                if item["item"] == order:
                    total_price += item["price"]
        return total_price
    
    def chaepest_item(self):
        cheapest = self.menu[0] 
        for item in self.menu:
            if item["price"] < cheapest["price"]:
                cheapest = item
        return cheapest
    
    def drinks_only(self):
        drinks = []
        for item in self.menu:
            if item["type"] == "drink": 
                drinks.append(item["item"])  
        return drinks
    
    def food_only(self):
        food = []
        for item in self.menu:
            if item["type"] == "food":
                food.append(item["item"])
        return food

menu = [
    {"item": "Burger", "type": "food", "price": 5},
    {"item": "Pizza", "type": "food", "price": 7},
    {"item": "Coke", "type": "drink", "price": 1},
    {"item": "Water", "type": "drink", "price": 3}
]

orders = []


o = CoffeeShop("3abdo caffe", menu, orders)

print(o.add_order("Burger"))
print(o.add_order("Pizza"))
print(o.add_order("Coke"))
print(o.add_order("Water"))

print(o.fulfill_orders()) 
print(o.list_orders())
print(o.due_amount())

print(o.drinks_only())
print(o.food_only())
print(o.chaepest_item())



