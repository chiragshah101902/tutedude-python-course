def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Call the function with a sample number
myNumber = 5
result = factorial(myNumber)

# Print the result
print(f"The factorial of {myNumber} is {result}")
