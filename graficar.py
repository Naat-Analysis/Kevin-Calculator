import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Graficador:
    def __init__(self, funcion, variables):
        """
        Constructor de la clase Graficador.

        Args:
            funcion (function): La función numérica que se va a graficar.
            variables (list): Lista de las variables involucradas en la función (por ejemplo, ['x'] o ['x', 'y']).
        """
        # Inicializa la función numérica que se utilizará para la gráfica.
        self.funcion = funcion
        
        # Almacena las variables de la función (esto se utiliza para determinar si se trata de una gráfica 2D o 3D).
        self.variables = variables

    def graficar_2d(self, rango_x):
        """
        Grafica la función en 2D.

        Args:
            rango_x (tuple): Tupla que define el rango de valores de x para la gráfica (por ejemplo, (0, 5)).
        """
        # Genera un conjunto de puntos en el rango de x especificado.
        x_vals = np.linspace(rango_x[0], rango_x[1], 100)
        
        # Evalúa la función en todos los puntos x generados.
        y_vals = [self.funcion(x) for x in x_vals]
        
        # Crea la gráfica 2D.
        plt.plot(x_vals, y_vals)
        
        # Establece etiquetas para los ejes y un título.
        plt.xlabel(self.variables[0])
        plt.ylabel('f({})'.format(self.variables[0]))
        plt.title('Gráfica 2D de la función')
        
        # Muestra la gráfica.
        plt.show()

    def graficar_3d(self, rango_x, rango_y):
        """
        Grafica la función en 3D.

        Args:
            rango_x (tuple): Tupla que define el rango de valores de x para la gráfica (por ejemplo, (0, 5)).
            rango_y (tuple): Tupla que define el rango de valores de y para la gráfica (por ejemplo, (0, 5)).
        """
        # Genera un conjunto de puntos en los rangos de x e y especificados.
        x_vals = np.linspace(rango_x[0], rango_x[1], 100)
        y_vals = np.linspace(rango_y[0], rango_y[1], 100)
        
        # Crea una malla de puntos (pares x, y) sobre los cuales se evaluará la función.
        X, Y = np.meshgrid(x_vals, y_vals)
        
        # Evalúa la función en cada par (x, y) de la malla.
        Z = self.funcion(X, Y)
        
        # Crea una figura y un conjunto de ejes 3D.
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        # Grafica la superficie en 3D.
        ax.plot_surface(X, Y, Z, cmap='viridis')
        
        # Establece etiquetas para los ejes y un título.
        ax.set_xlabel(self.variables[0])
        ax.set_ylabel(self.variables[1])
        ax.set_zlabel('f({}, {})'.format(self.variables[0], self.variables[1]))
        ax.set_title('Gráfica 3D de la función')
        
        # Muestra la gráfica.
        plt.show()
