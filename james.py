marks = int(input("Enter the marks here: "))

if(marks>=80 | marks<=100):
    print("A")
elif(marks>=70 | marks<80):
    print("B+")
elif(marks>=60 | marks<70):
    print("B")
elif(marks>=50 | marks<60):
    print("C")
elif(marks>=40 | marks<50):
    print("D")
elif(marks>=0 | marks<40):
    print("F")
else:
    print("Entered marks is incorrect")


