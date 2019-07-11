import sys
import printer

s = "wwwww\
     wwwwww"
print(s)

# Если это основной поток то ...
if __name__ == '__main__':
    # pass
    # None
    print('Hello world')
    print(sys.path)
    print(dir())
    print(__name__)
    print(sys.__name__)
    print(printer.NO)
    print(dir(s))
    print(type(s))
    s = 1
    print(type(s))
    print(dir(s))