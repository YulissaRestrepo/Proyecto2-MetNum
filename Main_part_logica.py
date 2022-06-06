from pyexpat import XMLParserType
from tkinter import X
import numpy as np

def metodo_regulafalsi(func, a, b, tol=10**-4, n=20):

    #evalua la funcion que es cadena
    def f(x):
        f= eval(func)
        return f

    e_abs = abs(b-a)
    i = 1
    c = a - (f(a)*(b - a))/(f(b) - f(a))
    while i <= n and e_abs > tol:
        c_1 = c
        print('ite {:<2}: a_{:<2}= {:.4f} , b_{:<2}= {:.4f}, abs_{:<2}= {:.4f}'.format(i,i-1,a,i-1,b,i,c_1))
        
        if f(c_1)==0:  # solución exacta encontrada
            print('Solución encontrada x={:.4f}'. format(c_1))
            return c_1
        
        if f(a)*f(c)<0:  # escoger intervalo izquierdo
            b = c_1
        else:  # escoger intervalo derecho
            a = c_1
            
        c = a - (f(a)*(b - a))/(f(b) - f(a))
        
        e_abs = abs(c_1 - c)  # error absoluto
        
        if e_abs < tol:  # criterio de parada
            print('Solución encontrada x= {:.4f}, iteraciones: {}'. format(c,i))
            return c
        
        i += 1
    print ('Solución no encontrada, iteraciones agotadas: {}'.format(i-1))
    return None

def metodo_secante(f,a,b,tol=10**-4, n=20):
    
    #Evalua la funcion que es cadena
    def f(x):
        f= eval(func)
        return f

    for i in range(n):  
        fp=(f(b)-f(a))/(b-a)
        x=b-f(b)/fp
        e=abs((x-b)/x)*100
        print('ite {:<2}: a_{:<2}= {:.4f} , b_{:<2}= {:.4f}, Eabs:{:<2}= {:.4f}'.format(i+1,i+1,a,i+1,b,i+1,e))
        if e<tol:
            break
        a=b
        b=x
        #print(k,x,f(x),e)


#programa principal
print("PROYECTO 2 - METODOS NUMERICOS\n J.Benthancourth y Y.Restrepo\n 1SF-131")
m= int(input("Escoja el metodo a usar \n\n 1- Metodo Cerrado (REGULA FALSI)\n 2-Metodo Abierto (SECANTE)\n"))
if m==1:
    func= input("introduzca la funcion: \n")
    a= float(input("introduzca el valor inferior: "))
    b= float(input("introduzca el valor superior: "))
    metodo_regulafalsi(func, a, b) 

if m==2:
    func= input("introduzca la funcion: \n")
    a= float(input("introduzca el valor inferior: "))
    b= float(input("introduzca el valor superior: "))
    metodo_secante(func, a, b)
     
