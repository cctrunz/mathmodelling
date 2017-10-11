
# coding: utf-8

# In[15]:

#for python notebook (in Jupyter)
get_ipython().magic(u'pylab inline')
from scipy.integrate import odeint

#for python file (in spider)
# from pylab import * 


# In[16]:

#Define parameters for the first previous exercice
R_SS = 2.5*10.**-5 #Subsidence rate in m/yr
P = 10.**8 #Period of sea level oscillations in years
slope = 1./5000.
omega = 2.*pi/P #angular frequency
D = 2.5 *10**5 #m
Psi = R_SS/(slope*D*omega)

#Define timestep and number of steps
dt = 0.03
nsteps = 150
x = zeros(nsteps+1)
x[0] = 1./(Psi**2.+1) #0.
t = arange(nsteps+1)*dt
for tstep in arange(nsteps):
    dx_dt = -2.*pi*sin(2.*pi*t[tstep]) - 2.*pi*Psi*x[tstep]
    x_pred = x[tstep] + dt*dx_dt
    dx_dt_x_pred = -2.*pi*sin(2.*pi*t[tstep+1]) - 2.*pi*Psi*x_pred
    x[tstep+1] = x[tstep] + dt*(dx_dt + dx_dt_x_pred)/2.


# In[22]:

#Define parameters for the Glacial-interglacial cycles
R_SS = 2.5*10.**-5 #Subsidence rate in m/yr
slope = 1./5000.
D = 2.5 *10**5 #m

Pnum = array([10.**4,10.**5,10.**6,10.**7,10.**8]) #Period of sea level oscillations in years
for pstep in Pnum(5):
    P=P(pstep)
    omega = 2.*pi/P #angular frequency
    Psi = R_SS/(slope*D*omega)
    #Define timestep and number of steps
    dt = 0.03
    nsteps = 150
    x = zeros(nsteps+1)
    x[0] = 1./(Psi**2.+1) #0.
    t = arange(nsteps+1)*dt
    for tstep in arange(nsteps):
        dx_dt = -2.*pi*sin(2.*pi*t[tstep]) - 2.*pi*Psi*x[tstep]
        x_pred = x[tstep] + dt*dx_dt
        dx_dt_x_pred = -2.*pi*sin(2.*pi*t[tstep+1]) - 2.*pi*Psi*x_pred
        x[tstep+1] = x[tstep] + dt*(dx_dt + dx_dt_x_pred)/2.
      


# In[17]:

def dx_dt(xi, ti, Psi):
    return -2.*pi*sin(2.*pi*ti) - 2.*pi*Psi*xi

# Ode-int solves similar to 4th order Rungar-Kutta, just easier and faster, but different algorithm
# less work, and better
x_ode = odeint(dx_dt, x[0], t, args=(Psi,))
figure()
plot(t, x_ode)


# In[18]:

x_true = -1./sqrt(Psi**2. + 1.)*sin(2.*pi*t - arctan(1./Psi))
y_sl = 0.1*cos(2.*pi*t)




figure()
plot(t,x)
plot(t,x_true, 'k--')
plot(t,y_sl, ':')
legend(['Numerical', 'Analytical','Sea level','glacaire'])
xlabel('Time')
ylabel('Shoreline position')


# In[ ]:



