age=36
txt="My name is john,and Iam {}"
print(txt.format(age))

quantity=3
itemno=567
price=49.95
myorder="I want{} pieces of item {} for {} dollors."
print(myorder.format(quantity,itemno,price))

quantity=3
itemno=567
price=49.95
myorder="I want to pay {2} dollors for {0} pieces of item {1}."
print(myorder.format(quantity,itemno,price))

