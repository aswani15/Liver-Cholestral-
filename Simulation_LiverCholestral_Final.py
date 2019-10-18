import scipy.integrate as sci
import numpy as np
#import pylab as pl
import matplotlib.pyplot as plt  
from scipy.interpolate import make_interp_spline, BSpline

#k=1070   
k=1500

#620
#720
#900
#1050
#1500

k21= 0.4 #1    
mi=1
mo=1.4  
mtis=0.234
mdiet= 0.4
k12=3.5


#g=90
v1=12
v2=43
#v3=43
mu=0.4
#86400
timesteps=np.array(range(1,129600))
timesteps1=timesteps/(24*60)
#186400))
#mo=1.4
mu=0.4/1440

INPUT = [2400, 8600]#,6000]
def diff_eqs(t,INP):
    
   #defining array
    Y=np.zeros((2))
   #Defining vector with time dependency
    M = INP    
    Y[0] = (k/M[0])+ (k21*M[1])-(k12*M[0])+ mi-mo
    #Y[1] = (-k21*M[1])+(k12*M[0])-mtis+ mdiet 
    Y[1] =(-k21*M[1])+(k12*M[0])-mtis+ mdiet-mu
    
    return Y   
 

 
RESULT = sci.solve_ivp(diff_eqs,[0,129600],INPUT,t_eval=np.array(timesteps),method='RK45')
Y=RESULT
merged = np.hstack([i.reshape(-1,1) for i in Y.y])
print merged[:,1]

##C2 is m2/v2
#Plot graph

#pl.ylim(0, 500)

#pl.plot(timesteps1,merged[:,1]/v2, 'g-', label='Synthesis Rate :'+str(k))

#pl.text(timesteps,merged[:,1]/v2, 'cholestral', label='concentration in C2:, K : '+str(k))
#pl.plot(timesteps1,merged[:,0]/v1, 'y--', label='concentration in blood liver C1 : K '+str(k))
#pl.plot(timesteps,merged[:,1]/v2, '-ro', label='concentration in blood stream-Impaired Kidney')
  
#plt.legend('k = '+str(k))
plt.plot(timesteps1,merged[:,1]/v2,color='blue')  
#plt.legend(label='850 orange 500 yellow green 680'  green 620 )   
plt.xlabel('Time(Days)')
plt.ylabel('Blood cholesterol (mg/dl) ')
#fig = plt.gcf()
#fig.set_size_inches(10, 5)
plt.show()

plt.title('Concentration of cholesterol in Blood Stream :C2'  )
#pl.xlabel('Time(Days)')
#pl.ylabel('Blood cholesterol (mg/dl')
#pl.show()
