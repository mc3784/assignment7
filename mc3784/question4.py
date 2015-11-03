import numpy as np
import matplotlib.pyplot as plt
print "#4 question: see file mandelbrot.png"


class Mandelbrot():
    N_max=0
    some_threshold=0
    
    def __init__(self,N_max=50,some_threshold=50):
        self.N_max=N_max
        self.some_threshold=some_threshold
    
    def generateMask(self):
        x,y=np.ogrid[-2:1:1000j,-1.5:1.5:1000j]
        c=x + 1j*y
        z=0  
        for v in range(self.N_max):
            z=z**2 + c
        mask=np.abs(z) < self.some_threshold
        return mask
    
    def generateplot(self): 
        mask=self.generateMask()
        plt.imshow(mask.T, extent=[-2, 1, -1.5, 1.5])
        plt.gray()
        plt.savefig('mandelbrot.png')

if __name__ == '__main__':
    mandelbrot=Mandelbrot() 
    mandelbrot.generateplot()  

    