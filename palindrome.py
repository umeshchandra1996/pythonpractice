num=int(input("Enter the number "))
numcopy=num #copy num for compare whith reverse   
reverse=0
while num>0:
    reminder=num%10 #find reminder  
    reverse=(reverse*10) + reminder
    num//=10
if(numcopy == reverse):
    print("Yes It is a plaindrome number ")
else:
    print("It is not plaindrome number ")
