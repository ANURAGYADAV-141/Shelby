var1=0
var2=1
sum=0
n=int(input())
print(var1,var2,end=" ")

for i in range(n):
    sum=var1+var2
    var1=var2
    var2=sum
    print(sum,end=" ")
