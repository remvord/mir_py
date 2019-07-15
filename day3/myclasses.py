class C1(object):
    YES='YES'
    __NO='NO'
    _CANCEL='CANCEL'

    def __init__(self):
        print('---------Construction C1------------')

    def m1(self):
        print(self)

    def __str__(self):
        print('=======C1=======')
        return "Class C1 - мой класс " + \
           super.__str__(self)


###############################
class C3(object):
    def __init__(self):
        print('---------Construction C3------------')

    def __str__(self):
        return "Class C3 " + \
           super.__str__(self)
###############################


class C2(C1, C3):
    def __init__(self):
        print('--------------Construction C2------------------')

    def __str__(self):
        return "Class C2 - наследник класса C1, C3 " + \
               super.__str__()

    def info(self):
        return self.YES


if __name__ == '__main__':
    c1 = C1()
    print(c1)