# a varibale is created the movement e assign it.
# python automatically reads the type of the varibale the movements its created 
# no need to specify the data type in python.
x = 10
print(x)
x = "salt"#reassigning to the string 
print (x)

#If you want to specify the data type of a variable, this can be done with casting.

x = str(5)
print(x)
print(type(x)) # get the tpe of the variable

#Variable names are case-sensitive.
# here A,a are different.
a = 4
A = "faffu"
print(a,A)
print(type(a),type(A))

#assign multiple values to variables

x,y,z = "do","mo","vu"
print(y)

#assign the same value to multiple variables in one line

x = y = z = "hehe"
print(z)

#Unpack a Collection

fruits = ["mango","banana","apple"]
x,y,z = fruits

print(x)

#Output Variables

v = "get me some water"
print(v)

#In the print() function, you output multiple variables, separated by a comma

print(x , v)

#You can also use the + operator to output multiple variables:

print(y +" "+ v + " and " + z)

#Global Variables
#variables that are created outside of the function
#these are accesable both inside and outside of the functions

g = "Hi there..!"

def greatings():
    print(g + "whatt.u.do..!!!") #g is used inside a function
print(g)
greatings()

#Local Variables
#tese variables are created inside the functions hich are accesable
#ithin the scope of that function.

x = "meaowww"

def sound():
    x = "tukktukk" #local variable which can be used only inside this function
    print("i hear.." + x)
sound()   
print("i hear.." + x)

#global keyword
#To create a global variable inside a function, you can use the global keyword.
#Also, use the global keyword if you want to change a global variable inside a function

h = "keekkk"
print("bus honk " + h)
def horn():
    global H 
    H = "peepppepeep"
    print("bike honk " + H)
    global h
    h = "turrtuuuu"
    print("car honk " + h)
horn()
print("bus honk " + h)

