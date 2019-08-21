import dataclasses
import datetime
@dataclasses.dataclass(order=True)
class Person:
    ename:str
    job:str
    sal:float
    bd:datetime.datetime
    empno:int
    def info(self):
        return 'Persona :{self.ename}'


if __name__ == '__main__':
    pass