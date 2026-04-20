class student:
    def __init__(self,name,rollno,age,marks):
        self.name=name
        self.rollno=rollno
        self.age=age
        self.marks=marks
        self.total=sum(marks)
        self.avg=self.total/len(marks)

    def display (self):
        print(f"Name:{self.name}")
        print(f"Roll number:{self.rollno}")
        print(f"Age:{self.age}")
        print(f"total marks :{self.total}")
        print(f"average marks :{self.avg}")
        print("_"*30)

n=int(input("enter the number of students :"))
l=[]
for i in range(n):
    print(f"enter detaials of student {i+1}:")
    name=input("enter name:")
    rollno=int(input("enter your roll no:"))
    age=int(input("enter your age:"))
    marks=[]
    for j in range(5):
        a=int(input(f"enter mark of subject {j+1}:"))
        marks.append(a)
    s=student(name,rollno,age,marks)
    l.append(s)
for i in l:
    i.display()
