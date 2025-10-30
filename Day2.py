# -*- coding: utf-8 -*-

"""reverse array without using another array"""

arr1 = []
n = int(input("enter number of elements:"))
i=0
while i<n:
  arr1.append(int(input("enter number:")))
  i+=1
j=n-1
i=0
while i<j/2 :
  temp=arr1[i]
  arr1[i]=arr1[j]
  arr1[j]=temp
  i+=1
  j-=1

print(arr1)

""""input 2 binary numbers and display their sum"""
s1 = input("enter first binary number")
s2 = input("enter second binary number")
btd1 = 0
btd2 = 0
n1 = (len(s1)-1)
n2 = (len(s2)-1)
while n1 >= 0:
  if s1[n1] == '1':
    btd1 = btd1 + 2**((len(s1)-1)-n1)
  n1-=1
print (btd1)

while n2 >=0:
  if s2[n2] == '1':
    btd2 = btd2 + 2**((len(s2)-1)-n2)
  n2-=1
print(btd2)

sum = btd1+btd2
print(sum)


