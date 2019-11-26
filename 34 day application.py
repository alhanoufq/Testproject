#Passing a List as a Parameter
def my_function(food):
    for x in food:
        print(x)
fruits=['apple','banana','cherry']

my_function(fruits)

#Return Values
def my_function(x):
    return 5*x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#Keyword Arguments
def my_function(child3,child2,child1):
    print("the youngest child is" + child3)
my_function(child1="Emil",child2="Tobias",child3="Linus")

#Arbitrary Arguments
def my_function(*kids):
    print("the youngest child is "+ kids[2])
my_function('Emil','Tobias','Linus')

# Recursion
def tri_recursion(k):
    if(k>0):
        result=k+tri_recursion(k-1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)

