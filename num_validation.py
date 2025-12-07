try:
    number= int(input("Enter a number: "))
    print(f"number is {number}")
except ValueError:
    print("Please enter a valid number")