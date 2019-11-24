#The range() Function
for x in range(7):
    print(x)


#determine starting value
for x in range(2,6):
    print(x)
#determine increment value
for x in range(2,30,3):
    print(x)

#Else in For Loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")

#nested loops
adj=['red','big','tasty']
fruits=['apple','banana','cherry']
for x in adj:
    for y in fruits:
        print(x,y)