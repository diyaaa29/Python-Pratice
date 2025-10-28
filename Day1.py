# -*- coding: utf-8 -*-
"""take numbers from user.if first number is greater than the second one add them, if first less than second substract them, if same ask for diff number, end when 0 or negative . check end result for palindrome
"""

n1=int(input("Enter the first number:"))
while True:
  n2=int(input("enter a number:"))
  if n2 <= 0:
    break
  elif n2 > n1:
    n1 = n1+n2
    print(n1)
  elif n2 < n1:
    n1 = n1-n2
    print(n1)
  elif n2 == n1:
    print("equal value enter different number")

x=n1
y=0
while x>0:
  y = y*10 + x%10
  x = x//10
print(y)
if y == n1:
  print("palindrome")
else :
  print("no")

"""Sort array - Bubble Sort"""

arr1 = []
n = int(input("enter number of elements:"))
while n>0:
  arr1.append(int(input("enter number")))
  n-=1

j=0
while j<len(arr1)-1:
  i=0
  while i< len(arr1)-1-j:
    if arr1[i]>arr1[i+1]:
      #using 3rd variable
      # temp=arr1[i]
      # arr1[i]=arr1[i+1]
      # arr1[i+1]=temp
      arr1[i],arr1[i+1]=arr1[i+1],arr1[i]
    i+=1
  j+=1
print(arr1)





