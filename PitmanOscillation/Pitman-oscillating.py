
# coding: utf-8

# In[4]:

#get_ipython().magic(u'pylab inline') # this line of code was created automatically by 
from pylab import *

# In[16]:

# Define parameters
# . is to create flotting points numbers and not a integer
# ** to the power

R_SS = 2.5*10.**-5 #Subsidence rate in m/yr
P = 10.**8 # Period of sea level oscillations in years
slope = 1./5000.
omega = 2.*pi/P # angular frequency
D = 2.5*10**5 # in meters
Psi = R_SS/(slope*D*omega)

# Define timestep and number of steps
dt = 0.001 # t* is t/periode of oscillation
nsteps = 1500
x = zeros(nsteps+1) # will be filled later with numbers !! this is xstar!!
x[0] = 1./(Psi**2.+1) #0
t = arange(nsteps+1)*dt # pour avoir le temps, il faut multiplier par dt ( le time step) !! this is tstar!!
for tstep in arange(nsteps): # arange(nsteps) = [0,1,2,3,... nsteps-1] and step1, tstep=0, at step2, tspep=1,...
    dx_dt = -2.*pi*sin(2.*pi*t[tstep]) - 2.*pi*Psi*x[tstep]
    x[tstep+1] = x[tstep] = dt*dx_dt


# In[17]:

x_true = -1./sqrt(Psi**2. + 1.)*sin(2.*pi*t - arctan(1./Psi))
y_sl = 0.1*cos(2.*pi*t)
figure()
plot(t,x)
plot(t,x_true, 'k--')
plot(t,y_sl, ':')
legend(['Numerical', 'Analytical','Sea level'])
xlabel('Time')
ylabel('Shoreline position')


# In[7]:

print dx_dt


# In[ ]:

# 2nd order accurate

for tstep in arange(nsteps): # arange(nsteps) = [0,1,2,3,... nsteps-1] and step1, tstep=0, at step2, tspep=1,...
    x[tstep+1] = x[tstep] + dt ( dx[tstep]/dt[tstep] + dx)
    
    dx_dt = -2.*pi*sin(2.*pi*t[tstep]) - 2.*pi*Psi*x[tstep]
     = x[tstep] = dt*dx_dt


