# -*- coding: utf-8 -*-

import PyPDF2
import re
import os
from web import session


class PDF:

    def __init__(self, path, filename):
        self.path = path
        self.filename = filename
        self.src = os.path.join(path, filename)
        self.text = ""
        self.cnjs = []
        self.__read_pdf()

    def __read_pdf(self):
        self.pdf_file_io = open(self.filename, 'rb')
        self.pdf_file_reader = PyPDF2.PdfFileReader(self.pdf_file_io)
        for page in self.pdf_file_reader.pages:
            self.text += page.extractText()
        self.cnjs = re.findall("\d{7}-\d{2}\.\d{4}\.\d{1}\.\d{2}\.\d{4}", self.text)


path = ""
file = "Ceará.pdf"
pdf = PDF(path, file)
print(len(pdf.cnjs))
for cnj in pdf.cnjs:
    print(cnj)
    s = session.Session(cnj=cnj)
    s.consult_process()
    print(len(s.returned_processes))


s = session.Session(cnj="0700688-74.2018.8.02.0060")
s.consult_process()
print(len(s.returned_processes))
print(s.results)