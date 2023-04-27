#include <iostream>
#include <iomanip>
#include <cmath>
#include <string>

using namespace std;

double f(double x)
{
    return 4.0 / (1.0 + x * x);
}

double deltax(double a, double b, double n)
{
    return (b - a) / n;
}

double trapezoidalRule(double a, double b, int n)
{
    double subinterval = deltax(a, b, n);
    double sigmafx = 0.0;
    for (int i = 1; i < n; i++)
    {
        sigmafx += f(i * subinterval);
    }
    return subinterval * (sigmafx + ((f(n * subinterval) + f(0 * subinterval)) / 2));
}

double simpsonsRule(double a, double b, int n)
{
    double subinterval = deltax(a, b, n);
    double sigmaN1 = 0.0;
    double sigmaN2 = 0.0;
    for (int i = 1; i < n; i++)
    {
        if (i % 2 == 1)
        {
            sigmaN1 += 4 * f(i * subinterval);
        }
        else if (i % 2 == 0 || i < n - 1)
        {
            sigmaN2 += 2 * f(i * subinterval);
        }
    }
    return (subinterval / 3) * (f(0 * subinterval) + sigmaN1 + sigmaN2 + f(n * subinterval));
}

double percentageError(double trueValue, double approxValue)
{
    return ((trueValue - approxValue) / trueValue) * 100;
}

int main()
{
    double truePi = 3.1415667;
    int n;
    double a;
    double b;
    double approxValue;
    cout << "Enter the amount of subintervals: ";
    cin >> n;
    cout << "Enter the lower limit: ";
    cin >> a;
    cout << "Enter the upper limit: ";
    cin >> b;
    std::string choice;
    cout << "Enter 1 for Trapezoidal Rule, 2 for Simpsons Rule or 3 Change Inputs : ";
    cin >> choice;
    switch (std::stoi(choice))
    {
    case 1:
        approxValue = trapezoidalRule(a, b, n);
        std::cout << "True value of Pi: " << truePi << "\nApproximation using Trapezoidal rule: " << std::setprecision(20) << approxValue << "\nPercentage Error: " << percentageError(truePi, approxValue);
        cout << "\nEnter 4 to calculate more or 5 to close: ";
        cin >> choice;
        if (choice == "4")
        {
            main();
        }
        else if (choice == "5")
        {
            return 0;
            break;
        }
    case 2:
        approxValue = simpsonsRule(a, b, n);
        std::cout << "True value of Pi: " << truePi << "\nApproximation using Simpson's rule: " << std::setprecision(20) << approxValue << "\nPercentage Error: " << percentageError(truePi, approxValue);
        cout << "\nEnter 4 to calculate more or 5 to close: ";
        cin >> choice;
        if (choice == "4")
        {
            main();
        }
        else if (choice == "5")
        {
            return 0;
            break;
        }
    case 3:
        main();
        break;
    default:
        cout << "Please enter a valid input\n";
        main();
    }

    return 0;
}