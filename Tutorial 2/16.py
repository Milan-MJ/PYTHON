# Write a menu driven program to implement the following
# i)check even or odd
# ii)check number is positive negative or zero
# iii) generate factors of a number
while True:
    print("1. Even or Odd\n2. Positive, Negative, Zero\n3. Factors of Number\n4. Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        n = int(input("Enter number: "))
        print("Even" if n % 2 == 0 else "Odd")
    elif choice == 2:
        n = int(input("Enter number: "))
        print("Positive" if n > 0 else "Negative" if n < 0 else "Zero")
    elif choice == 3:
        n = int(input("Enter number: "))
        print("Factors:", [i for i in range(1, n+1) if n % i == 0])
    elif choice == 4:
        break
