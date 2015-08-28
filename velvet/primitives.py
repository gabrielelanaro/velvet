import numpy as np
from .geometry import Box

class Primitive:
    pass

from freetype import Face

class Text(Primitive):
    
    type = 'text'
    
    def __init__(self, text, position, size=12):
        self.size = size
        self.text = text
        self.position = np.asarray(position)
        self.bounding_box = self.get_bounding_box()
    
    def get_bounding_box(self):
        face = Face('UbuntuMono-R.ttf')
        face.set_char_size(self.size)
        face.load_char('g')
        total_width = 0
        total_height = 0
        for char in self.text: 
            total_width += face.glyph.metrics.width
            total_height = max(total_height, face.glyph.metrics.width)
        # For the moment return
        return Box(self.position, [total_width, total_height])

    def transform(self, t):
        return self
        
    def __repr__(self):
        return "<Text '{}',{}>".format(self.text, self.position)

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

    def __repr__(self):
        return "<Point {}>".format(self.position)
