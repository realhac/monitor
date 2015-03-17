# -*- coding:utf-8 -*-

import os, sys

class HTML_Test_Report:
    def __init__(self, tr_name):
        self._html = open(tr_name, 'w')

    def writeTag(self, tag, begin, para=[]):
        if begin:
            if para:
                for pa in para:
                    self._html.write("<" + tag + " " + pa + " " + ">")
            else:
                self._html.write("<" + tag + ">")
        else:
            self._html.write("<" + tag + "/>")

    def trFinish(self):
        self._html.close()

    def writeTableCss(self):
        fp = open("../css/table.css", "rb")
        fc = fp.read();
        self._html.write(fc)
        fp.close()

    def writeTableHead(self):
        self.writeTag()

if __name__ == "__main__":
    tr = HTML_Test_Report("test.html")

    tr.writeTag("html", True)

    tr.writeTableCss()

    tr.writeTag("head", True)
    tr.writeTag("title", True)
    tr.writeTag("title", False)
    tr.writeTag("head", False)
    tr.writeTag("body", True)
    tr.writeTag("body", False)
    tr.writeTag("html", False)

    tr.trFinish()
