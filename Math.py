class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return f'{self.a} + {self.b} = {self.a + self.b}'

    def substruction(self):
        return f'{self.a} - {self.b} = {self.a - self.b}'

    def multiplication(self):
        return f'{self.a} * {self.b} = {self.a * self.b}'

    def division(self):
        return f'{self.a} / {self.b} = {self.a / self.b}'


math = Math(a=3, b=4)
print(math.addition())
print(math.substruction())
print(math.multiplication())
print(math.division())
