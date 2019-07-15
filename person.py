class Person():
    def __init__(self, fn, ln, age=0):
        self.__fn = fn
        self.__ln = ln
        self.__age = age

    @property
    def fn(self):
        return self.__fn

    @property
    def ln(self):
        return self.__ln

    @property
    def ln(self):
        return self.__ln

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.getter
    def getAge(self):
        if self.__age == 0:
            raise ValueError()
        return self.__age

    def __str__(self):
        return f'{self.fn} {self.ln} возраст {self.age}'

    def __repr__(self):
        return f'{self.fn} {self.ln} {self.age}'

    def info(self):
        return self.__str__()


class Student(Person):
    def __init__(self, fn, ln, age, univer):
        Person.__init__(self, fn, ln, age)
        self.__univer = univer

    @property
    def univer(self):
        return self.__univer

    def info(self):
        return f'{super().info()} учится в {self.univer}'


class Consumer(Person):
    def __init__(self, fn, ln, age, company):
        Person.__init__(self, fn, ln, age)
        self.__company = company

    @property
    def company(self):
        return self.__company

    def info(self):
        return f'{super().info()} работает в  {self.company}'


if __name__ == '__main__':
    s = Student('Ivan', 'Ivanov', 25, "UPI")
    c = Consumer('Petr', 'Petrov', 40, 'TIZOL')
    p = Person('Sidr', 'Sidorov', 35)
    a = [s, c, p]
    for r in a:
        print(r.info())
