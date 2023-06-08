def my_function():
    try:
        print("Hello")
        return
    finally:
        print("world")
my_function()

########################################################################################

numbers=[1,2,3]

try:
    value=numbers[0]
except IndexError as e:
    print(f'An error occurred:{e}')
###########################################################################################

def divide(a,b):
    try:
        result=a/b
    except ZeroDivisionError:
        print("Opps! Division by Zero is not allowed")
    else:
        print(f"The result is : {result}")
    finally:
        print("The Divided function has been executed")
divide(10,0)        