import numpy as np  
import matplotlib.pyplot as plt  
def graph(formula, x_range):  
    x = np.array([0,0.3,0.7,1.3,1.5,1.8,2])
    #x=np.array(x_range)  
    y = eval(formula)    
    plt.plot(x, y)  
   
    plt.xlabel('k21 (1/min)')
    plt.ylabel('C2/C1 : Equilibrium ')
    fig = plt.gcf()
    fig.set_size_inches(5, 2.5)
    plt.show()
 #for mi  
#formula = '(3.583 *( (1500*3.58)+(x* 0.234)+(1.4*0.234)- (0.234*0.234))/ (1500*3.58))'
##for mo
#formula = '(3.583 *( (1500*3.58)+(1* 0.234)+(x*0.234)- (0.234*0.234))/ (1500*3.58))'
##for k
#formula = '(3.583 *( (x*3.58)+(1* 0.234)+(1.4*0.234)- (0.234*0.234))/ (x*3.58))'

##for k12
formula = '(3.583 *( (1500*x)+(1* 0.234)+(1.4*0.234)- (0.234*0.234))/ (1500*x))'


graph(formula, range(0, 2000))
 
 
 