

a = 5
b = 2


try:
    print("resource open")
    print(a/b)

    k = int(input("Enter a number: "))
    print(k)

except ZeroDivisionError as e:
    print("you cannot divide a number by Zero.", e)

except ValueError as e:
    print("Invalid input.", e)

except Exception as e:
    print("Something went wrong.",e)

finally:
    print("resource closed")
print("Bye")

