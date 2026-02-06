from product import Product 

class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, name , price , quantity ):
        product = Product(name ,price ,quantity)
        self.products.append(product)

    def remove_product(self, name):
        initial_count = len(self.products)
        self.products = [p for p in self.products if p.name != name]
        if len(self.products) < initial_count:
            print(f"Product '{name}' removed.")
        else:
            print(f"Product '{name}' not found")

    def show_products(self):
        if not self.products:
            print("No products available")
        for product in self.products:
            print(product)