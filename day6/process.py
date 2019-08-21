import os
import subprocess

# os.system('Text Editor')

c = 'zip -r archive tmp/*'
proc = subprocess.Popen(c, shell=True, stdout=subprocess.PIPE)
out = proc.communicate()

if proc.returncode == 0:
    print(out, '\nok')
else:
    print('Error')
