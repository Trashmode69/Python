dict_names = {"David": 10000, "Misha": 20000, "Slava": 30000, "Alina": 40000,}
print(dict_names)
summary = dict_names["David"]+dict_names["Misha"]+dict_names["Slava"]+dict_names["Alina"]
print("The summary is: " + str(summary))
dict_names.update({"Sveta":dict_names})
dict_names.update({"Mark":dict_names})
print(dict_names)
print("Number of entries: " + str(len(dict_names)))
