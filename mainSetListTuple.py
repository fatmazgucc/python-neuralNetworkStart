# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def listAndTuple(): #Tuple can not be changed later. It is immutable
    #List can be changed. Allows to duplication
    lst = ['a', 'b', 'c', 'd', 'e']  # This is how to initialize list
    tpl = ('x', 'y', 'z', 'w', 't')  # This is how to initialize tuple
    print('Lst values 1 are : ')
    print(lst)
    print('Tpl values 2 are:')
    print(tpl)
    print()
    lst[1] = 'bb'
    print('Lst values 3 are : ')
    print(lst)
    lst.append('x')
    print('Lst values 4 are : ')
    print(lst)
    lst.insert(2, 'ff')
    print('Lst values 5 are : ')
    print(lst)
    lst.remove('a')
    print('Lst values 6 are : ')
    print(lst)
    del lst[0]
    print('Lst values 7 are : ')
    print(lst)


def forSet():
    #Set is unordered, mutable(can be changed), no duplication
    st = set()
    st = {'a', 'b', 'c', 'd', 'e'}
    print('Values of set is ')
    print(st)
    #or
    st=set(['a', 'b', 'c'])
    print('Values of set 1 is ')
    print(st)
    st.add('f')
    print('Values of set 2 is ')
    print(st)


# Press the green button in the gutter to run the script.

print_hi('We are starting :) Hello :)')

listAndTuple()
forSet()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
