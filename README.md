# 🧪 Interactive Periodic Table (Python/Tkinter)

**Interactive Periodic Table** is a cross-platform desktop application designed to provide a comprehensive and visual exploration of chemical elements. Built with **Python** and **Tkinter**, it offers a dynamic user interface where users can interact with elements to reveal deep technical data, from atomic properties to chemical uses.

## 🚀 Key Features

* **Interactive Grid UI:** A fully responsive periodic table layout with color-coded categories (Alkali metals, Noble gases, Transition metals, etc.) for instant visual identification.
* **Dynamic Data Loading:** Utilizes a robust backend JSON parser to load and display data for 118 elements, ensuring content flexibility and easy updates.
* **Detailed Element Profiles:** Clicking an element reveals a dedicated page with:
    * **Atomic Properties:** Atomic number, mass, and electron configuration.
    * **Chemical Behavior:** Oxidation states and phase at STP.
    * **Physical Constants:** Melting and boiling points in Kelvin.
    * **Real-world Applications:** Bulleted lists of common uses (e.g., Hydrogen for rocket fuel).
* **State Management:** Implements a controller-based navigation system to transition seamlessly between the table view and individual element pages.

## 🛠️ Project Structure

* **`main.py`**: The application entry point; manages frame switching and the main window loop.
* **`periodic_table_page.py`**: Handles the complex grid logic, category-based color mapping, and UI hover effects.
* **`element_page.py`**: A template-driven view that populates technical data for whichever element is selected.
* **`data_loader.py`**: Middleware that parses the JSON chemical database into Python-accessible objects.

## 🚀 Technical Stack

* **Language:** Python 3.x
* **GUI Library:** Tkinter / TTK (Standard Python Interface)
* **Data Format:** JSON (JavaScript Object Notation)

## 🕹️ How to Use

1. **Explore:** Hover over any element to highlight it.
2. **Details:** Left-click an element to open its technical profile.
3. **Navigation:** Use the "Back to Periodic Table" button to return to the main grid.

---
> **Note:** This project demonstrates proficiency in GUI development, data structures, and the ability to translate scientific data into intuitive software interfaces.