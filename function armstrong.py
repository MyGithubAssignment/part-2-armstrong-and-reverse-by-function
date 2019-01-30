'''#program to check wheather the numner is armstrong or not:
def armstrong(num):
    n=num
    sum=0
    while (n>0):
        pow=n%10
        sum=sum+(pow*pow*pow)
        n=int(n/10)
    if sum==num:
        return 1
    else:
        return 0
x=int(input("enter the value:"))
if armstrong(x):
    print("it is armstrong number .",x)
else:
    print(" it is not armstrong.",x)
'''
#program to check wheather it is palindrome or not:
def isPalindrome(n):
    num=n
    d=0
    rev=0
    while n>0:
        d=n%10
        n=n//10
        rev=rev*10+d
    if(num==rev):
        return True
    else:
        return False
y=int(input("enter the value:"))
if isPalindrome(y):
  print(y,"is palindrome")
else:
  print(y,"is not palindrome")
