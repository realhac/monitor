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
            self._html.write("</" + tag + ">")

    def trFinish(self):
        self._html.close()

    def importTableCss(self):
        fp = open("../css/table.css", "rb")
        fc = fp.read();
        self._html.write(fc)
        fp.close()

    def drawTableHead(self, head_name):
        self.writeTag("li", True, ['class="bt"'])
        self._html.write(head_name)
        self.writeTag("li", False)

    def drawTableBody(self, cell_name):
        self.writeTag("li", True)
        self._html.write(cell_name)
        self.writeTag("li", False)

    def drawTable(self, cell_name):
        self.writeTag("div", True, ['id="tb"'])
        self.writeTag("ul", True)
        
        self.drawTableHead(cell_name)
        self.drawTableHead(cell_name)
        self.drawTableHead(cell_name)
        self.drawTableHead(cell_name)

        self.writeTag("ul", False)
        self.writeTag("div", False)

if __name__ == "__main__":
    tr = HTML_Test_Report("test.html")

    tr.writeTag("html", True)
    tr.writeTag("head", True)
    tr.writeTag("title", True)
    tr.writeTag("title", False)

    tr.importTableCss()

    tr.writeTag("head", False)
    tr.writeTag("body", True)

    tr.drawTable("0")

    tr.writeTag("body", False)
    tr.writeTag("html", False)

    tr.trFinish()
