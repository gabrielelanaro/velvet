import numpy as np

class Primitive:
    pass
    
class Rectangle(Primitive):
    
    type = 'rect'
    
    def __init__(self, start, end):
        self.start = np.asarray(start)
        self.end = np.asarray(end)

    def copy(self):
        return Rectangle(self.start, self.end)

    def transform(self, t):
        obj = self.copy()
        obj.start = t.apply(self.start)
        obj.end = t.apply(self.end)
        return obj
        
class Point(Primitive):
    
    type = 'point'
    
    def __init__(self, position):
        self.position = np.asarray(position)

    def copy(self):
        return Point(self.position)

    def transform(self, t):
        obj = self.copy()
        obj.position = t.apply(self.position)
        return obj
