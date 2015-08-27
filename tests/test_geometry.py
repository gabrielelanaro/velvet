from velvet.geometry import Transformation
import numpy as np
from nose.tools import ok_, eq_

def npeq_(a, b):
    a = np.asarray(a)
    b = np.asarray(b)
    ok_(np.all(a == b), '{} != {}'.format(a, b))

def test_flip():
    
    coords = np.array([[0, 0], [0, 1], [1, 1], [1, 0]])
    trs = Transformation().translate([0.1, 0.0]).apply(coords)
    npeq_(trs, [[0.1, 0], [0.1, 1], [1.1, 1], [1.1, 0]])
