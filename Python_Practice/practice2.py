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
print("List after swapping",my_list)
