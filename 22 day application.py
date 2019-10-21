#Empty dictionary
thisdic= {}
print(thisdic)

#Create dictionary
thisdict={"brand":"Ford",
          "model":"Mustang",
          "year":1964
          }
print(thisdict)

#Access items
thisdict={"brand":"Ford",
          "model":"Mustang",
          "year":1964
          }
x=thisdict["model"]
print(x)

thisdict={"brand":"Ford",
          "model":"Mustang",
          "year":1964
          }
x=thisdict.get("model")
print(x)

#change values
thisdict={"brand":"Ford",
          "model":"Mustang",
          "year":1964
          }
thisdict["year"]=2018
print(thisdict)

#Loop through a dictionary
thisdict={"brand":"Ford",
          "model":"Mustang",
          "year":1964
          }
for x in thisdict:
    print(x)

#Print all values in the dictionary, one by one
thisdict={"brand":"Ford",
          "model":"Mustang",
          "year":1964
          }
for x in thisdict:
    print(thisdict[x])

#values() function
thisdict={"brand":"Ford",
          "model":"Mustang",
          "year":1964
          }
for x in thisdict.values():
    print(x)

# items() function
thisdict={"brand":"Ford",
          "model":"Mustang",
          "year":1964
          }
for x ,y in thisdict.items():
    print(x,y)
