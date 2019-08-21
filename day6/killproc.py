import os
import subprocess
import psutil

#
# p = subprocess.Popen(('ps', '-aux'), shell=True, stdout=subprocess.PIPE)
# out = p.communicate()
# c = 0
# a = str(out).find('thunderbird')
# print(a)
# print(out[a:32])


a = psutil.process_iter()
for r in a:
    if r.name() == 'zoiper':
        print(r.name(), r.pid)
        r.kill()
