import pickle
# Creating an empty dictionary
myDict = {}

# Adding list as value
myDict["key1"] = {'roll': 10, 'name': 'Sukanta Das'}
myDict["key2"] = {'roll': 5, 'name': 'Rabin Kanti Halder'}

# print(myDict)

print(myDict["key2"]["roll"])

example_dict = {1:"6",2:"2",3:"f"}

binary_file = open("sukanta_binary.hui","wb")
pickle.dump(myDict, binary_file)
binary_file.close()

binary_file = open("sukanta_binary.hui","rb")
loaded_dict = pickle.load(binary_file)
print(loaded_dict)