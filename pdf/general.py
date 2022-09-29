# -*- coding: utf-8 -*-

import PyPDF2
import re
import os
from web import session


class PDF:

    def __init__(self, path, filename, number_pages):
        self.path = path
        self.filename = filename
        self.src = os.path.join(path, filename)
        self.number_pages = number_pages
        self.text = ""
        self.cnjs = []
        self.__read_pdf()

    def __read_pdf(self):
        self.pdf_file_io = open(self.filename, 'rb')
        self.pdf_file_reader = PyPDF2.PdfFileReader(self.pdf_file_io)
        for page in self.pdf_file_reader.pages[:self.number_pages]:
            self.text += page.extractText()
        self.cnjs = re.findall("\d{7}-\d{2}\.\d{4}\.\d{1}\.\d{2}\.\d{4}", self.text)


if __name__ == "__main__":
    # is currently processing only 10 pages
    number_pages = 10
    files = "alagoas_test.pdf", "ceara_test.pdf"
    for file in files:
        pdf = PDF("", file,number_pages)
        print("number of processes to be processed", len(pdf.cnjs))
        for cnj in pdf.cnjs:
            s = session.Session(cnj=cnj)
            s.consult_process()
            print(cnj, s.results)
