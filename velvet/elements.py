from .primitives import Rectangle, Point
from .geometry import Box, Transformation

class Panel(object):
    
    def __init__(self, start, end):
        self.primitives = [ Rectangle(start, end) ]
        self.bounding_box = Box(start, end)

    def plot(self, x, y):
        for xy in zip(x, y):
            self.primitives.append(Point(xy))
        return self

    def copy(self):
        obj = Panel.__new__(Panel)
        obj.primitives = [p for p in self.primitives]
        obj.bounding_box = self.bounding_box
        return obj

    def transform(self, t):
        obj = self.copy()
        obj.primitives = [p.transform(t) for p in self.primitives]
        obj.bounding_box = self.bounding_box.transform(t)
        
        return obj
