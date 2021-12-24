#! python3
#
# py_pdf_manipulator_frame.py
import src.func_pdf_split as splt
import logging
import os
import re
import sys
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import tkinter as tk
import tkinter.ttk as ttk


class ManipulatorFrame(tk.Frame):
    # Initialization function
    def __init__(self, parent):
        # Instantiate logger
        self.logger = logging.getLogger("PyPdfManipulator.ManipulatorFrame")
        self.logger.debug("__init__ started...")
        # Instantiate the frame for the tab
        tk.Frame.__init__(self, parent)

        # Setup rows and columns for the tab
        tk.Grid.rowconfigure(self, 0, weight=1)
        tk.Grid.rowconfigure(self, 1, weight=1)
        tk.Grid.rowconfigure(self, 2, weight=1)
        tk.Grid.rowconfigure(self, 3, weight=1)
        tk.Grid.rowconfigure(self, 4, weight=1)

        tk.Grid.columnconfigure(self, 0, weight=1)
        tk.Grid.columnconfigure(self, 1, weight=1)
        tk.Grid.columnconfigure(self, 2, weight=1)
        tk.Grid.columnconfigure(self, 3, weight=1)
        tk.Grid.columnconfigure(self, 4, weight=1)
        tk.Grid.columnconfigure(self, 5, weight=1)
        tk.Grid.columnconfigure(self, 6, weight=1)
        tk.Grid.columnconfigure(self, 7, weight=1)
        tk.Grid.columnconfigure(self, 8, weight=1)

        #############
        # Variables #
        #############
        # Setting up the variables for the operations
        self.inputFile = ''
        self.fileName = ''
        self.outputDir = ''
        self.outputFile = ''
        self.defaultDir = str(os.path.expanduser('~'))
        self.pageRange = ''
        # Defining allowed characters for input sanitization
        self.notAllowedFileName = re.compile(r'[\|\*\?\\"/:<>]')
        self.pageChars = set("0123456789-,")

        #######################
        # Row 0 - INPUT LABEL #
        #######################
        # A status
        # Input file label
        self.input_file_lbl = tk.Label(self, text='Select Source PDF File')
        # Input file label placement
        self.input_file_lbl.grid(
            row=0, column=0, columnspan=4, sticky='snw', padx=2, pady=2
        )

        #########################
        # Row 1 - INPUT WIDGETS #
        #########################
        # Input file entry widget
        self.input_file_entry = tk.Entry(self)
        # Input entry field placement
        self.input_file_entry.grid(row=1, column=0, columnspan=3, sticky='ew')

        # Input file selection button
        self.input_file_btn = ttk.Button(
            self, text='Select File', command=lambda: self.openFile()
        )
        # Input file selection button placement
        self.input_file_btn.grid(row=1, column=3, sticky='ew', padx=5, pady=5)

        ########################
        # Row 2 - OUTPUT LABEL #
        ########################
        # Output directory label
        self.out_dir_lbl = ttk.Label(self, text='Output Directory')
        # Output directory label placement
        self.out_dir_lbl.grid(
            row=2, column=0, columnspan=4, sticky='snw', padx=2, pady=2
        )

        ##########################
        # Row 3 - OUTPUT WIDGETS #
        ##########################
        # Output directory entry field
        self.out_dir_entry = tk.Entry(self)
        # Output directory entry field placement
        self.out_dir_entry.grid(row=3, column=0, columnspan=3, sticky='ew')

        # Output directory selection button
        self.out_btn = ttk.Button(
            self, text='Select Directory', command=lambda: self.getDir()
        )
        # Output directory selection button placement
        self.out_btn.grid(row=3, column=3, sticky='ew', padx=5, pady=5)

        #############################
        # Row 4 - OUTPUT FILE LABEL #
        #############################
        # Output file name label
        self.outfile_name_lbl = ttk.Label(self, text='Output File Name')
        # Output file name label placement
        self.outfile_name_lbl.grid(
            row=4, column=0, columnspan=4, sticky='snw', padx=2, pady=2
        )

        ##############################
        # Row 5 - OUTPUT FILE WIDGET #
        ##############################
        # Output file entry field
        self.outfile_name_entry = tk.Entry(self)
        # Output file entry feild placement
        self.outfile_name_entry.grid(
            row=5, column=0, columnspan=4, sticky='ew'
        )

        ############################
        # Row 6 - PAGE RANGE LABEL #
        ############################
        # Page range label
        self.page_rng_lbl = ttk.Label(
            self, text='Page Range Selection (I.e. 1-2,5)'
        )
        # Page range label placement
        self.page_rng_lbl.grid(
            row=6, column=0, columnspan=4, sticky='snw', padx=2, pady=2
        )

        ##############################
        # Row 7 - PAGE RANGE WIDGETS #
        ##############################
        # Page Range entry field
        self.page_rng_entry = tk.Entry(self)
        # Page Range entry field placement
        self.page_rng_entry.grid(row=7, column=0, columnspan=4, sticky='ew')

        ###########################
        # Row 8 - PROCESS BUTTONS #
        ###########################
        # Process button
        self.process_btn = ttk.Button(
            self, text='Process', command=lambda: self.splitFile()
        )
        # Process button placement
        self.process_btn.grid(row=8, column=1, sticky='ew', padx=5, pady=5)
        # Quit button
        self.quit_btn = ttk.Button(
            self, text='Quit', command=lambda: self.quit()
        )
        # Quit button placement
        self.quit_btn.grid(row=8, column=2, sticky='ew', padx=5, pady=5)

        self.logger.debug("...__init__ complete")

    #############
    # Functions #
    #############
    # Get the PDF to be split
    def openFile(self):
        # Open file dialog to get user specified PDF file
        self.inputFile = fd.askopenfilename(
            initialdir=self.defaultDir, title="Select file",
            filetypes=(("PDF files", "*.pdf"), ("all files", "*.*"))
        )
        # Split the selected file into path and file to allow program to store
        # the directory the file was selected from as the default
        self.defaultDir, self.fileName = os.path.split(self.inputFile)
        # Delete any contents that may be in the entry widget
        self.input_file_entry.delete(0, tk.END)
        # Insert the contents of the inputFile variable into the entry widget
        self.input_file_entry.insert(0, self.inputFile)

    # Get the directory into which the new file will go
    def getDir(self):
        # Open directory selection dialog
        self.outputDir = fd.askdirectory(
            initialdir=self.defaultDir, title="Select Save Directory"
        )
        # Delete any contents that may be in the entry widget
        self.out_dir_entry.delete(0, tk.END)
        # Insert the contents of the outputDir variable into the entry widget
        self.out_dir_entry.insert(0, self.outputDir + '\\')

    # Check all fields to ensure that the values are legitimate
    def sanitizeInputs(self):
        # Check the entry widget contents for input file
        self.inputFile = self.input_file_entry.get()
        if os.path.isfile(self.inputFile):
            pass
        else:
            mb.showwarning(
                title="Input File Warning",
                message="The input file is invalid"
            )
            return

        # Check the entry widget contents for output directory
        self.outputDir = self.out_dir_entry.get()
        if os.path.isdir(self.outputDir):
            pass
        else:
            mb.showwarning(
                title="Save Path Warning",
                message="The output path does not exist"
            )
            return

        # Check the entry widget contents for file name
        self.outputFile = self.outfile_name_entry.get()
        if self.notAllowedFileName.search(self.outputFile) is \
                None and self.outfile_name_entry.get() != '':
            pass
        else:
            mb.showwarning(
                title="Output Filename Warning",
                msg="The file name specified is invalid"
            )
            return

        # Check the entry widget contents for page range
        self.pageRange = (self.page_rng_entry.get()).replace(' ', '')
        # Delete any contents that may be in the entry widget
        self.page_rng_entry.delete(0, tk.END)
        # Insert the contents of the outputDir variable into the entry widget
        self.page_rng_entry.insert(0, self.pageRange)
        if self.pageChars.issuperset(self.page_rng_entry.get()):
            pass
        else:
            mb.showwarning(
                title="Page Range Warning",
                msg="The page range specified is invalid"
            )
            return

    def splitFile(self):
        check = self.sanitizeInputs()
        if check is None:
            split = splt.PdfMod()

            split.addInput(self.inputFile)
            split.addPageRange(self.pageRange)
            split.addOutDir(self.outputDir)
            split.addOutput(self.outputFile)

            split.pdfSplit()
            mb.showinfo(
                win_title='Success',
                msg="Operation completed"
            )
        else:
            return

    # Quit button...it quits the program
    def quit(self):
        sys.exit()
