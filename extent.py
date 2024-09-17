list1=[10,20,30]
list2=[100,200,300]
print(list1+list2)
list1.extend(list2)
print(list1)
list2.extend(list1)
print(list2)