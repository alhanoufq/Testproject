#Empty set
thisset = {}
print(thisset)

#Create set
thisset ={"A","B","T","H","W"}
print(thisset)
thisset ={"Sara","Raneem",3,6,90,6}
print(thisset)

#access items
num ={"bader","salma","sara","kareem","ethair","sadeem"}
for x in num:
    print(x)

#Check if "yellow" is present in the set
x ={"red","yellow","green"}
print("yellow" in x)

#change items
#add()method
x ={"red","yellow","green"}
x.add("white")
print(x)
#update()method
color = {"red","yellow","green"}
color.update(["white","black","orange"])
print(color)

