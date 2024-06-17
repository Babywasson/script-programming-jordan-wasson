interest = 0.12
downPayment = 0.1 
loanMonths = 12

startingPrice = float(input("What is the starting price of the item to purchase:"))

owedPrincipal  = startingPrice - startingPrice * downPayment
principalbyMonths = owedPrincipal / loanMonths

print("%-6s%12s%19s%21s%18s%25s" % ("Month", "Balance", "Monthly Interest", "Monthly principal", "Monthly payment", "Balance After Payment"))

for month in range(1, loanMonths+1):
        permonthInterest = owedPrincipal * interest / 12
        permonthPayment = principalbyMonths + permonthInterest
        newBalance = owedPrincipal - principalbyMonths

        print("%-6d%12.2f%19.2f%21.2f%18.2f%25.2f" % (month, owedPrincipal , permonthInterest, principalbyMonths, permonthPayment, newBalance))

        owedPrincipal = newBalance
