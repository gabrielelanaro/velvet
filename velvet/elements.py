from __future__ import division
from .primitives import Point, Text
from .geometry import Box, Transformation, distance
import numpy as np
import itertools

unique = itertools.imap(str, itertools.count())

class Panel(object):
    
    def __init__(self, width, height, xlim=[0, 1], ylim=[0, 1]):
        self.id = 'panel_' + next(unique)
        self.width = width
        self.height = height
        self.xlim = xlim
        self.ylim = ylim
        self.data = []
        
        data_width = self.xlim[1] - self.xlim[0]
        data_height = self.ylim[1] - self.ylim[0]
        # Takes a coordinate in data, returns a coordinate in 
        # Panel coordinates
        self.data_transform = (Transformation()
                               .scale([width/data_width, height/data_height]))
        
    def scatter(self, x, y):
        
        for xy in zip(x, y):
            self.data.append(xy)
        
        return self
    
    def get_primitives(self, transform=Transformation()):
        res = []
        for xy in self.data:
            res.append({'type': 'point', 
                        'position': transform.apply(self.data_transform.apply(xy))})
        return res

class TextBox(object):
    
    def __init__(self, text, position):
        self.id = 'text_' + next(unique)
        self.position = np.asarray(position, dtype='float')
        self.text = text
        self.primitives = [Text(text, position)]
        print self.position, self.primitives
    
    def bounding_box(self, resolution):
        return self.primitives[0].get_bounding_box()

    def transform(self, t):
        print self.position
        print t.matrix
        print t.apply(self.position)
        return TextBox(self.text, t.apply(self.position))

class Rectangle(object):
    
    def __init__(self, width, height):
        self.id = 'rect_' + next(unique)
        self.width = np.asarray(width)
        self.height = np.asarray(height)
    
    def get_primitives(self, transform=Transformation()):
        position = transform.apply([0.0, 0.0])
        y = transform.apply([0.0, self.height])
        x = transform.apply([self.width, 0.0])
        
        return [{'type': 'rect', 
                 'position': position, 
                 'width': distance(position, x), 
                 'height': distance(position, y)}]
        
    def __repr__(self):
        return "<Rectangle {}{}>".format(self.width, self.height)
