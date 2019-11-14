'''
cmd命令执行 mitmdump -s mtdu.py | python extract.py
'''
import sys
sys.path.append('../')
import os
path = os.getcwd()
print(path)
# os.system('mitmdump -s {path}\midu.py | python {path}\extract.py'.format(path=path))


