import cairo
import math
from .geometry import Transformation

class CairoRenderer:
    
    def __init__(self, filename, width=600, height=600):
        # We expect the object to be in normalized screen space
        self.surface = cairo.SVGSurface(filename, width, height)
        self.cr = cairo.Context(self.surface)
        
        self.cr.scale(width, height)
        
    def render(self, object): 
        cr = self.cr
        cr.set_line_width(0.01)
        
        for primitive in object.primitives:
            if primitive.type == 'rect':
                cr.rectangle(primitive.start[0], primitive.start[1], 
                             primitive.end[0], primitive.end[1])
                cr.set_source_rgb(0, 0, 0)
                cr.fill()
            if primitive.type == 'point':
                cr.translate(primitive.position[0], primitive.position[1])
                cr.set_source_rgb(0.7, 0.2, 0.0)
                cr.arc(0, 0, 0.01, 0, 2*math.pi)
                cr.stroke()
        
        cr.show_page()
        self.surface.finish()
