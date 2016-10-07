class BasePrinter:

    def __init__(self):
        print(">Base Printer")

    def set_value(self, n):
        self.num = n

    def get_value(self):
        return self.num
