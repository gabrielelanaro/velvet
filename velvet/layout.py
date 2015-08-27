from __future__ import division
from .geometry import Transformation

class Layout:
    pass

class Container(Layout):
    
    def __init__(self, object, parent=None):
        self.object = object

    @property
    def primitives(self):
        bb = self.object.bounding_box
        # Transform the child
        t = Transformation().translate(bb.start).scale([1/bb.width, 1/bb.height])
        tobj = self.object.transform(t)
        return tobj.primitives     

    def transform(self, f):
        return Container(self.object.transform(f))
