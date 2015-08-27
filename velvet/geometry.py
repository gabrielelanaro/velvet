import numpy as np

class Transformation:
    
    def __init__(self, matrix=None):
        '''Perform geometric transformations on homogeneous coordinates'''
        if matrix is None:
            self.matrix = np.eye(3, 'float')
        else:
            self.matrix = np.asarray(matrix, 'float')

    def translate(self, xy):
        m = np.eye(3, 'float')
        m[0:1, 2] = xy
        return self.apply(m)
    
    def scale(self, xy):
        xy = np.asarray(xy)
        m = np.eye(3, 'float')
        
        if len(xy) == 1:
            m[0, 0] = xy
            m[1, 1] = xy
            
        elif len(xy) == 2:    
            m[0, 0] = xy[0]
            m[1, 1] = xy[1]
        else:
            raise ValueError('xy has to be either a scalar or a 2D array')
        return self.apply(m)

    def rotate(self, theta):
        raise NotImplementedError()
    
    def skew(self, arg):
        raise NotImplementedError()

    def apply(self, matrix):
        matrix = np.asarray(matrix, 'float')
        self.matrix = matrix.dot(matrix)
        return self
