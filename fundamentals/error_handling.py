x = 42
y = 0


try:
    print(x / y)
except ZeroDivisionError as e:
    print("Not allowed to divide by zero")
else:
    print("something else went wrong")
finally:
    print("This is our cleanup code")
