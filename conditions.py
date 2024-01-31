a=11
b=2
c=33
d=4
if a > b and c > a:
  print("Both conditions are True")


#nested

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#pass keyword

if b > a:
  pass

#loops while
i = 1
while i < 6:
  print(i)
  i+=1

#for loops
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#looping through string
for x in "banana":
  print(x)

#range function
for x in range(2, 6):
  print(x)

#Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)