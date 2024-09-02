from sympy import symbols, lambdify
from simbolico import OperacionesSimbolicas
from numerico import OperacionesNumericas
from graficar import Graficador

def main():
    """
    Función principal que ejecuta el programa.
    Permite al usuario definir una función, realizar operaciones simbólicas y numéricas,
    y graficar la función.
    """
    # Solicita al usuario que ingrese la expresión de la función
    funcion_str = input("Introduce la función en términos de x e y (por ejemplo, 'x**2 + y**2'): ")
    
    # Solicita al usuario que ingrese las variables que se utilizarán en la función
    variables_str = input("Introduce las variables separadas por espacio (por ejemplo, 'x y'): ")
    
    # Convierte la cadena de variables en símbolos de SymPy
    variables = symbols(variables_str)
    
    # Convierte la cadena de la función en una expresión simbólica de SymPy
    funcion_sym = eval(funcion_str)

    # Crea una instancia de la clase OperacionesSimbolicas para manejar operaciones simbólicas
    operaciones_simbolicas = OperacionesSimbolicas(funcion_sym, variables_str)

    # Realiza y muestra la derivada simbólica con respecto a la primera variable
    derivada_simbolica = operaciones_simbolicas.derivar(variables[0])
    print(f"Derivada simbólica con respecto a {variables[0]}: {derivada_simbolica}")
    
    # Realiza y muestra la integral simbólica con respecto a la primera variable
    integral_simbolica = operaciones_simbolicas.integrar(variables[0])
    print(f"Integral simbólica con respecto a {variables[0]}: {integral_simbolica}")

    # Convierte la función simbólica a una función numérica usando lambdify
    funcion_numerica = lambdify(variables, funcion_sym)

    # Crea una instancia de la clase OperacionesNumericas para manejar operaciones numéricas
    operaciones_numericas = OperacionesNumericas(funcion_numerica)

    # Solicita al usuario un punto para evaluar la derivada numérica
    x0 = float(input(f"Introduce el valor de {variables[0]} para calcular la derivada numérica: "))
    
    # Calcula y muestra la derivada numérica en el punto dado
    derivada_numerica = operaciones_numericas.derivar(x0)
    print(f"Derivada numérica en {variables[0]}={x0}: {derivada_numerica}")

    # Solicita al usuario el rango para la integral numérica
    a = float(input(f"Introduce el límite inferior para integrar {variables[0]}: "))
    b = float(input(f"Introduce el límite superior para integrar {variables[0]}: "))
    
    # Calcula y muestra la integral numérica en el rango dado
    integral_numerica = operaciones_numericas.integrar(a, b)
    print(f"Integral numérica de {variables[0]}={a} a {variables[0]}={b}: {integral_numerica}")

    # Crea una instancia de la clase Graficador para manejar la gráfica de la función
    graficador = Graficador(funcion_numerica, variables_str.split())

    # Si la función tiene una sola variable, grafica en 2D
    if len(variables) == 1:
        rango_x = (a, b)  # Se usa el rango de integración como rango para la gráfica
        graficador.graficar_2d(rango_x)
    # Si la función tiene dos variables, grafica en 3D
    elif len(variables) == 2:
        rango_x = (float(input(f"Introduce el límite inferior para graficar {variables[0]}: ")),
                   float(input(f"Introduce el límite superior para graficar {variables[0]}: ")))
        rango_y = (float(input(f"Introduce el límite inferior para graficar {variables[1]}: ")),
                   float(input(f"Introduce el límite superior para graficar {variables[1]}: ")))
        graficador.graficar_3d(rango_x, rango_y)
    else:
        print("Solo se pueden graficar funciones de una o dos variables.")

if __name__ == "__main__":
    main()
