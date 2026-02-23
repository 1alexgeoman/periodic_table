import tkinter as tk
from tkinter import ttk

class ElementPage(ttk.Frame):
    def __init__(self, parent, controller, element):
        super().__init__(parent)
        self.controller = controller

        #Create a title for the page based on the element name
        title = tk.Label(self, text=element['name'], font=('Arial', 24, 'bold'))
        title.pack(pady=10)

        #Put the symbol on the page
        symbol = tk.Label(self, text=f"Symbol: {element['symbol']}", font=('Arial', 16))
        symbol.pack()

        #Put the atomic number and mass on the page
        atomic_info = tk.Label(self, text=f"Atomic Number: {element['atomic_number']}\n" f"Atomic Mass: {element['atomic_mass']}",font=('Arial', 14))
        atomic_info.pack(pady=5)

        #put the electron configuration on the page
        config = tk.Label(self,text=f"Electron Configuration: {element['electron_configuration']}",font=('Arial', 12),wraplength=800, justify='left')
        config.pack(pady=5)

        #Put the oxidation states on the page
        oxidation_states_list = []
        if element['oxidation_states'] == 'Unknown':#If the oxidation states are unknown then add that to the list to be displayed to the user
            oxidation_states_list.append("Unknown")
        else:
            for state in element['oxidation_states']:#Else add every oxidation state to the list to be displayed to the user
                oxidation_states_list.append(str(state))
        oxidation_states = ", ".join(oxidation_states_list)
        ox_label = tk.Label(self, text=f"Oxidation States: {oxidation_states}", font=('Arial', 12))
        ox_label.pack(pady=5)

        #Add the common uses of the element to the page
        uses_label = tk.Label(self, text="Common Uses:", font=('Arial', 12, 'bold'))
        uses_label.pack(pady=(10, 0))
        for use in element['common_uses']:
            tk.Label(self, text=f"• {use}", font=('Arial', 12)).pack()

        #add the general properties about the element to the page
        gp = element.get('general_properties', {})
        general_props = (f"\nPhase at STP: {gp.get('phase_at_stp', 'N/A')}\n" f"Melting Point: {gp.get('melting_point', 'N/A')} K\n" f"Boiling Point: {gp.get('boiling_point', 'N/A')} K")
        gp_label = tk.Label(self, text=general_props, font=('Arial', 12))
        gp_label.pack(pady=10)

        #Add the element groups to the page
        eg = element.get('element_groups', {})
        group_info = (f"Category: {eg.get('category', 'N/A')}\n" f"Block: {eg.get('block', 'N/A')}")
        group_label = tk.Label(self, text=group_info, font=('Arial', 12))
        group_label.pack(pady=5)

        #Add a buton to go back to the periodic table page
        back_button = ttk.Button(self, text="Back to Periodic Table", command=self.controller.show_table)
        back_button.pack()