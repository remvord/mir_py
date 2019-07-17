import dataclasses


@dataclasses.dataclass()
class Emp:
    ename: str
    job: str
    sal: int = dataclasses.field(compare=False)


#########################################
@dataclasses.dataclass()
class Employee(Emp):
    """Class son Emp"""
    empno: int
    pass

    def info(self):
        """Comment print"""
        print(self.__str__())


if __name__ == '__main__':
    # p1 = Emp(ename='Ivanov', job='Boss', sal=100)
    # p2 = Emp(ename='Petrov', job='Mnager', sal=200)
    p = Employee(ename='Petrov', job='Mnager', sal=201, empno=10)
    # print(p.__repr__())
    # print(p)
    # p.ename='3333'
    # print(p)
    # print(p22 == p2)
    p.empno = 111
    print(p)
    print(Employee.__doc__)
