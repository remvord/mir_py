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


if __name__ == '__main__':
    p = Person('Ivan', 'Ivanov')
    p.age = 25
    print(p.fn, p.ln, p.age)
    print(p)
