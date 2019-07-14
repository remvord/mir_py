import sys
import funclib
import funclib1

lang = 'en'
if lang == 'ru':
    glob = sys.modules['funclib']
    print(glob.YES)

else:
    glob = sys.modules['funclib1']
    print(glob.YES)



