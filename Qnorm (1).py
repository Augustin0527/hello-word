#!/usr/bin/env python
# coding: utf-8

# In[38]:


### Généralisation de valeurs de normale centrée réduite 
### Importation des packages importants
import numpy as np
import matplotlib.pyplot as plt
import math as ma
import random as rd
def qnorm(n,p):
    ''' Génération de nombre pseudo aléatoire de normale centrée réduite'''
    X=np.zeros(n)
    Esp=p/2
    Vsp=p/12
    for i in range(n):
        Sp=0
        A=[rd.random() for j in range(p)]
        for k in A:
            Sp=Sp+ k
        X[i]=(Sp-Esp)/ma.sqrt(Vsp)
    ### Courbe de la loi centrée réduite
    A=np.linspace(-3,3,11)
    B=[[],[],[],[],[],[],[],[],[],[]]
    x=np.zeros(10)
    y=np.zeros(10)
    for j in X:
        for i in range(10): 
            if j<A[i+1] and j>=A[i] :
                B[i].append(j)
                
    for i in range(10):
        y[i]=(len(B[i]))/n ## l'axe des ordonnées en fonction des fréquence fi
        x[i]=(A[i+1]+A[i])/2  ### L'axe des abscisses , centre ci des intervales
    return x,y


# In[43]:


x,y=qnorm(1000,50)
a1,b1=qnorm(1000,100)
plt.subplot()
plt.plot(x,y,'b')
plt.plot(a1,b1,'r')
plt.show()


# In[ ]:




