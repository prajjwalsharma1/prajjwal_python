from math import *
print("hello Prajjwal sharma")
print("-----------------------question_1---------------------")
a=int(input("enter marks\n"))
if a>=60:
    print("grade: A")
elif a<60 & a>55:
    print("grade : B")

else:
    print("grade : C")

print("----------------------- question_2-------------------------")

y= int(input("enter year: \n"))

a=(y % 400 == 0) if (y % 100 == 0) else (y % 4 == 0)
if a==1:
    print("Leap year \n")

else:
    print("Not Leap Year \n")

print("---------------- question_3-------------------------")


a=int(input("enter first number : \n"))
b=int(input("enter first number : \n"))
c=int(input("enter first number : \n"))

if a>b & a>c:
    print(f" {a} is largest number\n")
elif b>c:
    print(f"{b} is largest number\n")
else:
    print(f" {c} is the largest\n")


print("------------------question_4------------------")

n=int(input("enter the number\n"))
sum=0
while n>0:
    sum=sum+ n%10
    n=n//10
print(f"{sum} is the sum of all digits")



print("-----------------question_5---------------------------")
n=int(input("enter the number: \n"))
a=n
rev=0
while n>0:

    rev=rev*10+(n%10)
    n=n//10
if rev==a:
    print("it is palindrome \n")
else:
    print("not a palindrome")
print("-----------------------------question_6---------------")
n=int(input("enter the number : \n"))
print("all the factors are :\n ")
for i in range(2,n):
    if(n%i==0):
        print(i)

print("--------------------question_7----------------")

n= int(input("enter the number :"))
print(f"the table of {n} is :")
for i in range(1,n+1):
    print(n*i)


print("---------------------queation_8-----------------")
n= int(input("enter the number to which to want to print series "))
print(f"the fibo series upto {n} number")
sum1=0
sum2=1

if n==1:
    print(sum1)
elif n==2:
    print(sum2)
else:
    for i in range(1,n+1):
        if i==1:
            print(0)
            continue
        elif i==2:
            print(1)
        else:
            next=sum1+sum2
            print(next)
            sum2=next
            sum1=sum2

print("------------------------------question_9---------------------------")
n= int(input("enter the number to check whether it is armstron or not  :"))

a=n
d=n
count=0
while a>0:
    count=count+1
    a=a//10

sum=0
while d>0:
    sum=sum+ pow((d%10),count)
    d=d//10
if sum==n:
    print("it is arm strong ")
else:
    print("it is not armstrong")


print("------------------------------question_10-------------------")
from math import *


n=int(input("enter the number : "))

print(factorial(n))