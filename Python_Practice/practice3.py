#13- Program to count the occurrence of an element in a list?
list1=[1,2,3,4,1,3,5,2,4,5,1,9]
count=0
element=1
for i in list1:
    if i==element:
        count=count+1
print("{} has occured {} times".format(element,count))
#################################################################################################

#14- How to find sum of element in the list?

list1=[1,2,3,4,1,3,5,2,4,5,1,9]
count=0
for i in range(0,len(list1)):
    print(i)
    count=count+list1[i]
    
print("Count of all list is:",count)    

# How to find the smallest and the largest number in a list? without using in-built function

my_list=[3,4,5,21,65,3,1,55,6,90]
mx_list=list[0]
for i in my_list:
    print(i)
    if i > mx_list:
        mx_list=i
print(mx_list)