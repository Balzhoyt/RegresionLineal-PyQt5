# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 23:38:39 2019

@author: balzh
"""
import pandas as pd
import RegresionLineal as rl
df=pd.read_csv('data/peso_estatura_edad.csv')
x=df['peso']
y=df['estatura']


r=rl.regresionLineal()
print(r.b0,r.b1)
r.plot_recta(x,y)
