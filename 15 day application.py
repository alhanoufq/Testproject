#List Length
thelist =["N","F","O","E","Q","Z","K"]
print(len(thelist))

#Add Items
thelist =["N","F","O","E","Q","Z","K"]
thelist.append("H")
thelist.append("S")
print(thelist)

#Add specified items
thelist =["N","F","O","E","Q","Z","K"]
thelist.insert(3,"H")
print(thelist)

#Remove Item
thelist =["N","F","O","E","Q","Z","K"]
thelist.remove("Q")
print(thelist)
thislist =["Ali","Omar","Nasser","Ali"]
thislist.remove("Ali")
print(thislist)

#pop()method
thelist =["mona","farah","yarah","sara"]
thelist.pop()
print(thelist)
thelist =["mona","farah","yarah","sara"]
thelist.pop(1)
print(thelist)

#clear() method
thelist =["mona","farah","yarah","sara"]
thelist.clear()
print(thelist)

#Copy a List
thislist =["apple","banana","cheery"]
mylist = thislist.copy()
thislist.pop(1)
print(mylist)
print(thislist)

#list() method
thislist =["mona","farah","yarah","sara"]
mylist =list(thislist)
print(mylist)

#The list() Constructor
thislist =list(("A","B","C","D"))
print(thislist)





