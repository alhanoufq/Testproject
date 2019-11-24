# The For Loops
fruits=['apple','banana','cherry']
for x in fruits:
    print(x)

#Looping Through a String
fruits=['apple','banana','cherry']
for x in 'apple':
    print(x)

#the break
fruits=['apple','banana','cherry']
for x in fruits:
    print(x)
    if x=='banana':
     break

#The continue Statement
fruits=['apple','banana','cherry']
for x in fruits:
    if x=='banana':
     continue
    print(x)
