from scipy.misc import derivative
from scipy.integrate import quad

class OperacionesNumericas:
    def __init__(self, funcion):
        self.funcion = funcion

    def derivar(self, x0, dx=1e-6):
        return derivative(self.funcion, x0, dx=dx)

    def integrar(self, a, b):
        return quad(self.funcion, a, b)[0]
