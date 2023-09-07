import cmath
#to override
class Complex_No:
    def __init__(self, real, imag):
        self.number = complex(real, imag)
    
    def Display(self):
        print(f"{self.number:.2f}")
    
    def __add__(self, other):
        summation = self.number + other.number
        return Complex_No(summation.real, summation.imag)
    
    def __sub__(self, other):
        difference = self.number - other.number
        return Complex_No(difference.real, difference.imag)
    
    def __mul__(self, other):
        multiplication = self.number * other.number
        return Complex_No(multiplication.real, multiplication.imag)
    
    def __truediv__(self, other):
        division = self.number / other.number
        return Complex_No(division.real, division.imag)
    
    def Modulus(self):
        return abs(self.number)


C = Complex_No(3, 2)
D = Complex_No(-4, -5)

C.Display()
D.Display()

sum = C + D
sum.Display()

diff = C - D
diff.Display()

times = C * D
times.Display()

div = C / D
div.Display()

mod1 = C.Modulus()
print(f"{mod1:.2f}")

mod2 = D.Modulus()
print(f"{mod2:.2f}")