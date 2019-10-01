#first
thislist = [56,7,8.34,7,4.6,8,10]
thislist.append(5)
print(thislist)
mylist = thislist.copy()
print(mylist)
print(thislist.index(7,2))


#second
tuple =("java","python","swift")
if "python"in tuple:
    print("yes,'python' is in the tuple")