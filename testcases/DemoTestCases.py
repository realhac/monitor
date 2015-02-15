# -*- coding:utf-8 -*-

import sys

sys.path.append('..')

from core.TestCases import Test_Cases

class Demo_Test_Case(Test_Cases):
    def __init__(self):
        Test_Cases.__init__(self)

    def setUp(self):
        Test_Cases.setUp(self)

    def testRun(self):
        Test_Cases.testRun(self)

    def tearDown(self):
        Test_Cases.tearDown(self)

    def main(self):
        self.setUp()
        self.testRun()
        self.tearDown()

if __name__ == "__main__":
    dtc = Demo_Test_Case()
    dtc.main()
