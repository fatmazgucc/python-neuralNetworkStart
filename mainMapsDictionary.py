# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def dictionary():
    d = {'name': 'Hsn', 'address': 'Kartal'}
    print('Values of d :')
    print(d)
    print(f"Name of d.name is {d['name']} ")
    if 'name' in d:
        print('Name is in d')
    if 'surname' not in d:
        print('Surname is not in d ')  # There is no such element in d
    d2 = [{"name": "fato", "pets": ["cat", "horse"]}, {"name": "Hsn"}, {"name": "hkg", "pets": "dog"}]
    for d_val in d2:
        print(
            f"{d_val['name']} : {d_val.get('pets', 'no_pets')} ")  # if d does not have pets, it prints no_pets as default on .get() method



def addition(n):
    return n + n


def mapFor():
    # The map function takes a list and applies a function to each member of the list and returns a second list that is the same size as the first
    print("on map function")
    lst = [2, 8, 5]
    print("lst values 1 is ")
    print(lst)

    lst = map(addition, lst)
    print("lst values 2 is ")
    print(lst) #it is map object now
    print("lst values 3 is ")
    print(list(lst)) #it doubles each of lst elements


# Press the green button in the gutter to run the script.
dictionary()
mapFor()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
