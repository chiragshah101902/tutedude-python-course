import math

def MathModueFunction():
    number = float(input("Enter a number: "))

    if number >= 0:
        sqrt_value = math.sqrt(number)

    # Calculate natural log
    if number > 0:
        log_value = math.log(number)
    else:
        log_value = "undefined (logarithm of non-positive number is undefined)"

    sine_value = math.sin(number)

    # Display results
    print("Square root :", sqrt_value)
    print("Logarithm :", log_value)
    print("Sine:", sine_value)

MathModueFunction()
