'''Define the function calculate_interest with appropriate parameters.
Apply the formula to calculate the simple interest.
Return the calculated interest.
Print the result using an f-string:'''
def calculate_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

def main():
    p = float(input("Enter the principal amount: "))
    r = float(input("Enter the interest rate: "))
    t = float(input("Enter the time in years: "))
    interest = calculate_interest(p,r,t)
    print(f"The simple interest for ${p:,.2f} at {r}% over {t} years is ${interest:,.2f}.")

if True:
    main()  