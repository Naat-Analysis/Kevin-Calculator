from sympy import symbols, lambdify
from simbolico import OperacionesSimbolicas
from numerico import OperacionesNumericas
from graficar import Graficador

def main():
    # Definir la función simbólica y las variables
    x, y = symbols('x y')
    funcion_simbolica = x**2 + y**2

    # Operaciones Simbólicas
    operaciones_simbolicas = OperacionesSimbolicas(funcion_simbolica, 'x y')
    derivada_x = operaciones_simbolicas.derivar(x)
    integral_x = operaciones_simbolicas.integrar(x)
    print("Derivada simbólica con respecto a x:", derivada_x)
    print("Integral simbólica con respecto a x:", integral_x)

    # Convertir la función simbólica a numérica para evaluación
    funcion_numerica = lambdify((x, y), funcion_simbolica, 'numpy')

    # Crear una función univariable fijando y = 1 para derivadas numéricas
    funcion_univariable = lambda x_val: funcion_numerica(x_val, 1)

    # Operaciones Numéricas
    operaciones_numericas = OperacionesNumericas(funcion_univariable)
    derivada_numerica = operaciones_numericas.derivar(1)
    integral_numerica = operaciones_numericas.integrar(0, 1)
    print("Derivada numérica en x=1:", derivada_numerica)
    print("Integral numérica de x=0 a x=1:", integral_numerica)

    # Graficar
    # Usar funcion_univariable para la gráfica 2D
    graficador_2d = Graficador(funcion_univariable, ['x'])
    graficador_2d.graficar_2d((0, 5))

    # Usar la función original para la gráfica 3D
    graficador_3d = Graficador(funcion_numerica, ['x', 'y'])
    graficador_3d.graficar_3d((0, 5), (0, 5))

if __name__ == "__main__":
    main()
