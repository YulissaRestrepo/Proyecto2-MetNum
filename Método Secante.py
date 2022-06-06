from re import X
import numpy as np


def metodo_secante(f, p_0, p_1, tol=10**-4, n=50):
    """
    Método Newton Raphson
    :param f: Funcion a la que se le intenta encontrar una solucion para la ecuacion f(x)=0, previamente definida
    :param p_0: semilla (punto inicial)
    :param p_1: semilla (punto inicial)
    :param tol: toleracia, criterio de parada
    :param n: número máximo de iteraciones, criterio de parada
    :return: solución exacta o aproximada, si tiene.
    """
    e_abs = abs(p_1 - p_0)
    
    print('ite {:<2}: p_{:<2}={:.7f}'.format(0,0,p_0))
    print('ite {:<2}: p_{:<2}={:.7f}, e_abs={:.7f}'.format(1,1,p_1,e_abs))
    
    i = 2
    while i <= n:
        if f(p_1) == f(p_0): #división por cero
            print('Solución no encontrada (error en los valores iniciales)')
            return None
        
        p_2 = p_0 - (f(p_0)*(p_1 - p_0))/(f(p_1) - f(p_0))  # fórmula método secante
        e_abs = abs(p_2 - p_1)
        print('ite {:<2}: p_{:<2}={:.7f}, e_abs={:.7f}'.format(i,i,p_2,e_abs))
        
        if e_abs < tol:  # criterio de parada
            print('Solución encontrada x= {:.7f}, iteraciones: {}'. format(p_2,i))
            return p_2
        p_0 = p_1
        p_1 = p_2
        i += 1
    print('Solución no encontrada, iteraciones agotadas: {}'.format(i-1))
    return None    

#Declaramos una función cualquiera
def f(x):
    return x**x - 100
    
metodo_secante(f, 3, 3.2, 10**-15, 500)   
