from functools import reduce


class Calculator:
    @staticmethod
    def add(*args):
        result = sum(args)
        return result

    @staticmethod
    def multiply(*args):
        return reduce(lambda a, b: a * b, args)

    @staticmethod
    def divide(*args):
        return reduce(lambda a, b: a / b, args)

    @staticmethod
    def subtract(*args):
        return reduce(lambda a, b: a - b, args)

