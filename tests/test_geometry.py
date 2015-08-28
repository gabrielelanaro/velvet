from velvet.geometry import Transformation
import numpy as np
from nose.tools import ok_, eq_
from .tools import npeq_

def test_translate():
    coords = np.array([[0, 0], [0, 1], [1, 1], [1, 0]])
    trs = Transformation().translate([0.1, 0.0]).apply(coords)
    npeq_(trs, [[0.1, 0], [0.1, 1], [1.1, 1], [1.1, 0]])

def test_flip():
    coords = np.array([[0, 0], [0, 1], [1, 1], [1, 0]])
    trs = (Transformation()
           .translate([-0.5, -0.5])
           .scale([-1, 1])
           .translate([0.5, 0.5])
           .apply(coords))
    npeq_(trs, [[1, 0], [1, 1], [0, 1], [0, 0]])
