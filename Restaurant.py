class Restaurant:
    def __init__(self, money=1000, current_recipes=None, current_raw_materials=None):
        # Initial amount of money for the restaurant
        self.money = money
        # List of current recipes available in the restaurant
        self.current_recipes = current_recipes if current_recipes is not None else []
        # Dictionary of current raw materials in the restaurant
        self.current_raw_materials = current_raw_materials if current_raw_materials is not None else {}
