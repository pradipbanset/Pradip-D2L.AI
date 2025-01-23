# def happy_birthday(name, age):
#     print(f"Happy Birthday to {name}!")
#     print(f"You are {age}!")
#     print(f"Happy Birthday dear {name}!")
#     print(f"You are {age} !")

# happy_birthday("pradip",21)

# def display_invoice(username, amount, due_date):
#     print(f"derar {username}")
#     print(f"your pending amount is {amount:} and  due date {due_date}")
    

# display_invoice("pradip", 1000.000, "poush-18")

##return - tstement used to end the function and return the value to the caller

# def add(a,b):
#     return a+b 

# def sub(a,b):
#     return a-b

# def mul(a,b):
#     return a*b

# print(add(10,20))
# print(sub(10,20))
# print(mul(10,20))


#lets create a function that takes full name 

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last
full_name = create_name("pradip", "basnet")
print(full_name)

 