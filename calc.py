class Calculator:
    def __init__(self,a,b):
        self._a=a
        self._b=b

    def Addition(self):
        return f"{self._a} + {self._b} = {self._a+self._b}"

c = Calculator(3,5)
print(c.Addition())