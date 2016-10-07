

class BaseWriter:

	def __init__(self):
		print("> Call BaseWriter!")

    def set_value(self, n):
        self.num = n

    def get_value(self):
        return self.num
