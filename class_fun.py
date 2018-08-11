class student:
    pass

std_1 = student()
std_2 = student()

std_1.first = 'Umesh'
std_1.midium = 'chandra'
std_1.last = 'Yadav'
std_1.email = 'umesh@gmail.com'
std_1.marks = 90

std_2.first = 'Ramesh'
std_2.midium = 'chandra'
std_2.last = 'Yadav'
std_2.email = 'Ramesh@gmail.com'
std_2.marks = 95

print(std_1.first)

print(std_1.last)

print(std_1.email)

print(std_1.marks)

print(std_2.first)

print(std_2.email)

print(std_2.marks)









class student:

    def __init__(self,first,last,marks):
        self.first = first
        self.last = last
        self.marks = marks
        self.email = first.lower() + last.lower() + '@school.com'

std_1 =student('Neel','Verma',60)
std_2 =student('Hemant','Verma',50)

print(std_1.first)

print(std_1.last)

print(std_1.email)

print(std_1.marks)

print(std_2.first)

print(std_2.email)

print(std_2.marks)






































