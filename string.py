
#String in python are surrounded by either single quotation marks, or double quotation marks. 

print("Hello")
print("Hello")
print("It's alright")


# Quotes Inside Quotes 
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Assign String to Variable 
a = "Hello"
print(a)


# Multiline String 
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua"""

print (a)



# String are Arrays 
a = "Hello, World!"
print (a[1])

# Looping through a string 
for x in "banana":
    print(x)
    
# String Length 
a = "Hello, World!"
print(len(a))

# Check String
txt = "The best thing in life are free!"
if "free" in txt:
    print("Yes, 'free' is present")


# Check if Not 
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No,'expensive' is NOT present")

