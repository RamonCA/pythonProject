import Tkinter as tk    # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filename)