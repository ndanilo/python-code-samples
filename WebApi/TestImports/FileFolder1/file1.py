def test(obj):
    print(f"Hello {obj}.")
    file2.CallFromFile2()

def testA():
    print('from file1')

import sys, os
x = os.path.dirname(__file__)
a = os.path.abspath(os.path.join(x,'..','FileFolder2'))
b = os.path.abspath(os.path.join(a,'file2.py'))
sys.path.insert(0, a)
sys.path.insert(0, b)

import file2 as file2

if __name__ == '__main__':
    test('me caller')
    file2.OtherFile()