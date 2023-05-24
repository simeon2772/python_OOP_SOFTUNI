from project.booths.booth import Booth


class OpenBooth(Booth):
    PRICE_PER_PERSON = 2.50

    def __init__(self, booth_number: int, capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self):
        self.price_for_reservation = self.PRICE_PER_PERSON * self.capacity
        self.is_reserved = True

