import calendar
year=int (input("Enter the year:"))
m=1
print("*******calendar*****")
cal = calendar.TextCalender(calendar.Sunday)
i=1
while i<=12:
	cal.permonth(y,i)
	i+=1
