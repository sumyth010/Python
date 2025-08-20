

# Loops are used to store multiple items in a single variables 

# mylist = ["apple", "banana", "cherry"]

thislist = ["apple", "banana", "cherry"]
print(thislist)

# List item are ordered , changeable , and allow duplicate values .
# This list is chnageable , meaning that we can change, add and remove items in a list after it has created . 


# Allow duplicates 
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# List length 
#  To determine how many items a list has , use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))




# list Items - Data Types
list1 = ["apple", "banana" , "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]


# the list () Constructor 
thislist = list (("apple", "banana", "cherry"))
# note the doubele round - brackets 
print(thislist)

















# Access List Items 
thislist = ["apple", "banana", "cherry"]
print(thislist[1])


# Range of Index 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Ranage of Negative Indexes 
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-2:-5])

# Check if item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("yes, 'apple' is in the fruits list")






# Change List Items 
thislist = ["apple"]
