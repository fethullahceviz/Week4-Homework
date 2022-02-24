import math as m
import sys
print("""
Select opertaion
[1] Addition
[2] Subtraction
[3] Multiplicaion
[4] Division
[Q] Quit
""")

def add(n1, n2):
    add = n1+n2
    print(f"{n1}", "+", f"{n2} =", m.ceil(add))
def sub(n1, n2):
    sub = n1-n2
    print(f"{n1}", "-", f"{n2} =", m.ceil(sub))
def mult(n1, n2):
    mult = n1*n2
    print(f"{n1}", "*", f"{n2} =", m.ceil(mult))
def division(n1, n2):
    division = n1/n2
    print(f"{n1}", "/", f"{n2} =", m.ceil(division))


while True:
    choice = input("Choice a operation :")

    if choice in ("1", "2", "3", "4"):

        try:
            n1 = float(input("Enter first number: "))
            print("first number  :", n1)
            n2 = float(input("Enter second number: "))
            print("second number :", n2)

            if choice == "1":
                add(n1, n2)                
            elif choice == "2":
                sub(n1, n2)
            elif choice == "3":
                mult(n1, n2)
            elif choice == "4":
                division(n1, n2)

        except:
            tex1 = str(sys.exc_info()[0])
            print("Opps " + tex1.split("'")[1])

    elif choice == "Q" or choice == "q":
        print("exiting the program...")
        quit()

    else:
        print("Invalid Input")
