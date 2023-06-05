#How to find the length of a list?

list1=[1,2,3,4,5,9]
count=0
for i in list1:
    count=count+1
print(count)

#####################################################################################

#How to swap first & last elements of a list

my_list=[1,2,3]
print("List before swapping:",my_list)
size=len(my_list)
temp=my_list[0]
my_list[0]=my_list[size-1]
my_list[size-1]=temp
print("List before swapping:",my_list)

#####################################################################################
#10- How To Search an Element in a List

my_list=[1,2,3,4,5,6,7,8,9]
element=53
flag=0
for i in my_list:
    if (i==element):
        print("Element found in list")
        flag=1
        break
if flag==0:
    print("Element not found in list")
    
######################################################################################    
#11- How to clear a List?
    """Initlaizing with empty list
    """
first_list=[1,2,3,4]
print("Firstlist before clearing:",first_list)
first_list=[]
print("Firstlist after clearing:",first_list)


"""
    using clear keyword

"""
list1=[1,2,3,4,5]

print("Firstlist before clearing:",list1)
list1.clear()
print("Firstlist after clearing:",list1)

"""
    Using operator  *=0 
"""
list2=[1,2,3,4,5]
print("Firstlist before clearing:",list2)
list2 *=0
print("Firstlist after clearing:",list2)

######################################################################################

#9- How to remove the nth occurrence of the word from a list?

list1=["Vital","Reddy","Nani","Bittu"]

n=2
word="Nani"
count=0
for i in range(0,len(list1)):
    if (list1[i])==word:
        count=count+1
        if count==n:
            del list1[i]
print("Updated list",list1)
        
        
        
    

