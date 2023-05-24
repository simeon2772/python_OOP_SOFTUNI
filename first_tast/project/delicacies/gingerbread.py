from project.delicacies.delicacy import Delicacy


class Gingerbread(Delicacy):
    GINGERBREAD_PORTION_GRAMS = 200

    def __init__(self, name: str, price: float):
        super().__init__(name, self.GINGERBREAD_PORTION_GRAMS, price)

    def details(self) -> str:
        return f"Gingerbread {self.name}: 200g - {self.price:.2f}lv."


