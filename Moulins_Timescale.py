

from pylab import * 
#get_ipython().magic(u'pylab inline') # for jupyter
from scipy.integrate import odeint


# MOULIN'S WATER LEVEL TIMESCALE FLUCTUATIONS
#############################################
# use: 
# a) Reservoir-constriction equation from eq(5a)&(5b)
# b) Creep equation from eq(6) in Covington(2012)-> derived from Spring&Hutter(1981), 
#    and also used in Arnold et al.(1998) model


# In[1]:

# RESERVOIR-CONSTRICTION
########################
# D_h = small variation in waterlevel
#


# Inputs
R = 10. #m^3/s


# Parameters of the moulin
r = 4.
Ar = pi*r**2. # m^2


# Parameters of the conduit
# Ac = pi*(D**2)/4. 
L = 1000. #m
f = 0.1 #unitless

# Friction
Cf = 1. + f*L/D

# melt & creep
rhow=1000. # kg/m^3, density of water
rhoi=900. # kg/m^3, density of ice


# Pw = # Conduit water pression = h
Pi = 500. # m, Ice overburden
Lf = 3.34*10.**5 # J/kg
n = 3. # Unitless, ice flow law exponent
B = 5.8*10.**7 # N/m^2*s, Arrhenius parameter

initialpara=[200.,3.] # initial h, initial conduit diameter

def dh_dt(parameter, time, args=()):
    Fh,FAc = parameter
    fD = sqrt(FAc*4./pi)
    fCf = 1. + f*L/fD
    fPwet = 2.*pi*fD # conduit wetted perimeter
    fQ = FAc*sqrt(2.*g*Fh/fCf)
    fmelt = (f*rhow*fPwet*fQ**3.)/(8.*rhoi*Lf*FAc**3.)
    fcreep = (2.*(1./n*B)**n)*FAc(Pi-Fh)*abs(Pi-Fh)**(n-1.)
    return (R - fQ)/Ar, fmelt-fcreep

# hours = 4 ;  duration = hours*3600
# tstep = duration/100

# t = linspace(0,duration,tstep)

t = linspace(0,10000,100)
result = odeint(dh_dt, initialpara, t, args=())


# In[44]:

print para


# In[ ]:




# In[ ]:



