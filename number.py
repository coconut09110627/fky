def main():
   x = get_in()
   print(f"The input number is: {x}")

def get_in():
    while True:
        try:
            x = int(input("What is x?"))
        except ValueError:
            print("Please enter a valid integer.")
        else:
            return x
        
main()