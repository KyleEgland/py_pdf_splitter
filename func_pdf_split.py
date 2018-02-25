#! python3
from PyPDF2 import PdfFileWriter
from PyPDF2 import PdfFileReader


class PdfMod():

    def __init__(self):
        # Start by taking an input file, specifying output file, and page range
        self.inFile = ""
        self.outFile = ""
        self.outDir = ""

        self.pageRange = ""

        # Instantiate the PdfFileWriter
        self.output = PdfFileWriter()

    def addInput(self, inFile):
        self.inFile = inFile
        # Instantiate PdfFileReader
        self.inputPdf = PdfFileReader(open(self.inFile, "rb"))

    def addPageRange(self, pageRange):
        self.pageRange = pageRange

    def addOutDir(self, outDir):
        self.outDir = outDir

    def addOutput(self, outputFile):
        if self.outDir == "":
            # Assign output file variable
            self.outFile = outputFile
            # Create the actual Output.pdf file
            self.outputFile = open(self.outFile, "wb")
        else:
            self.outFile = self.outDir + outputFile
            self.outputFile = open(self.outFile, "wb")

    def pdfSplit(self):
        # Splitting the page_range into a sequential python list of pages to
        # extract
        self.pageRanges = (x.split("-") for x in self.pageRange.split(","))
        self.rangeList = [i for r in self.pageRanges for i in range(int(r[0]),
                                                                    int(r[-1])
                                                                    + 1)]
        # Copy the page from the input and save to the output
        for p in self.rangeList:
            # Subtract 1 to deal with 0 index
            self.output.addPage(self.inputPdf.getPage(p - 1))

        self.output.write(self.outputFile)
