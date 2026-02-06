class Cart:
    def __init__(self):
        self.items = []

    def add_to_cart(self, product, quantity):
        if quantity <= product.quantity:
            self.items.append((product, quantity))
            product.quantity -= quantity
            print("Produs adaugat in cos")
        else:
            print("Stock insuficient")

    def view_cart(self):
        if len(self.items) == 0:
            print("Cosul este gol")
            return
        total = 0
        for product, quantity in self.items:
            cost = product.price * quantity
            total += cost
            print(product.name, "-",quantity , "buc-", cost,"lei")
        print("Total:", total , "lei")