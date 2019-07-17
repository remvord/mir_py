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


class Ud(ZP):
    def m1(self):
        print('Ud.m1')

    def ud(self):
        print("Удержания")


class Print(ZP):
    def m1(self):
        print('Ud.m1')

    def print(self):
        print("Печать")


class ZPAll(Nach, Print, Ud):
    """Расчет зарплаты"""


if __name__ == '__main__':
    r = ZPAll()
    r.raschet()
    r.m1()
