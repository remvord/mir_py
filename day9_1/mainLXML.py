import lxml.html
# from xml.etree import ElementTree

if __name__ == '__main__':
    with open(r'/home/remvord/king_corp.xml', 'r') as f:
        try:
            dom = lxml.html.parse(f)
            root = dom.getroot()
            for r in root.xpath(
                    '//king_corp/departments/department/employees/employee/salary'):
                print(r.text)
            print('-'*20)
            sal = 0
            for r in dom.iter('salary'):
                sal += float(r.text)
            print(sal)
            print('-'*20)
            print('---Document valid---' + str(root))

        except Exception as e:
            print(e)
