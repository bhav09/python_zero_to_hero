#empty list
list=[]
print("Enter values into a demo list:")
#appending values into a list
for i in range(0,5):
    x=int(input())
    list.append(x)
print(list)     #printting list

#insert():::inserting value at particular position
a=[10,20,20,40,50]
print('List a is:',a)
a.insert(2,25)                                    #syntax= list_name.insert(index,value)
print("List -a- after insertion:",a)

#extend():::concatenates 2 lists ~ sorta
b=[100,200]
c=[300,400]
b.extend(c)
print(b)

#sum()
print("Sum of list a is:",sum(a))
print("--------------------------------------------")

#count()
print("Occurence of 20 in list a is:",a.count(20))
print("--------------------------------------------")

#len():::returns the length of mentioned list
print("Lenght of the mentioned list is:",len(a))
print("--------------------------------------------")

#max() and min()
print("Max in the list list:",max(list))
print("Min in the list list:",min(list))
print("--------------------------------------------")

#reverse() and sort()
a.reverse()
print("Reverse of list a is:",a)
a.sort()
print("Sorting of the reversed list:",a)
print("--------------------------------------------")

#pop() deletes the element at a particular position
print("Popped element:",a.pop())
print("Poping out element at index 2 of list a:",a.pop(2))
print("--------------------------------------------")
 


