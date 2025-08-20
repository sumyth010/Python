

# In programming you often need to know if an expression is True or false.

# Example 
print(10 > 9 )
print(10 == 9)
print(10 < 9)


# Example 2
a = 200
b = 33

if b > a :
    print ("b is greater than a ")
else:
    print("b is not greater tha a ")




# Evaluate Values and Variables 
# The bool()funaction allows you to evaluate any value, and give you True or False 
print (bool("Hello"))
print (bool("15"))


# Example 
x = "Hello"
y = 15

print (bool(x))
print (bool(y))





# Most Values are True 

# Some Values are Fasle 
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# Example 
class myclass():
    def __len__(self):
        return 0 

myobj = myclass()
print(bool(myobj))




# Function can Return a Boolen 
def myfunction():
    return True

print (myfunction)