#Format - Strings

#To specify a string as an f-string, 
# simply put an f in front of the string literal,
# and add curly brackets {} as placeholders for 
# variables and other operations.

#F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#Placeholders and Modifiers
#A placeholder can contain variables, operations,
#functions, and modifiers to format the value.

price = 59.56852
txt = f"The price is {price:.2f} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)

#can perform if...else statements inside the placeholders
price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)

#Execute Functions in F-Strings
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

#can create user defined functions and use them
def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

#Use a comma as a thousand separator
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)

#Binary format
txt = f"The binary version of 5 is {5:b}"
print(txt)

#decimal number format
txt = f"We have {0b101:d} chickens."
txt1 = f"we have {0b1101:d} burgers."
print(txt)
print(txt1)

#format() method can still be used, 
# but f-strings are faster and the preferred way to 
#format strings..

price = 23
txt = "the price is {} rupees"
print(txt.format(price))
txt = "The price is {:.2f} dollars"
print(txt.format(price))

#Multiple Values
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))

#Index Numbers
quantity = 3
itemno = 567
price = 49
myorder = "I want {1} pieces of item number {0} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

# refer to the same value more than once, use the index number
age = 34
name = "john"
txt = "his name is {1} , {1} is {0} years old"
print(txt.format(age,name))

#Named Indexes
my_order = "I have a {carname},it is a {model}."
print(my_order.format(carname = 'Ford' , model = 'Mustang'))
