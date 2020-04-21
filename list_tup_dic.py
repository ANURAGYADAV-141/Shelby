print("Enter the length of list")
lenl=int(input())
list1=list()
for i in range(lenl):
    ele=input()
    list1.append(ele)
print(list1)

print("Converting your list in tuple")
tup1=tuple(list1)
print("enter the index you wanna access")
ind=int(input())
print(tup1[ind])
print("Deleting an element of dictionary")
dic={1:'A',2:'B',3:'C',4:'D'}
print("enter the key u want to remove")
krem=int(input())
if krem<=4 :
   dic.pop(krem)
print(dic)
