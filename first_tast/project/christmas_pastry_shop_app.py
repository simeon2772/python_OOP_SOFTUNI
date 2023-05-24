from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0  # total income of the pastry shop

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        delicacies_names = [d.name for d in self.delicacies]
        if name in delicacies_names:
            raise Exception(f"{name} already exists!")
        elif type_delicacy not in ("Gingerbread", "Stolen"):
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        if type_delicacy == "Gingerbread":
            d = Gingerbread(name, price)
        else:
            d = Stolen(name, price)

        self.delicacies.append(d)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        booth_numbers = [n.booth_number for n in self.booths]
        if booth_number == booth_numbers:
            raise Exception(f"Booth number {booth_number} already exists!")
        elif type_booth not in ("Open Booth", "Private Booth"):
            raise Exception(f"{type_booth} is not a valid booth!")
        if type_booth == "Open Booth":
            b = OpenBooth(booth_number, capacity)
        else:
            b = PrivateBooth(booth_number, capacity)
        self.booths.append(b)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        valid_booth_capacity = [b for b in self.booths if b.capacity >= number_of_people and b.is_reserved == False]
        if valid_booth_capacity is None:
            raise Exception(f"No available booth for {number_of_people} people!")
        valid_booth_capacity[0].reserve()
        return f"Booth {valid_booth_capacity[0].booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        try:
            booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))
        except StopIteration:
            raise Exception(f"Could not find booth {booth_number}!")

        try:
            delicacy = next(filter(lambda d: d.name == delicacy_name, self.delicacies))
        except StopIteration:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = next(filter(lambda b: b.booth_number == booth_number, self.booths))

        bill = booth.price_for_reservation + sum(d.price for d in booth.delicacy_orders)

        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0

        self.income += bill
        return f"Booth {booth_number}:\n" \
               f"Bill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."


shop = ChristmasPastryShopApp()
print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
print(shop.delicacies[0].details())
print(shop.add_booth("Open Booth", 1, 30))
print(shop.add_booth("Private Booth", 10, 5))
print(shop.reserve_booth(30))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.reserve_booth(5))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.get_income())
