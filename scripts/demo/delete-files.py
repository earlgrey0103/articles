"""https://www.ibm.com/developerworks/cn/linux/tips/l-python/
"""

from os.path import walk, join, normpath
from os import chdir, remove


def scan(arg, dirname, names):
    for file in names:
        if file[-1:] == "~" or file[-4:] == ".bak": # 第1行
            files = normpath(join(dirname, file)) # 第2行
            chdir(dirname) # 第3行
            print("deleting", files) # 第4行
            remove(file) # 第5行
            print("done!") # 第6行

if __name__ == '__main__':
    path = chdir('.') # 第7行
    walk(path, scan, 0)

