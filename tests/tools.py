import numpy as np
from nose.tools import eq_, ok_

def npeq_(a, b):
    b = np.asarray(b)
    a = np.asarray(a)
    ok_(np.all(a == b), '\n{} != \n{}'.format(a, b))
