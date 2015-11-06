from attractor import Attractor
import random
import numpy as np
from nose import with_setup
import os

###
# Test Suite for Attractor interface
#
# Run with the command: "nosetests"
###

class TestRandomValues:
    """Define an Attractor with random values for s, p and b, test interface"""
    def setup(self):
        """Setup fixture is run before every test method separately"""
        s=random.uniform(15,20)
        p=random.uniform(1,5)
        b=random.uniform(10,15)
        self.s=s
        self.p=p
        self.b=b
        start=0
        end=random.uniform(5,30)
        points=random.randint(5,100)
        self.start=start
        self.end=end
        self.points=points
        self.a=Attractor(s,p,b,start,end,points)
    def test_defintions(self):
        """Test the first definitions of the class"""
        assert self.a.params[0]==self.s, "\nError in the definition of self.params. The first argument should coincide with the value of s, the first input of the class.\n"
        assert self.a.params[1]==self.p, "\nError in the definition of self.params. The second argument should coincide with the value of p, the second input of the class.\n"
        assert self.a.params[2]==self.b, "\nError in the definition of self.params. The third argument should coincide with the value of b, the third input of the class.\n"
        assert self.a.dt==(self.end-self.start)/self.points, "\nError in the definition of self.dt.\n"
    def test_ks(self):
        """Test if the methods euler, rk2 and rk4 are generating the correct answer"""
        self.a=Attractor(1.,1.,1.,0.,80.,100)
        c=np.array([2,3,4])
        assert self.a.euler(c)[0]==1., "\nError in the first element of the np.array output of euler method.\n"
        assert self.a.euler(c)[1]==-9., "\nError in the second element of the np.array output of euler method.\n"
        assert self.a.euler(c)[2]==2., "\nError in the third element of the np.array output of euler method.\n"
        assert self.a.rk2(c)[0]==-3., "\nError in the first element of the np.array output of rk2 method.\n"
        assert self.a.rk2(c)[1]==-8.52, "\nError in the second element of the np.array output of rk2 method.\n"
        assert self.a.rk2(c)[2]==-6.24, "\nError in the third element of the np.array output of rk2 method.\n"
        assert self.a.rk4(c)[0]==1.97024, "\nError in the first element of the np.array output of rk4 method.\n"
        assert int(self.a.rk4(c)[1])==-4, "\nError in the second element of the np.array output of rk4 method.\n"
        assert int(self.a.rk4(c)[2])==0, "\nError in the third element of the np.array output of rk4 method.\n"
    def test_solve(self):
        """Test if solve is printing in the CSV file"""
        os.remove('save_solution.csv')
        self.a.save()
        data=open('save_solution.csv','r')
        d=data.read()
        assert len(d)>0, "\nError in the save method. It is not creating the save_solution.csv file or saving the information of self.solution in it.\n"
