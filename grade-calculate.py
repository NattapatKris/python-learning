point = input("enter your point : ")

if int(point) < 50:
    print("your grade is 0")
elif int(point) < 55:
    print("your grade is 1")
elif int(point) < 60:
    print("your grade is 1.5")
elif int(point) < 65:
    print("your grade is 2")
elif int(point) < 70:
    print("your grade is 2.5")
elif int(point) < 75:
    print("your grade is 3")
elif int(point) < 80:
    print("your grade is 3.5")
elif int(point) <= 100:
     print("your grade is 4")
else :
    print("error")