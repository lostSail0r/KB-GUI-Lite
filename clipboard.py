#######################################
# Chris Grady						  #
# Simple Clipboard Function (Windows) #
# #####################################
from tkinter import Tk

def clippy(word):
	r = Tk()
	copied = word
	r.withdraw()
	r.clipboard_clear()
	r.clipboard_append(copied)
	r.update()
	r.destroy()

def clippyOD():
	copiedOD = input("Enter Text to be copied: ")
	clippy(copiedOD)

if __name__ == "__main__":
    clippyOD()