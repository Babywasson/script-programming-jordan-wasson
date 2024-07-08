print("This code will calcuate an employee's pay")
employeesHours = float(input("Employee's hours worked: "))
payRate = float(input("Input the employee's Pay Rate: "))
normalPay = employeesHours * payRate
employeesotHours = float(input("Employee's overtime hours worked: "))
otRate = payRate * 1.5
otPay = otRate * employeesotHours
totalPay = normalPay + otPay
x = round(totalPay, 2)
print("The employee's total pay is $" + str(x))
