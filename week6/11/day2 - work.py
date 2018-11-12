
class Complex(object):
    def __init__(self, rel, im):
        self.real = rel
        self.img = im
    def __add__(self, other):
        if type(other) == int:
            r=self.real+other
            return Complex(r, i)
        else:
           # return Complex(self.real + other.real, self.img + other.img)
            r = self.real+other.real
            i = self.img + other.img
            return Complex(r,i)
    def __sub__(self, other):
        if type(other) == int:
            r=other - self.real
            return Complex(r, i)
        else:
           # return Complex(self.real + other.real, self.img + other.img)
            r = self.real - other.real
            i = self.img - other.img
            return Complex(r,i)
    def __str__(self):
        return f'{self.real}+{self.img}i'

    def __mul__(self, other):
        r = (self.real * other.real) - (self.img * other.img)
        i = (self.real * other.img) + (self.img * other.real)
        return Complex(r, i)
    # Mnożenie
    # (a1 + b1i)(a2 + b2i) = (a1a2 - b1b2) + (a1b2 + a2b1)i
    def __pow__(self, power, modulo=None):
        if power ==2:
            return self*self
        else:
            return "Poteguje tylko do drugiej potegi1"
# operator + wywoluje nam funkcje add, do tego co jest po lewej stronie plusa
z1 = Complex(1,2)
z2 = Complex(3,4)
#print(Complex)
w = z1+z2
x = z2-z1
y = z1*z2
p = z1**2
print(w,"\n",x, "\n", y, "\n", p)
