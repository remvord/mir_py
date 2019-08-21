import os
import shutil


w = os.walk('/home/remvord/shara')
print(w)

for r in w:
    for rr in r[2]:
        name = f'{r[0]}/{rr}'
        if (name[-3::]) == '.py':
            print(name, os.path.getsize(name))
            shutil.copyfile(name, fr'/home/remvord/PycharmProjects/mir_py/tmp/{rr}')


# print(os.getlogin())
# print()