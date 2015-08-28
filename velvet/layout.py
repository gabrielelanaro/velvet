from __future__ import division
from .geometry import Transformation

class Layout:
    
    def __init__(self, width=600, height=600):
        # We use this guy to put elements
        self.children = []
        self.child_transform = {}
    
    def add(self, object, position):
        """Add an object at position"""
        self.children.append(object)
        self.child_transform[object.id] = Transformation().translate(position)
        
    def get_primitives(self):
        return sum([c.get_primitives(self.child_transform[c.id]) 
                    for c in self.children], [])

class Container(Layout):
    
    def __init__(self, object, width=600, height=600):
        """Container gets a single child and puts it at its origin"""
        self.child = object
        
    @property
    def primitives(self):
        bb = self.object.bounding_box(self.resolution)
        # Transform the child
        t = Transformation().translate(bb.start).scale([1/bb.width, 1/bb.height])
        tobj = self.object.transform(t).transform(self.transformation)
        return tobj.primitives     

    def transform(self, f):
        c = Container(self.object)
        c.resolution = self.resolution
        c.transformation = f
        return c
