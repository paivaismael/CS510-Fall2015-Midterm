import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Attractor(object):
    def __init__(self,s=10.,p=28.,b=8./3.,start=0.0,end=80.0,points=10000):
        self.params=np.array([s,p,b])
        self.start=start
        self.end=end
        self.points=int(points)
        self.dt=(self.end-self.start)/self.points
        self.solution=pd.DataFrame([])
    def euler(self,r=np.array([])):
        x,y,z=r
        kx=self.params[0]*(y - x)
        ky=x*(self.params[1] - z) - y
        kz=x*y-self.params[2]*z
        return np.array([kx,ky,kz])
    def rk2(self,r=np.array([])):
        k1=self.euler(r)
        r1=np.array([r[0]+k1[0]*self.dt/2,r[1]+k1[1]*self.dt/2,r[2]+k1[2]*self.dt/2])
        return self.euler(r1)
    def rk4(self,r=np.array([])):
        k2=self.rk2(r)
        r2=np.array([r[0]+k2[0]*self.dt/2,r[1]+k2[1]*self.dt/2,r[2]+k2[2]*self.dt/2])
        k3=self.euler(r2)
        r3=np.array([r[0]+k3[0]*self.dt,r[1]+k3[1]*self.dt,r[2]+k3[2]*self.dt])
        return self.euler(r3)
    def evolve(self,x0=0.1,y0=0.0,z0=0.0,order=1):
        x=np.zeros(1+self.points)
        y=np.zeros(1+self.points)
        z=np.zeros(1+self.points)
        t=np.linspace(self.start,self.end,1+self.points,endpoint=True)
        x[0]=x0
        y[0]=y0
        z[0]=z0
        i=1
        if order==1:
            while i<= self.points:
                k1=self.euler(np.array([x[i-1],y[i-1],z[i-1]]))
                x[i]=x[i-1]+k1[0]*self.dt
                y[i]=y[i-1]+k1[1]*self.dt
                z[i]=z[i-1]+k1[2]*self.dt
                i+=1
        elif order==2:
            while i<= self.points:
                k2=self.rk2(np.array([x[i-1],y[i-1],z[i-1]]))
                x[i]=x[i-1]+2*k2[0]*self.dt
                y[i]=y[i-1]+2*k2[1]*self.dt
                z[i]=z[i-1]+2*k2[2]*self.dt
                i+=1
        elif order==4:
            while i<= self.points:
                k4=self.rk4(np.array([x[i-1],y[i-1],z[i-1]]))
                x[i]=x[i-1]+k4[0]*self.dt
                y[i]=y[i-1]+k4[1]*self.dt
                z[i]=z[i-1]+k4[2]*self.dt
                i+=1
        else:
            order=input('Please choose 1, 2, or 4 for the order input: ')
            self.evolve(x0,y0,z0,order)
        sol=pd.DataFrame(data=[t,x,y,z],index=['t', 'x', 'y', 'z'])
        self.solution=pd.DataFrame.transpose(sol)
        return self.solution
    def save(self):
        self.solution.to_csv('save_solution.csv')
    def plotx(self):
        plt.plot(self.solution['t'],self.solution['x'])
        plt.show()
    def ploty(self):
        plt.plot(self.solution['t'],self.solution['y'])
        plt.show()
    def plotz(self):
        plt.plot(self.solution['t'],self.solution['z'])
        plt.show()
    def plotxy(self):
        plt.plot(self.solution['x'],self.solution['y'])
        plt.show()
    def plotyz(self):
        plt.plot(self.solution['y'],self.solution['z'])
        plt.show()
    def plotzx(self):
        plt.plot(self.solution['z'],self.solution['x'])
        plt.show()
    def plot3d(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(self.solution['x'], self.solution['y'], self.solution['z'])
        plt.show()