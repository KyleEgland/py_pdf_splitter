#! python
#
# __main__.py
from config import Config
from src import PyPdfManipulator


Config = Config()

app = PyPdfManipulator(Config)

app.mainloop()
