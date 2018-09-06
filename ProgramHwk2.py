# JiaYi Feng jf3354 5/13
# coding: utf-8

# Monte Carol simulation is an important algorithm in finance.  It is very useful for option pricing and risk managment. We can apply Monmte Carlo to price options using the model of stock prices from Black Scholes Merton (1973). The stock price in BSM is a stochastic differential equation with geometric Brownian motion under the risk neutral probability. A discretization scheme for the SDE is given by $S_t=S_{t-\Delta t}exp((r-\frac{1}{2}\sigma^2)\Delta t + \sigma \sqrt{\Delta t} W_t)$.

# To implement a Monte Carlo valuation for an option the following algorithm can be applied. 
# 1. Divide the time interval $[0,T]$ in to equal subintervals of length $\Delta t$.
# 2. Start iterating $i=1,2,\dots,I$.
#    
#    a. For every time step $t\in{\Delta t, 2\Delta t, \dots, T}$ draw a random number from the normal distribution. 
#    
#    b. Determine the time T value of the index level $S_T(i)$ for each time step in the discretization scheme: $S_t=S_{t-\Delta t}exp((r-\frac{1}{2}\sigma^2)\Delta t + \sigma \sqrt{\Delta t} W_t)$.
#    
#    c. At T, determine the value of the option $v_T(S_T(i))$ according to the payoff.
#    
#    d. Iterate until i = I.
#    
# 3. Average all the values of $v_T(S_T(i))$ and discount them back
# 
# 

# Question 1: Complete the Monte Carlo below, adding the code for the discretization scheme: $S_t=S_{t-\Delta t}exp((r-\frac{1}{2}\sigma^2)\Delta t + \sigma \sqrt{\Delta t} W_t)$.
#    



from time import time
from math import exp, sqrt, log
from random import gauss, seed

#get_ipython().magic('matplotlib inline')

import numpy as np
import matplotlib.pyplot as plt



# variables
S0 = 100
T = 1.0
r = 0.05
sigma = 0.20
N = 50
dt = T/N
I = 5000



seed(2000)
S=[]
for i in range(I):
    path = []
    for t in range(N+1):
        if t == 0:
            path.append(S0)
        else:
            wt = gauss(0.0,1.0)
            #
            # add code for St 
            St = path[t-1] * exp((r-0.5*sigma**2) * dt + sigma *sqrt(dt) *wt)
            path.append(St)
    S.append(path)


# Graph 10 price paths for the stock price:


plt.plot(S[1])
plt.plot(S[2])
plt.plot(S[3])
plt.plot(S[4])
plt.plot(S[5])
plt.plot(S[6])
plt.plot(S[7])
plt.plot(S[8])
plt.plot(S[9])
plt.plot(S[10])
plt.grid(True)
plt.xlabel('time step')
plt.ylabel('idenx label')


# Question 2: Using the code from the Monte Carlo and the stock price discretization scheme, price the following options
#     
#     a) Call with Strike = 105, Maturity T = 1
#     
#     b) Put with Strik = 105, Maturity T = 1
#     
#     c) Call with Strike $(S-K)^2$ , Maturity T = 1



seed(2000)
S=[]
vT = []
for i in range(I):
    path = []
    for t in range(N+1):
        if t == 0:
            path.append(S0)
        else:
            wt = gauss(0.0,1.0)
            #
            # add code for St 
            St =path[t-1] * exp((r-0.5*sigma**2) * dt + sigma *sqrt(dt) *wt)
            path.append(St)
    S.append(path)
    
#
# Add option pricing
StrikeA = 105
sumC = 0
for i in range(I):
    vT.append(max((S[i].pop()-StrikeA),0)) #call option pay off
    sumC+=vT[i]
Call1 = sumC/I
sumP = 0
vT2 = []
for i in range(I):
    vT2.append(max(0,(StrikeA-S[i].pop()))) #put option pay off
    sumP+=vT2[i]
Put1 = sumP/I

sumC2 = 0
vT3 = []
for i in range(I):
    STi = S[i].pop()
    if (STi-StrikeA)>0:
        vT3.append((STi-StrikeA)*(STi-StrikeA)) # new option pay off
    else:
        vT3.append(0)
    sumC2+=vT3[i]
Call2 = sumC2/I
