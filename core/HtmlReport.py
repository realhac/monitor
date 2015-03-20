# -*- coding:utf-8 -*-

import os, sys

class HTML_Test_Report:
    def __init__(self, tr_name):
        self._html = open(tr_name, 'w')

    def writeCharset(self):
        self._html.write('<meta charset="utf-8">')

    def writeTag(self, tag, begin, para=[]):
        if begin:
            if para:
                self._html.write("<" + tag)
                for pa in para:
                    self._html.write(" " + pa + " ")
                self._html.write(">")
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

    def drawTableHead(self):
        self.writeTag("div", True, ['id="header_div"'])
        self.drawTableCell("状态码", "header_div_wd100")
        self.drawTableCell("失败信息", "header_div_wd250")
        self.drawTableCell("线上详情", "header_div_wd300")
        self.drawTableCell("预发布详情", "header_div_wd300")
        self.writeTag("div", False)

    def drawTableCell(self, cell_name, id):
        self.writeTag("div", True, ['id="'+id+'"'])
        self._html.write(cell_name)
        self.writeTag("div", False)

    def drawClear(self):
        self.writeTag("div", True, ['class="clr"'])
        self.writeTag("div", False)

    def drawTableRows(self):
        self.writeTag("div", True, ['id="rows_div"'])

        self.drawTableRow(["11111111111111111111","11111111111","111111111111111111111111","111"])
        self.drawTableRow(["22222","222222222222222222222222222222222222222222","2222222222222222","2222"])
        self.drawTableRow(["333333333333333333333","22222222222222222222222222","2222222222222222","2222"])

        self.writeTag("div", False)

    def drawTableRow(self, info):
        self.writeTag("div", True, ['id="row_div"'])

        self.writeTag("div", True, ['id="row_div_wd100"'])
        self.drawTableCell(info[0], "row_div_wd96")
        self.drawTableCell(info[0], "row_div_wd96")
        self.writeTag("div", False)

        self.drawTableCell(info[1], "row_div_wd250")

        self.writeTag("div", True, ['id="row_div_wd604"'])
        self.drawTableCell(info[2], "row_div_wd300")
        self.drawTableCell(info[2], "row_div_wd300")
        self.drawClear()
        self.drawTableCell(info[3], "row_div_wd300")
        self.drawTableCell(info[3], "row_div_wd300")
        self.drawClear()
        self.drawTableCell(info[3], "row_div_wd300")
        self.drawTableCell(info[3], "row_div_wd300")
        self.drawClear()
        self.writeTag("div", False)


        #self.drawTableCell(info[0], "row_div_wd100")
        #self.drawTableCell(info[1], "row_div_wd250")
        #self.drawTableCell(info[2], "row_div_wd300")
        #self.drawTableCell(info[3], "row_div_wd300")
        self.drawClear()
        self.writeTag("div", False)

    def drawTable(self):
        self.writeTag("div", True, ['id="main_div"'])
     
        self.drawTableHead()
        self.drawTableRows()

        self.writeTag("div", False)

if __name__ == "__main__":
    tr = HTML_Test_Report("test.html")

    tr.writeTag("html", True)
    tr.writeTag("head", True)
    tr.writeCharset()
    tr.writeTag("title", True)
    tr.writeTag("title", False)

    tr.importTableCss()

    tr.writeTag("head", False)
    tr.writeTag("body", True)

    tr.drawTable()

    tr.writeTag("body", False)
    tr.writeTag("html", False)

    tr.trFinish()
