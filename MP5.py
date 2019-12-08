
#importing libraries to be used
import matplotlib.pyplot as mpl
import numpy as np 

n = np.arange(200)

#user input function 

def MP5 (x):
   y = list(range(200))
   
#looping statement for the function 
   for z in range (0,200):
       
        if n[z] == 0:    
            y[z] = -1.5*x[z] + 2*x[z+1]- 0.5*x[z+2]; 
            
        elif n[z] <= 198: #if n(z) is <198
            
            y[z] = 0.5*x[z+1] - 0.5*x[z-1]; 
            
        else :    #if n(z) is not = 0 and n is <198
            
            y[z] = 1.5*x[z] - 2*x[z-1] + 0.5*x[z-2];
            
#plotting the function using the mpl.plot function        
   mpl.plot(n,x,'g--')
   mpl.plot(n,y,'m--')
   mpl.xlabel('x(n)')
   mpl.ylabel('y(n)')
   mpl.legend('x','y')
   mpl.title('plot of x(n) and y(n)')
   mpl.grid()
   
   
   
   

