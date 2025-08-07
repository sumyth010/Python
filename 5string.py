
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















# String Slicing 
b =  "Hello, World! "
print(b[2:5])
# 

# Slice From the Start 
b = "Hello, World!"
print(b[:5])

# Slice to the end
b = "Hello, World!"
print(b[2:])

# Negative Indexing 
b = "Hello, World"
print(b[-5: -2])


















# Modify Strings 
# Upper Case
a = "Hello, World!"
print(a.upper())

# Lower Case
a = "Hello, World!"
print(a.lower())

# Remove Whitespace
a = "Hello, World! "
print(a.strip())
# returns "Hello, World!"

# Replace String 
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
a = "Hello, World!"
print(a.split(","))
# return ['Hello', 'World!']