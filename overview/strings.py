#Strings..
print("printing the stings..")

#assigning the stings to variables
a = 'hello world'
print(a)

#multiline string
b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)

#strings are Arrays
print(a[2])

#looping to the string
c = "hakunamatata"
for x in c:
    print(x)

#string length
print(len(c))

#check 'in' string
txt = "dont fire the fire if you fire the fire fire will fire you"
print("fire" in txt)
print("free" in txt)
# txt = "free free freee.!!!"
if "fire" in txt:
    print("yes..! fire is present in txt")
else:
    print("fire is not present in txt")

#check 'not in' string

txt = "The best things in life are free!"
print("expensive" not in txt)

if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#string slicing
b = "hello,world"
print(b[2:5])

#leaving out the start index
#the range will start at the first character
print(b[:5])

#leaving out the end index
#the range will go to the end
print(b[2:])

#negitive indexing
print(b[-5:-2])

#Modify Strings
#upper case
j = "   hi,hello , namaskar   ,,,,  "
print(j.upper())

#lower case
print(j.lower())

#remove whitespace
print(j.strip())

#replace
print(j.replace("h" , "d"))

#split string
print(j.split(","))

#string concatenation
f = "arrow"
g = "and"
h = "bow"

k = f + g + h
print(k)
k = f + " " + g + " " + h
print(k)

