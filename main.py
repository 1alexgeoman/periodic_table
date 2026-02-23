import tkinter as tk
from tkinter import ttk
from periodic_table_page import PeriodicTablePage
from element_page import ElementPage

class PeriodicTable(tk.Tk):
    def __init__(self):
        #Create the page
        super().__init__()
        #Add title to the page
        self.title("Interactive Periodic Table")
        #Set minimum size to the oage
        self.minsize(1200, 600)

        #Create a dictionary to store the frames for the differet pages
        self.frames = {}
        self.container = ttk.Frame(self)
        #Make the container expand to the full size of the frame when run
        self.container.pack(fill="both", expand=True)

        #Load the periodic table page and place it on the screen
        self.frames["table"] = PeriodicTablePage(self.container, self)
        self.frames["table"].pack(fill="both", expand=True)

    #If the element is select then load
    def show_element_page(self, element):
        #Error handling to prevent it opening twice
        if "element" in self.frames:
            self.frames["element"].destroy()

        self.frames["element"] = ElementPage(self.container, self, element)
        self.frames["element"].pack(fill="both", expand=True)
        self.frames["table"].pack_forget()

    def show_table(self):
        #Hides the element page if its still visible and then shows the periodic table
        self.frames["element"].pack_forget()
        self.frames["table"].pack(fill="both", expand=True)

if __name__ == "__main__":
    app = PeriodicTable()
    app.mainloop()