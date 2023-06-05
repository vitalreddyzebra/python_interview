print("FirstProgram adding into git repo")


#1- How to swap two numbers?

num1=input("Enter num1 value:")
num2=input("Enter num2 value:")
print("Num1 value before swap:",num1)
print("Num2 value before swap:",num2)

temp=num1
num1=num2
num2=temp

print("Num1 value after swap:",num1)
print("Num2 value after swap:",num2)

#####################################################################################################

#Method 2- Without using a temporary variable, simply using the shortcut,

num1=input("Enter num1 value:")
num2=input("Enter num2 value:")
print("Num1 value before swap:",num1)
print("Num2 value before swap:",num2)

num1,num2=num2,num1

print("Num1 value after swap:",num1)
print("Num2 value after swap:",num2)

########################################################################################################

#How to check number is prime or not?

num=int(input("Enter a Number to check weather prime or not:"))
if num%2==0:
    print("Entered number is prime")
else:
    print("Entered number is not a prime")
    
##########################################################################################################

#How to find the factorial of a number?

'''
Factorial of a number is the product of all the integers from 1 to that number. For example, the factorial of 7 is 1*2*3*4*5*6*7 = 5040 

'''

factorial=1

num=5

if num<0:
    print("Factorial is not support for negitive numbers")
elif num==0:
    print("factorial number for 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("Factorial of given number:", num ,"is :",factorial)
    