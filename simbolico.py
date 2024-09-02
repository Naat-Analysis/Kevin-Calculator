from sympy import symbols, diff, integrate

class OperacionesSimbolicas:
    def __init__(self, funcion, variables):
        self.funcion = funcion
        self.variables = symbols(variables)

    def derivar(self, variable):
        return diff(self.funcion, variable)

    def integrar(self, variable):
        return integrate(self.funcion, variable)
