from breezypythongui import EasyFrame

class incomeTax (EasyFrame):
                
    def __init__(self):
        EasyFrame.__init__(self)
        self.incomeLabel = self.addLabel(text = "Gross Income", sticky = "W", row = 0, column = 0)
        self.incomeField = self.addFloatField(value = 0.0, sticky = "NSEW", row = 0, column = 1, columnspan = 2)
        self.depLabel = self.addLabel(text = "Dependents", sticky = "W",  row = 1, column = 0)
        self.depField = self.addIntegerField(value = 0, sticky = "NSEW", row = 1, column = 2)
        self.calcuateButton = self.addButton(text = "Calcuate", row = 2, column = 1, command = self.taxCalcuator)
        self.taxLabel = self.addLabel (text = "Total tax", sticky = "W", row = 3, column = 0)
        self.taxField = self.addFloatField (value = 0.0, sticky = "NSEW", row = 3, column = 1, columnspan = 2, precision = 2)

    def taxCalcuator(self):
        commonDeduction = 10000.0
        depDeduction = 3000.0
        currentTaxRate = 0.20
        taxedIncome = self.incomeField.getNumber() - commonDeduction -\
                        (depDeduction * self.depField.getNumber())
        if taxedIncome < 0:
            taxedIncome = 0
        self.taxField.setNumber(taxedIncome * .20)
        
def main():
    incomeTax().mainloop()

main()
