#Two functions to display name and age

#The get age function takes only integer
def get_age():
    age = int (input("Enter your age:"))
    return (print("You are" ,age, "years old"))


#The get name function takes only strings
def get_name():
    name = str(input("Enter your name:"))
    return (print(name, "is your name."))

print (get_name(),get_age())

