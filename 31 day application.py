#callong a function
def my_function():
    print("Hello my friends")
my_function()

#Parameters
def my_function(fname):
    print(fname+"Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

#Default Parameter Value
def my_function(country="Norway"):
    print("I am from"+country)

my_function("swedan")
my_function("India")
my_function()
my_function("Brazil")
