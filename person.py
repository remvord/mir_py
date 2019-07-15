class Person():
    # __fn = None

    def __init__(self, fn, ln):
        self.__fn = fn
        self.__ln = ln

    @property
    def fn(self):
        return self.__fn

    @property
    def ln(self):
        return self.__ln


if __name__ == '__main__':
    p = Person('Ivan', 'Ivanov')
    print(p.fn, p.ln)
