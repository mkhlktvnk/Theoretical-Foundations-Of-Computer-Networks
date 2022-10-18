import random

from accessify import private


class ErrorGenerator:
    def __init__(self, number_of_errors: int, packages: list):
        self.__number_of_errors = number_of_errors
        self.__packages = packages

    def generate_errors(self) -> list:
        packages_with_errors = []
        positions = self.generate_positions_list()
        for package in self.__packages:
            temp = list(package)
            for position in positions:
                temp[position] = self.generate_symbol(temp[position])
            packages_with_errors.append(''.join(temp))
        return packages_with_errors

    @private
    def generate_positions_list(self) -> list:
        positions = []
        seen = set()
        for i in range(self.__number_of_errors):
            x = int(random.uniform(8, 32))
            while x in seen:
                x = int(random.uniform(8, 32))
            seen.add(x)
            positions.append(x)
        positions.sort()
        return positions

    @private
    def generate_symbol(self, initial_symbol: str):
        symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        random.shuffle(symbols)
        for symbol in symbols:
            if symbol != initial_symbol:
                return symbol
