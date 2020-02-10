class MenuManager:
    def __init__(self, menu):
        self.menu = {}
    def add_item(self,name, price, spice, gluten):
        self.menu[name, price, spice, gluten] = "Burger", 15, "A", True

my_Menu = MenuManager("menu")

my_Menu.add_item("Burger", 15, "A", True)

print(my_Menu.menu)