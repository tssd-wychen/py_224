# -*- coding: utf-8 -*-
"""
target:extract page within key words, then merge thse pages in one
"""

from PyPDF2 import PdfFileReader, PdfFileWriter
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp mport PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator
import re
import os

fp = open('mypdf.pdf', 'rb')
# to create a pdf document parser for analysis
parser = PDFParser(fp)
# to create pdf document object for saving doc struct
document = PDFDocument(parser)
# check the pdf wether extractable
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
else:
    # create a PDF browser object for saving shared resource
    rsrcmgr = PDFResourceManager()
    # set para to analysis
    laparams = LAParams()
    # create a pdf device object
    # device = PDFDevice(rsrcmgr)
    device = PDFPageAggregator(rsrcmgr, laparams = laprams)
    # 创建一个PDF解释器对象
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # 处理每一页
    pageindex = []
    i = 0
