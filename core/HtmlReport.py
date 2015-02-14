# -*- coding:utf-8 -*-

import os, sys

class HTML_Test_Report:
    def __init__(self, tr_name):
        self._html = open(tr_name, 'w')

    def write_tag(self, tag, begin, para=[]):
        if begin:
            if para:
                for pa in para:
                    self._html.write("<" + tag + " " + pa + " " + ">")
            else:
                self._html.write("<" + tag + ">")
        else:
            self._html.write("<" + tag + "/>")

    def tr_finish(self):
        self._html.close()

if __name__ == "__main__":
    tr = HTML_Test_Report("test.html")

    tr.write_tag("html", True)
    tr.write_tag("head", True)
    tr.write_tag("title", True)
    tr.write_tag("title", False)
    tr.write_tag("head", False)
    tr.write_tag("body", True)
    tr.write_tag("body", False)
    tr.write_tag("html", False)

    tr.tr_finish()
