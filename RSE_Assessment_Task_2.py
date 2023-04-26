import math

truePi = 3.1415667

def f(x):
    'Defines the function to pass x through'
    return 4 /(1 + x**2)

def percentageError(trueValue, approxValue):
    'Takes both values and calculates the percentage error of the approximate value'
    percError = ((trueValue-approxValue)/ trueValue) * 100
    return percError

def deltax (a, b, n):
    'Calculates delta x using the input values'
    return (b - a)/n

def trapezoidalRule(a, b, n):
    '''
    Takes the upper and lower limits of the integration as a and b and n as the
    number of subintervals to be used in the trapezoidal rule
    '''
    subinterval = deltax(a, b, n) # sets subinterval as delta x because it will be used for the increment of x and in the formula
    sigmaFx = 0 # initialises the sum total of the sigma part of the formula
    for i in range(1, n): # performs the sigmaf(xi) part of the formula 
        sigmaFx += f(i * subinterval)
    result = subinterval*(sigmaFx + ((f(n * subinterval) + f(0 * subinterval))/2)) # calculates the trapezoidal rule approximate value
    return result

def simpsonsRule(a, b, n):
    '''
    Takes the upper and lower limits of the integration as a and b and n as the
    number of subintervals to be used in the Simpson's rule
    '''
    subinterval = deltax(a, b, n) # sets subinterval as delta x because it will be used for the increment of x and in the formula
    sigmaN1 = 0 # initialises the sum total of the n-1 sigma
    sigmaN2 = 0 # and the n-1 sigma
    for i in range(1,n): # performs the sigmaf(xi) for both sigmas of the value, stops at n-1 for sigmaN1
        if i % 2 == 1: # if i is odd i.e. 1,3,5 
            sigmaN1 += 4*f(i * subinterval) # multiplies by 4 like 4f(x) in the formula
        elif i % 2 == 0 and i < n - 1: # if i is even i.e. 2,4,6 and stops at n-2
            sigmaN2 += 2*f(i * subinterval) # multiplies by 2 like 2f(x) 
    result = (subinterval / 3) * (f(0 * subinterval) + sigmaN1 + sigmaN2 + f(n * subinterval))
    return result

def main():
    '''
    Gets the users inputs to be used in the formula
    Also creates a simple menus so all the required calculations can be do in one execution of the program
    '''
    n = int(input("\nEnter the amount of subintervals: ")) # gets the 3 inputs to be used in the approximation formulas
    a = int(input("Enter the lower limit: "))
    b = int(input("Enter the upper limit: "))
    # creates the menu to run multiple caluclations
    choice = input("Enter 1 for Trapezoidal Rule, 2 for Simpsons Rule or 3 Change Inputs: ")
    if choice == "1": # calls the trapezoidal rule and the percentage error and outputs the results
        approxValue = trapezoidalRule(a, b, n)
        print("\nTrue Value of pi: ", truePi, "\nApproximate Value: ", approxValue, "\nPercentage Error :", percentageError(truePi, approxValue), "\n")
        choice = input("Enter 4 to Calculate more or anything else to exit: ")
        if choice == "4":
            main()
        else:
            return
    elif choice == "2": # calls the simpson's rule and the percentage error and outputs the results
        approxValue = simpsonsRule(a, b, n)
        print("\nTrue Value of pi: ", truePi, "\nApproximate Value: ", approxValue, "\nPercentage Error :", percentageError(truePi, approxValue), "\n")
        choice = input("Enter 4 to Calculate more or anything else to exit: ")
        if choice == "4":
            main()
        else:
            return
    elif choice == "3":
        main()
    else:
        print("Please enter a valid input")
        main()
    return

main()
