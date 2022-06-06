#Método cerrado "Regula falsi"
import matplotlib.pyplot as ptl
import numpy as np
 
def metodo_regulafalsi(f, a, b, tol=10**-4, n=50):
    """
    Método de regula falsi
    :param f: Funcion a la que se le intenta encontrar una solucion para la ecuacion f(x)=0, previamente definida
    :param a: límite inferior
    :param b: límite superior
    :param tol: toleracia, criterio de parada
    :param n: número máximo de iteraciones, criterio de parada
    :return: solución exacta o aproximada, si tiene.
    """
    if f(a)*f(b) >= 0:  # el intevalo escogido no sirve
        print('El intervalo no funciona, f(a)={:.2f} y f(b)={:.2f}'.format(f(a),f(b)))
        return None
    
    e_abs = abs(b-a) #Valor absoluto
    i = 1
    c = a - (f(a)*(b - a))/(f(b) - f(a))
    while i <= n and e_abs > tol:
        c_1 = c
        print('ite {:<2}: a_{:<2}={:.7f} , b_{:<2}={:.7f}, c_{:<2}={:.7f}'.format(i,i-1,a,i-1,b,i,c_1))
        
        if f(c_1)==0:  # solución exacta encontrada
            print('Solución encontrada x={:.7f}'. format(c_1))
            return c_1
        
        if f(a)*f(c)<0:  # escoger intervalo izquierdo
            b = c_1
        else:  # escoger intervalo derecho
            a = c_1
            
        c = a - (f(a)*(b - a))/(f(b) - f(a))
        
        e_abs = abs(c_1 - c)  # error absoluto
        
        if e_abs < tol:  # criterio de parada
            print('Solución encontrada x= {:.7f}, iteraciones: {}'. format(c,i))
            return c
        
        i += 1
    print ('Solución no encontrada, iteraciones agotadas: {}'.format(i-1))
    return None

# Declaramos una función calquiera
def f(x):
    import numpy as np
    return x + np.log(x)

metodo_regulafalsi(f,0.2,1.4)