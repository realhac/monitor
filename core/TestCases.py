# -*- coding:utf-8 -*-

class Test_Cases:
    def __init__(self):
        print "init test cases template"

    def setUp(self):
        print "setup"

    def testRun(self):
        print "test running"

    def tearDown(self):
        print "teardown"

    def main(self):
        self.setUp()
        self.testRun()
        self.tearDown()

if __name__ == "__main__":
    tc = Test_Cases()
    tc.main()
