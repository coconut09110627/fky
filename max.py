x = float(input("What is x?"))
y = float(input("What is y?"))
z = float(input("What is z?"))
if x > y :
    if x > z :
        print("x is the largest number")
    elif x < z :
        print("z is the largest number")
    else :
        print("x and z are equal and the largest number")
elif x < y :
    if y < z :
        print("z is the largest number")
    elif y > z :
        print("y is the largest number")
    else :
        print("y and z are equal and the largest number")
else :
    if x > z :
        print("x and y are equal and the largest number")
    elif x < z :
        print("z is the largest number")
    else : 
        print("x, y and z are equal")