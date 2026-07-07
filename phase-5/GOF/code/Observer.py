class Inventory:

    def __init__(self, drug_name, quantity):
        self.drug_name = drug_name
        self.quantity = quantity
        self.observers = []   # list baraye service haye neshande (observer)

    def add_observer(self, observer):
        self.observers.append(observer)

    def change_quantity(self, new_quantity):
        self.quantity = new_quantity
        print("Mojoodi daroo taghir kard:", self.quantity)

        # khabar dadan be observer ha
        for obs in self.observers:
            obs.update(self)


class AlertService:

    def update(self, inventory):
        # check mikone aya mojoodi kam shode ya na
        if inventory.quantity < 10:
            print("Hoshdar! Mojoodi daroo", inventory.drug_name, "kam shode.")


# estefade sade az system

inv = Inventory("Paracetamol", 20)

alert = AlertService()

# sabt kardan observer
inv.add_observer(alert)

# taghir mojoodi
inv.change_quantity(5)
