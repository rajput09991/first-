i=1
x = int(input("Enter no of students : "))
while i<=x:
 age  = int(input("Enter your age : "))
if age>=18:
    print("You can drive")
elif age<=12:
    print("You are child , you can,t drive")
elif age>=90:
    print("You are too old to drive")
else:
    print("Invalid input")
i+=1