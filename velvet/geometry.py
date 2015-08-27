import numpy as np

class Transformation:
    
    def __init__(self, matrix=None):
        '''Perform geometric transformations on homogeneous coordinates'''
        if matrix is None:
            self.matrix = np.eye(3, dtype='float')
        else:
            self.matrix = np.asarray(matrix, dtype='float')

    def translate(self, xy):
        m = np.eye(3, dtype='float')
        m[0, 2] = xy[0]
        m[1, 2] = xy[1]
        return self.combine(m)
    
    def scale(self, xy):
        xy = np.asarray(xy)
        m = np.eye(3, dtype='float')
        
        if len(xy) == 1:
            m[0, 0] = xy
            m[1, 1] = xy
            
        elif len(xy) == 2:    
            m[0, 0] = xy[0]
            m[1, 1] = xy[1]
        else:
            raise ValueError('xy has to be either a scalar or a 2D array')
        return self.combine(m)

    def rotate(self, theta):
        raise NotImplementedError()
    
    def skew(self, arg):
        raise NotImplementedError()

    def combine(self, matrix):
        matrix = np.asarray(matrix, dtype='float')
        self.matrix = matrix.dot(self.matrix)
        return self

    def apply(self, coords):
        # Apply this transformation to coordinates
        coords = np.asarray(coords)
        if len(coords.shape) == 1:
            return self.matrix.dot(np.append(coords, 1))[:2]
        else:
            # Transform to homogenoeus
            ones = np.ones(len(coords))[:, np.newaxis]
            hcoords = np.concatenate([coords, ones], axis=1)
            return self.matrix.dot(hcoords.T).T[:,:2]

class Box(object):
    
    def __init__(self, start, end):
        self.start = np.asarray(start)
        self.end = np.asarray(end)
    
    def copy(self):
        return Box(self.start, self.end)

    def transform(self, t):
        obj = self.copy()
        obj.start = t.apply(self.start)
        obj.end = t.apply(self.end)
        return obj
    
    @property
    def width(self):
        return (self.end - self.start)[0]

    @property
    def height(self):
        return (self.end - self.start)[1]
