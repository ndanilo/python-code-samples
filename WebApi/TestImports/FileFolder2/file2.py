a = "file2"

def CallFromFile2():
    print("file2 ok!")
    #file1.test('called from file2')

def OtherFile():
    file1.testA()

import sys, os
x = os.path.dirname(__file__)
a = os.path.abspath(os.path.join(x,'..','FileFolder1'))
b = os.path.abspath(os.path.join(a,'file1.py'))
sys.path.insert(0, a)
sys.path.insert(0, b)

import file1

if __name__ == '__main__':
    print('file2')

