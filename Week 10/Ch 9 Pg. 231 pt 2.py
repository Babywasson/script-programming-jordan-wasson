from breezypythongui import EasyFrame
class LayoutDemo(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self)
        self.addLabel(text = "(0, 0)", row = 0, column = 0, sticky = "NSEW")
        self.addLabel(text = "(0, 1)", row = 0, column = 1, sticky = "NSEW")
        self.addLabel(text = "(1, 0 and 1)", row = 1, column = 0, sticky = "NSEW", columnspan = 2)
def main():
    LayoutDemo().mainloop()

main()
