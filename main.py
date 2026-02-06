from product_manager import ProductManager
from cart import Cart

manager = ProductManager()
cart = Cart()

manager.add_product("Telefon", 2000 , 5)
manager.add_product("Laptop", 4300, 4)

manager.show_products()

cart.add_to_cart(manager.products[0] , 2)
cart.view_cart()