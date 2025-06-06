#string..
a = "Hello World" 
print(type(a))

#Integer...
b = 12
print(type(b))

#float..
c = 25.55
print(type(c))

#complex...
d = 1+5j
print(type(d))

#list...
e = ["apple", "banana", "cherry"]
print(type(e))

#Tuple...
f = ("bike", "car", "bus")
print(type(f))

#range...
g = range(6)
print(type(g))

#Dictionary..
h = {"name":"pinky", "class":5, "present":True}
print(type(h))

#Set...
i = {"kousar", "malavika", "navya", "indu", "medha", "pinky"}
print(type(i))

#FrozenSet
j = frozenset({"apple", "banana", "cherry"})
print(type(j))

#Bool...
k = True
print(type(k))

#bytes...
l = b"Hello"
    #display l:
print(l)
    #display the data type of l:
print(type(l)) 

#bytearray...
x = bytearray(5)
    #display x:
print(x)
    #display the data type of x:
print(type(x))

#memoryview...
x = memoryview(bytes(5))
    #display x:
print(x)
    #display the data type of x:
print(type(x))

#none..
x = None
    #display x:
print(x)
    #display the data type of x:
print(type(x)) 


#Type Conversion
#convert from one type to another with 
#the int(), float(), and complex() methods

#convert from int to float:
x = float(1)

#convert from float to int:
y = int(2.8)

#convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

#Python does not have a random() function to make a random number,
#but Python has a built-in module called random 
# that can be used to make random numbers.
import random

print(random.randrange(1, 10))