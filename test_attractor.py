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
        assert self.a.params[0]==self.s
        assert self.a.params[1]==self.p
        assert self.a.params[2]==self.b
        assert self.a.dt==(self.end-self.start)/self.points
    def test_euler(self):
        """Test if euler is generating the correct answer"""
        self.a=Attractor(1.,1.,1.,0.,80.,101)
        assert self.a.euler(np.array([2,3,4]))[0]==1.
        assert self.a.euler(np.array([2,3,4]))[1]==-9.
        assert self.a.euler(np.array([2,3,4]))[2]==2.
    def test_solve(self):
        """Test if solve is printing in the CSV file"""
        os.remove('save_solution.csv')
        self.a.save()
        data=open('save_solution.csv','r')
        d=data.read()
        assert len(d)>0