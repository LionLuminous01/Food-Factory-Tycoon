# import the modules what we coded
from Shop import Shop
from Statistics import Statistics
from Machine import Machine
from Recipe import Recipe
from Restaurant import Restaurant
# import the other modules
from json import load
import random
class Main():
    def __init__(self, rounds=100):
        self.shop = Shop(create_product_per_tick=5)
        self.statistics = Statistics("Recipes.json")
        self.machines_data = {}
        self.machines = {}
        self.recipes = {}
        self.recipes_names = []
        self.current_recipes = []
        self.raw_materials = {}
        self.rounds = rounds
        self.current_round = 0
        self.restaurant = Restaurant(money=1000, current_recipes=[], current_raw_materials={})
        self.load_data("Datas.json")
        self.shop.add_raw_materials_to_inventory()  # Add initial raw materials to inventory
    
    def load_data(self, path):
        from json import load
        with open(path, "r") as file:
            data = load(file)
        # Load raw materials
        self.raw_materials = {}
        for name, details in data["Raw Materials"].items():
            self.raw_materials[name] = details
        # Load machines
        self.machines_data = {}
        for machine_name, machine_data in data["Machines"].items():
            self.machines_data[machine_name] = machine_data
        print("Data loaded successfully from", path)

    def machine_name(self, machine_type):
        # Finds the highest number among the given type of machines and returns the next one
        max_number = 0
        for name in self.machines:
            if name.startswith(machine_type + "_"):
                try:
                    number = int(name.split("_")[-1])
                    if number > max_number:
                        max_number = number
                except ValueError:
                    continue
        return f"{machine_type}_{max_number+1}"

    def create_machine(self, machine_type):
        name = self.machine_name(machine_type)
        if name in self.machines:
            print(f"Machine {name} already exists.")
            return False
        else:
            machine_data = self.machines_data.get(machine_type)
            if not machine_data:
                print(f"No data for machine type: {machine_type}")
                return False
            new_machine = Machine(name, machine_type)
            self.machines[name] = new_machine
            print(f"Machine {name} of type {machine_type} created successfully.")
            return True

    def run(self):
        if self.rounds <= 0:
            self.current_round = -1 # Infinite loop
        # print statistics
        print(f"Total recipes: {self.statistics.get_total_recipes()}")
        print(f"Average recipe time: {self.statistics.get_average_time()} ticks")
        print(f"Most common machine: {self.statistics.get_most_common_machine()[0]} used {self.statistics.get_most_common_machine()[1]} times")
        print("Most used raw materials:")
        most_used_raw_materials = self.statistics.get_most_used_raw_materials(top=True, topelements=5, reverse=True)
        for raw_material, amount in most_used_raw_materials:
            print(f"{raw_material}: {amount} times")
        # Does not generate new random orders, only uses the existing functions
        print("Available machines:", list(self.machines_data.keys()))
        print("Available raw materials:", list(self.raw_materials.keys()))
        print("Available recipes:", self.recipes_names)
        # Here you can add further logic, e.g. machine creation, raw material purchase, etc.
        # Example for creating a machine:
        # self.create_machine("Oven")
        # self.create_machine("Mixer")
        # etc.
if __name__ == "__main__":
    main = Main(rounds=10)  # Set the number of rounds to run
    main.run()
    print("Simulation completed.")