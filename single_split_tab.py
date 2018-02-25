#! python3
#
# This tab will allow user to add a single PDF, specify how it should be split
# then allow for the split contents to be put into a single output PDF.
# tkinter = GUI module, used to construt the GUI
# ttk = tkinter styling, more GUI stuff
import tkinter as tk
import tkinter.ttk as ttk
import func_pdf_split


class SingleSplitTab(tk.Frame):
    # Initialization function
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        # The "rowconfigure" and "columnconfigure" tell the program
        # how to resize widgets when the window is resized
        # Weight affects how the item will be scaled in relation
        # to the other elements that are bing re-sized
        # E.g. a row with weight 1 will scale more than a row with weight 2
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

        #######################
        # Row 0 - INPUT LABEL #
        #######################
        # A status
        # Input file label
        self.input_file_lbl = tk.Label(self, text='Select Source PDF File')
        # Input file label placement
        self.input_file_lbl.grid(row=0, column=0, columnspan=4, sticky='snw',
                                 padx=2, pady=2)

        #########################
        # Row 1 - INPUT WIDGETS #
        #########################
        # Input file entry widget
        self.input_file_entry = tk.Entry(self)
        # Input entry field placement
        self.input_file_entry.grid(row=1, column=0, columnspan=3, sticky='ew')

        # Input file selection button
        self.input_file_btn = ttk.Button(self, text='Select File')
        # Input file selection button placement
        self.input_file_btn.grid(row=1, column=3, sticky='ew', padx=5, pady=5)

        ########################
        # Row 2 - OUTPUT LABEL #
        ########################
        # Output directory label
        self.out_dir_lbl = ttk.Label(self, text='Output Directory')
        # Output directory label placement
        self.out_dir_lbl.grid(row=2, column=0, columnspan=4, sticky='snw',
                              padx=2, pady=2)

        ##########################
        # Row 3 - OUTPUT WIDGETS #
        ##########################
        # Output directory entry field
        self.out_dir_entry = tk.Entry(self)
        # Output directory entry field placement
        self.out_dir_entry.grid(row=3, column=0, columnspan=3, sticky='ew')

        # Output directory selection button
        self.out_btn = ttk.Button(self, text='Select Directory')
        # Output directory selection button placement
        self.out_btn.grid(row=3, column=3, sticky='ew', padx=5, pady=5)

        #############################
        # Row 4 - OUTPUT FILE LABEL #
        #############################
        # Output file name label
        self.outfile_name_lbl = ttk.Label(self, text='Output File Name')
        # Output file name label placement
        self.outfile_name_lbl.grid(row=4, column=0, columnspan=4, sticky='snw',
                                   padx=2, pady=2)

        ##############################
        # Row 5 - OUTPUT FILE WIDGET #
        ##############################
        # Output file entry field
        self.outfile_name_entry = tk.Entry(self)
        # Output file entry feild placement
        self.outfile_name_entry.grid(row=5, column=0, columnspan=4,
                                     sticky='ew')

        ############################
        # Row 6 - PAGE RANGE LABEL #
        ############################
        # Page range label
        self.page_rng_lbl = ttk.Label(self, text='Page Range Selection (I.e. \
1-2,5)')
        # Page range label placement
        self.page_rng_lbl.grid(row=6, column=0, columnspan=4, sticky='snw',
                               padx=2, pady=2)

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
        self.process_btn = ttk.Button(self, text='Process')
        # Process button placement
        self.process_btn.grid(row=8, column=1, sticky='ew', padx=5, pady=5)
        # Quit button
        self.quit_btn = ttk.Button(self, text='Quit')
        # Quit button placement
        self.quit_btn.grid(row=8, column=2, sticky='ew', padx=5, pady=5)
