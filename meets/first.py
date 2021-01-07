try:

    a=10
    print(a/0)
except ZeroDivisionError:
    print("zero cannot be divided")

a=input("enter integer values")
if not type(a)  is int:
    raise TypeError("only interger allowed")