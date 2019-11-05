#first
thisset={1,3,5,7,8}
thisset.update([4,8,12])
print(thisset)

#number 8 delete
thisset={1,3,5,7,8}
thisset.update([4,8,12])
thisset.remove(8)
print(thisset)

#set delete
thisset={1,3,5,7,8}
thisset.update([4,8,12])
thisset.remove(8)
#del thisset
print(thisset)

#second
info ={
    "name":"pigeon",
    "type":"brid",
    "skin cover":"feathers"
}
#type value print
print(info["type"])
#skin cover change
info["skin cover"]="wool"
print(info)