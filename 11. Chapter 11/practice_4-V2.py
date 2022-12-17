from math import sqrt


class Complex:
    def __init__(self, real, imag):
        self.re = real
        self.im = imag

    def __add__(self, o):
        return Complex(self.re+o.re, self.im+o.im)

    def __sub__(self, o):
        return Complex(self.re-o.re, self.im-o.im)

    def __mul__(self, o):
        return Complex(self.re*o.re-self.im*o.im, self.re * o.im + self.im * o.re)

    def __truediv__(self, o):
        m = o.re * o.re + o.im * o.im
        return Complex((self.re * o.re + self.im * o.im)/m, (self.im * o.re - self.re * o.im)/m)

    def __rmul__(self, o):
        # Allow multiplication with scalars on the right
        return Complex(self.re * o, self.im * o)

    def __radd__(self, o):
        # Allow addition with scalars on the right
        return Complex(self.re + o, self.im)

    def __rsub__(self, o):
        # Allow subtraction from scalars on the right
        return Complex(o - self.re, -self.im)

    def __rtruediv__(self, o):
        # Allow division of scalars by complex numbers on the right
        m = self.re * self.re + self.im * self.im
        return Complex((o * self.re) / m, (-o * self.im) / m)

    def __abs__(self):
        return sqrt(self.re*self.re + self.im*self.im)

    def __repr__(self):
        return f'Complex({self.re!r}, {self.im!r})'

    def __eq__(self, o):
        return self.re == o.re and self.im == o.im

    def __pow__(self, o):
        if o == 0:
            return Complex(1, 0)
        if o < 0:
            return Complex(1, 0) / (self ** abs(o))
        if o % 2 == 0:
            return (self * self) ** (o // 2)
        return self * (self ** (o - 1))

    def __round__(self, n=None):
        return Complex(round(self.re, n), round(self.im, n))

    def __format__(self, fmt):
        if ',' in fmt:
            real_fmt, imag_fmt = fmt.split(',')
        else:
            real_fmt = imag_fmt = fmt
        return f'({self.re:{real_fmt}} + {self.im:{imag_fmt}}i)'

    def __str__(self):
        if self.im == 0:
            return f'{self.re:.2f}'

        def __iadd__(self, o):
        self.re += o.re
        self.im += o.im
        return self

    def __isub__(self, o):
        self.re -= o.re
        self.im -= o.im
        return self

    def __imul__(self, o):
        self.re = self.re*o.re - self.im*o.im
        self.im = self.re * o.im + self.im * o.re
        return self

    def __itruediv__(self, o):
        m = o.re * o.re + o.im * o.im
        self.re = (self.re * o.re + self.im * o.im) / m
        self.im = (self.im * o.re - self.re * o.im) / m
        return self

    def conjugate(self):
        """Return the complex conjugate of the complex number."""
        return Complex(self.re, -self.im)

    def phase(self):
        """Return the phase (or argument) of the complex number."""
        return atan2(self.im, self.re)
