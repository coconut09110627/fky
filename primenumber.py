x = int(input("What is x?"))
if x < 2:
    print("x is not prime")
else :
    for i in range(2, x):
        if x % i == 0:
            print("x is not prime")
            break
    else:
        print("x is prime")
        