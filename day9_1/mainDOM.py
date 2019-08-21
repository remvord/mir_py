import xml
from xml.etree import ElementTree

if __name__ == '__main__':
    with open(r'/home/remvord/king_corp.xml', 'r') as f:

        try:
            etree = ElementTree.parse(f)
            print('---Document valid---' + str(etree))
            dom = etree.getroot()
            print(dir(dom))
            # print(len(dom.getchildren()))
            print(list(dom))
            for r in list(dom):
                print(r.tag)
            for r in list(dom[0]):
                print(r.tag, r.attrib['id'])
                for r in (list(r)):
                    print('  ', r.text)

            print('-'*20)
            sal = 0

            for r in dom.iter('salary'):
                sal += float(r.text)
            print(sal)

        except Exception as e:
            print(e)
