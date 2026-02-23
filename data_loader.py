import json

#Load the JSON data with all the chemical properties from a file
with open('chemical_properties.json', 'r') as file:
    elements_data = json.load(file)
#When the data is loaded, check if it is a list or a dictionary and then create a list of elements from it
if isinstance(elements_data, list):
    elements_list = []
    for item in elements_data:
        elements_list.append(item['element'])
else:
    elements_list = [elements_data['element']]