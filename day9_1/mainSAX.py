import time
import xml.sax


class MyHandler(xml.sax.ContentHandler):
    __sal = False
    __ename = False
    __emp = False
    __report = ''

    def __init__(self, file):
        self.__file = file

    def characters(self, content):
        if self.__emp and self.__ename:
            self.__report += ' ' + content
        if self.__emp and self.__sal:
            self.__report += ' ' + content + '\r\n'


    def startDocument(self):
        self.__startTime = time.time()
        print('---Start parsing---')

    def startElement(self, name, attrs):
        if (name=='employee'):
            self.__emp=True
            self.__report+=attrs.get('id')
        if self.__emp:
            if name == 'name':self.__ename=True
        if self.__emp:
            if name == 'salary':self.__sal=True

    def endElement(self, name):
        if (name=='employee'):self.__emp=False
        if self.__emp:
            if name == 'name': self.__ename = False
        if self.__emp:
            if name == 'salary': self.__sal = False

    def endDocument(self):
        time.sleep(.1)
        print('---End parsing---', (time.time() - self.__startTime))
        self.__file.write(self.__report)


if __name__ == '__main__':
    with open(r'/home/remvord/king_corp.xml', 'r') as f:
        try:
            with open(r'/home/remvord/emp.txt', 'w') as fEmp:
                myhandler = MyHandler(fEmp)
                xml.sax.parse(f, myhandler)
                print('---Valid---')

        except Exception as e:
            print(e)
