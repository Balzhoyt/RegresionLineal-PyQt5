import numpy as np
import matplotlib.pyplot as plt


class regresionLinealMultiple:
    def __init__(self):
        self.b0=0
        self.b1=0
        self.b2=0
    
    def operaciones(self,x1,x2,y):
        x1x1=sum([x1**2 for x in x1])
    
    def beta1(self,x,y):
        termino1=x-np.average(x)
        termino2=y-np.average(y)
        Sxy=sum(termino1*termino2)
        Sxx=sum(termino1*termino1)
        return Sxy/Sxx
        
    def beta0(self,x,y):
        return np.average(y)-self.beta1(x,y)*np.average(x)
        
    def plot_recta(self,x,y):
        x=x.tolist()
        y=y.tolist()
        self.b1=self.beta1(x,y)
        self.b0=self.beta0(x,y)
        puntos_x=np.linspace(x[0],x[-1],100)
        puntos_y=self.b0+self.b1*puntos_x
        plt.plot(puntos_x,puntos_y)
        plt.plot(x,y,'r*')
        plt.show()