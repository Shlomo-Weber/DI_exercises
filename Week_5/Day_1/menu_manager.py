class MenuManager:
    def __init__(self, menu):
        self.menu = {}

    def add_item(self, name, price, spice_level, gluten):
        item = {
            "name":name,
            "price":price,
            "spice_level": spice_level,
            "gluten": gluten
        }
        self.menu.append(item)
my_menu = MenuManager("herp")

print(my_menu.menu)