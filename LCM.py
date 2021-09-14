def sort_by_age(e):
    return e['age']

def sort_by_name(e):
    return e['name']

myList = [
    {'name': 'sukanta', 'age': 12},
    {'name': 'rajib', 'age': 22},
    {'name': 'shymal', 'age': 25},
    {'name': 'ani', 'age': 9}
]
myList.sort(reverse=False, key=sort_by_name)
print(myList)
