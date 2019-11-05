#Check if Key Exists
thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
if "model" in thisdict:
    print("Yes,'model' is one of the keys in the thisdict dictionary")

#Dictionary Length
thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
print(len(thisdict))

#Adding Items
thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964
}
thisdict["color"]="red"
print(thisdict)

#Removing Items
thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964,
    "color":"red"
}
thisdict.pop("model")
print(thisdict)

#popitem()method
hisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964,
    "color":"red"
}
thisdict.popitem()
print(thisdict)

#clear()method
hisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964,
    "color":"red"
}
thisdict.clear()
print(thisdict)

