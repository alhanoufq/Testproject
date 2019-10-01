#Check if Item Exists
thistuple = ("red","green","blue","yellow")
if "blue" in thistuple:
   print("yes,'blue' is the color tuple")
#Repeat Item
thistuple =("love",)*5
print(thistuple)
#+ Operator in Tuple
x =(3,4,5,6)
x = x+(1,2,3)
print(x)
#Tuple Length
num =(4,6,9,3,8,46,4)
print(len(num))
#The tuple() Constructor
thislist=[3,4,5,6,"A","B"]
thistuple=tuple(thislist)
print(thistuple)
#count tuple
thistuple =(4,7,2,8,5,5,5,4,5)
x=thistuple.count(5);
print("Number 5 exists", x,"in the tuple")
#index tuple
num =(1,2,3,4,5)
print(num.index(3))
print(num.index(4,1))



