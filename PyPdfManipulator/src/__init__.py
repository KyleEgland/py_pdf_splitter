#! python3
#
# Main program for a GUI with tkinter
# Import information
# tkinter = GUI module, used to construct GUI
# ttk = tkinter styling module, more GUI stuff
import logging
from src.py_pdf_manipulator_frame import ManipulatorFrame
import tkinter as tk
import tkinter.ttk as ttk


class PyPdfManipulator(tk.Tk):
    def __init__(self, Config, *args, **kwargs):
        self.logger = logging.getLogger("PyPdfManifpulator.MainWindow")
        self.logger.debug("__init__ started...")

        self.Config = Config

        tk.Tk.__init__(self, *args, **kwargs)
        # Give the window an icon (must be in dir desginated)
        # tk.Tk.iconbitmap(self, default='icons/example_icon.ico')
        # Give the window a title (displayed in title bar; top of window)
        tk.Tk.wm_title(self, 'Py PDF Splitter')

        # Create the Notebook widget that will comprise the main part
        # of the application
        self.mainframe = ManipulatorFrame(self)
        # Use pack geometry to fill window with the Notebook widget
        self.mainframe.pack(fill='both', expand=True)

        menu_bar = tk.Menu(self)

        file_menu = tk.Menu(menu_bar, tearoff=0)

        file_menu.add_command(label='New Thing', accelerator='Ctrl+N')
        file_menu.add_command(label='Load Thing', accelerator='Ctrl+L')
        file_menu.add_command(label='Save Thing', accelerator='Ctrl+S')

        menu_bar.add_cascade(label='File', underline=0, menu=file_menu)

        self.config(menu=menu_bar)
