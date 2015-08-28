from __future__ import division
import cairocffi as cairo
import math
from .geometry import Transformation

class CairoRenderer:
    
    def __init__(self, filename, width=600, height=600):
        # We expect the object to be in normalized screen space
        self.width, self.height = width, height
        self.surface = cairo.SVGSurface(filename, width, height)
        self.cr = cairo.Context(self.surface)
        
        self.cr.translate(width/2, height/2)
        self.cr.scale(1, -1)
        self.cr.translate(-width/2, -height/2)
        
    def render(self, primitives): 
        cr = self.cr
        cr.set_line_width(1)
        
        for primitive in primitives:

            if primitive['type'] == 'rect':
                cr.rectangle(primitive['position'][0], primitive['position'][1], 
                             primitive['width'], primitive['height'])
                
                cr.set_source_rgb(0, 0, 0)
                cr.fill()

            if primitive['type'] == 'point':
                cr.set_source_rgb(0.7, 0.2, 0.0)
                cr.arc(primitive['position'][0], primitive['position'][1], 5, 0, 2*math.pi)
                cr.fill()

            if primitive['type'] == 'text':
                cr.show_text(primitive.text)
                cr.rectangle(primitive.position[0], primitive.position[1], 
                             primitive.bounding_box.width, primitive.bounding_box.height)
                cr.set_source_rgb(0, 0, 0)
                cr.fill()                
        
        cr.show_page()
        self.surface.finish()
