#x=int(input("Enter the number"))
"""
sum=0
num=x
while(num>0):
    remd=num%10
    sum=sum+remd**3
    num =num//10
print(sum)
if sum == x:
    print("yes")
else:
    print("no") """

def angramnum(start,last):
    for x in range (start,last):
        
        sum=0
        l=len(str(x))
        num=x
        while(num>0):
            remd=num%10
            sum=sum+remd**l
            num =num//10
        if sum == x:
            print("yes" + str (x))
        else:
            print("no" + str(x))
    

start=int(input("Enter the start number "))
last=int(input ("Enter the last number "))
result=angramnum(start,last)

