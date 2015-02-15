# -*- coding:utf-8 -*-

import sys

sys.path.append('..')

from core.TestCases import Test_Cases

class Demo_Test_Case(Test_Cases):
    def __init__(self):
        Test_Cases.__init__(self)

if __name__ == "__main__":
    dtc = Demo_Test_Case()
