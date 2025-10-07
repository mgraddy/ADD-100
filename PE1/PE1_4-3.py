'''Define the function calculate_interest with appropriate parameters.
Apply the formula to calculate the simple interest.
Return the calculated interest.
Print the result using an f-string:'''
def calculate_interest(principal, rate, time):
    simple_interest = (principal * rate * time) / 100
    return simple_interest

def main():
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the interest rate: "))
    time = float(input("Enter the time in years: "))
    interest = calculate_interest(principal,rate,time)
    print(f"The simple interest for ${principal:,.2f} at {rate}% over {time} years is ${interest:,.2f}.")

main()  