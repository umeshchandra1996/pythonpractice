s1=int(input("Enter the s1 marks: "))
s2=int(input("Enter the s2 marks: "))
s3=int(input("Enter the s3 marks: "))
s4=int(input("Enter the s4 marks: "))
s5=int(input("Enter the s5 marks: "))
ave=int(s1+s2+s3+s4+s5)/5
if(ave>=90):
	print("GRADE : O")
elif(ave>=80):
	print("GRADE : A")
elif(ave>=70):
	print("GRADE : B")
elif(ave>=60):
	print("GRADE : C")
elif(ave>=50):
	print("GRADE : D")
elif(ave>=40):
	print("GRADE : E")
else:
	print("FAILED")
	
	
	
	
	
	
	
	
	
	
	
	
	
studentMarks=[]
noOfSub = int(input("Enter the no of subject\n"))
noOfSubi =noOfSub
while noOfSub>0:
    marks=int(input("Enter the marks\n"))
    studentMarks.append(marks)
    noOfSub=noOfSub-1
    
sum=0
for i in range (0,noOfSubi):
    sum+=studentMarks[i]
    
ave=sum/noOfSubi
print(str(ave)+"\n")
if(ave>=90):
	print("GRADE : O")
elif(ave>=80):
	print("GRADE : A")
elif(ave>=70):
	print("GRADE : B")
elif(ave>=60):
	print("GRADE : C")
elif(ave>=50):
	print("GRADE : D")
elif(ave>=40):
	print("GRADE : E")
else:
	print("FAILED")



