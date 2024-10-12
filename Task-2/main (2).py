'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1-n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2

def main():
    while True:
        print("Options:")
 
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Divide")
        print("5. Exit application")
        choice = input("Enter your choice: ")
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
        print("Result:")
        if choice == "1":
            print(add(num1, num2))
        elif choice =="2":
            print(sub(num1, num2))
        elif choice == "3":
            print(multiply(num1, num2))
        elif choice == "4":
            print(divide(num1, num2))
        elif choice == "5":
            print("Exiting application")
            break
        else:
            print("Wrong option. Try again")
    
if __name__ == "__main__":
    main()           

    
    
    
    
    