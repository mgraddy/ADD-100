'''Open sales_totals in read mode (Download the start file (sales_totals.txt)) Read each line in a loop Strip newline and convert to float Add to running total Count the lines Format and print each number Print the total, count, and average Use a main() function Use try and except for errors'''
def main():
    
    try:
        total = 0
        count = 0
        with open('PE2/4.3/sales_totals.txt', 'r') as file:
            line = file.readline()
            while line:
                number = float(line.rstrip())
                formatted_number = "{:,.2f}".format(number)
                print(formatted_number)
                total += number
                count += 1
                line = file.readline()
        if count > 0:
            average = total / count
            print("Total:", "{:,.2f}".format(total))
            print("Count:", count)
            print("Average:", "{:,.2f}".format(average))
    except IOError:
        print("An IOError has occurred.")
    except (ValueError, TypeError):
        print("An input error has occurred")

main()