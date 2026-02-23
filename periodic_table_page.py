import tkinter as tk
from tkinter import ttk
from data_loader import elements_list

#Dictionary to store all the colours of the different types of elements
category_colors = {
    "Reactive non-metals": "#7FFF00",
    "Noble gas": "#FF1493",
    "Alkali metal": "#FFD700",
    "Alkaline earth metal": "#FF8C00",
    "Metalloid": "#32CD32",
    "Halogen": "#00FFFF",
    "Transition metal": "#FF4500",
    "Post-transition metal": "#4169E1",
    "Lanthanoid": "#9370DB",
    "Actinide": "#8B008B",
    "Unknown": "#00ffff"
}

class PeriodicTablePage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        #Set the title on the frame 
        title_label = tk.Label(self, text="Periodic Table", font=('Arial', 24, 'bold'))
        title_label.pack(pady=(0, 20))

        #Set the container to store all the items of the periodic table
        self.main_container = ttk.Frame(self)
        self.main_container.pack(expand=True, fill='both', padx=10, pady=10)

        #create a frame to hold the whole periodic table and then add a grid to whole main bit of the periodic table
        self.periodic_table_frame = ttk.Frame(self.main_container)
        self.periodic_table_frame.pack(expand=True, fill='both')
        for i in range(18):
            self.periodic_table_frame.grid_columnconfigure(i, weight=1)
        
        #create a frame to hold the f-blocks and add a grid to it
        self.f_block_frame = ttk.Frame(self.main_container)
        self.f_block_frame.pack(expand=False, fill='x')
        for i in range(15):
            self.f_block_frame.grid_columnconfigure(i+1, weight=1)

        #Call the function to create the periodic table
        self.create_periodic_table()

    def create_element(self, element):
        #Create a frame for each element in the periodic table and set the size of it 
        frame = tk.Frame(self.periodic_table_frame, width=70, height=70, bg=category_colors.get(element['element_groups']['category'], 'white'), highlightthickness=0, highlightbackground="black")

        #Add labels to the each element to show the atomic number, mass, symbol and name of the element
        tk.Label(frame, text=str(element['atomic_number']), bg=frame['bg'], font=('Arial', 8)).place(x=2, y=2)
        tk.Label(frame, text=f"{element['atomic_mass']:.1f}", bg=frame['bg'], font=('Arial', 8)).place(x=65, y=2, anchor='ne')
        tk.Label(frame, text=element['symbol'], bg=frame['bg'], font=('Arial', 16, 'bold')).place(relx=0.5, rely=0.45, anchor='center')
        tk.Label(frame, text=element['name'], bg=frame['bg'], font=('Arial', 8)).place(relx=0.5, rely=0.85, anchor='center')

        def on_enter(e): frame.config(highlightthickness=2)#Highlight the element when hovered over
        def on_leave(e): frame.config(highlightthickness=0)#Hide the highlight when not hovered over

        for child in frame.winfo_children():#Make sure every element has the same hover effect
            child.bind('<Enter>', on_enter)
            child.bind('<Leave>', on_leave)
            child.bind('<Button-1>', lambda e, el=element: self.controller.show_element_page(el))#Left click opens the element page

        return frame

    def create_periodic_table(self):
        #Create the elements that are in the periodic table and add them to the grid
        for element in elements_list:
            period = element['element_groups']['period']#Get the periodd of the element
            group = element['element_groups']['group']#Get the group of the element
            element_frame = self.create_element(element)#Create the element frame using the function from above
            element_frame.grid(row=period-1, column=group-1, padx=1, pady=1, sticky='nsew')#Place the element in the grid


            
       