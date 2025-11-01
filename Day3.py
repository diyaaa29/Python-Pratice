# factorial
a = int(input("enter a number"))

if a == 0:
  print(1)
elif a < 0:
  print ('undefined')
else :
  fact =1
  while a > 0:
    fact = fact * a
    a-=1
  print (fact)
