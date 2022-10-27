class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "coxinha": ["massa", "frango"],
    }
    MINIMUM_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    def __init__(self):
        self._inventory = {
            "pao": 0,
            "carne": 0,
            "queijo": 0,
            "molho": 0,
            "presunto": 0,
            "massa": 0,
            "frango": 0,
        }

    def add_new_order(self, customer, order, day):
        for ingredient in self.INGREDIENTS[order]:
            if (
                self._inventory[ingredient]
                >= self.MINIMUM_INVENTORY[ingredient]
            ):
                return False
        for ingredient in self.INGREDIENTS[order]:
            self._inventory[ingredient] += 1

    def get_quantities_to_buy(self):
        return self._inventory

    def get_available_dishes(self):
        available_ingredients = {
            inventory[0]
            for inventory, minimun_quantity in zip(
                self._inventory.items(), self.MINIMUM_INVENTORY.values()
            )
            if minimun_quantity - inventory[1] >= 1
        }
        available_dishes = {
            dish[0]
            for dish in self.INGREDIENTS.items()
            if set(dish[1]).issubset(available_ingredients)
        }
        return available_dishes
