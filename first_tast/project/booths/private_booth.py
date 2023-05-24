from project.booths.booth import Booth


class PrivateBooth(Booth):
    PRICE_PER_PERSON = 3.50

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self):
        self.price_for_reservation = self.PRICE_PER_PERSON * self.capacity
        self.is_reserved = True

