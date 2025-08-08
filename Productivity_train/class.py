#  A class is like  a blueprint or template to create something called object.
# Object = a specfic instance buit from that class.





# class Dog:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age

#     def bark(self):
#         print("Woof! My name is", self.name)

# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Max", 5)



class book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def show_info(self):
        print(f"'{self.title} by {self.author}")

book1 = book("Harry Potter", "J.k Rowling")
book2 = book("Atomic Habits", "James Clear")

book1.show_info()
book2.show_info()