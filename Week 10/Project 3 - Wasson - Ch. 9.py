from breezypythongui import EasyFrame

class temperatureCalcuator (EasyFrame):
                
    def __init__(self):
        EasyFrame.__init__(self)
        self.titleLabel = self.addLabel(text = "Temp Converter", sticky = "NSEW", row = 0, column = 0, columnspan = 4)
        self.fahrenheitLabel = self.addLabel(text = "Fahrenheit", sticky = "W",  row = 1, column = 0, columnspan = 2)       
        self.fahrenheitField = self.addFloatField(value = 32.0, sticky = "NSEW", row = 2, column = 0, columnspan = 2)
        self.celsiusLabel = self.addLabel(text = "Celsius", sticky = "W", row = 1, column = 2, columnspan = 2)
        self.celsiusField = self.addFloatField(value = 0.0, sticky = "NSEW", row = 2, column = 2, columnspan = 2)
        self.calcuatecelsiusButton = self.addButton(text = ">>>>", row = 3, column = 0, command = self.celsiusConversion)
        self.calcuatefahrenheitButton = self.addButton(text = "<<<<", row = 3, column = 2, command = self.fahrenheitConversion)

    def celsiusConversion(self):
        Celsius = (self.fahrenheitField.getNumber() - 32) * (5/9)
        self.celsiusField.setNumber(celsius)

    def fahrenheitConversion(self):
        Fahrenheit = self.celsiusField.getNumber() * (9/5) + 32
        self.fahrenheitField.setNumber(fahrenheit)
        
def main():
    temperatureCalcuator().mainloop()

main()
