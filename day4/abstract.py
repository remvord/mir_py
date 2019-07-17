from abc import ABC, abstractmethod


class ZP(ABC):
    """Базовый класс зарплаты"""

    @abstractmethod
    def nach(self):
        """Начисления"""

    @abstractmethod
    def ud(self):
        """Удержания"""

    @abstractmethod
    def print(self):
        """Печать"""

    def raschet(self):
        self.nach()
        self.ud()
        self.print()


class Nach(ZP):
    def nach(self):
        """Начисления"""
        print("Начисления")


class Ud(Nach):
    def ud(self):
        print("Удержания")


class Print(Ud):
    def print(self):
        print("Печать")


class ZPAll(Print):
    """Расчет зарплаты"""


if __name__ == '__main__':
    r = ZPAll()
    r.raschet()
