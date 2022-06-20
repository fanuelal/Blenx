import json
import os
import shutil
import subprocess
print('this is the test file')
cmd = 'python detector.py'
p = subprocess.Popen(cmd, shell=True)
print('hello after the dataset')
"""
data = {'id': 23,'name': 'hello'}
readen = []
with open("list.json",'r') as li:
    readen = json.load(li)

readen.append(data)

with open("list.json",'w') as lif:
    json.dump(readen, lif, indent=4)
"""
#shutil.rmtree('testdir') for delete dir with sub dir

