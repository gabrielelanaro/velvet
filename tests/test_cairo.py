from velvet.layout import Container, Layout
from velvet.elements import Panel, TextBox
from velvet.cairo_ import CairoRenderer
from nose.tools import eq_, ok_
import numpy as np

def test_render():
    r = CairoRenderer('/tmp/hello.svg', 600, 600)
    r.render([{'type': 'point', 
               'position': [10, 10]},
              {'type': 'rect',
               'position': [300, 300],
               'width': 100,
               'height': 200}])
    

def test_scatter():
    object = Panel(200, 200)
    
    object.scatter(np.arange(0, 1, 0.1), np.arange(0, 1, 0.1))
    
    r = CairoRenderer('/tmp/hello.svg', width=400, height=400)
    r.render(object.get_primitives())

def test_twopanels():
    p1 = Panel(200, 200)
    p2 = Panel(50, 50)
    p1.scatter(np.arange(0, 1, 0.1), np.arange(0, 1, 0.1))
    p2.scatter(np.arange(0, 1, 0.1), np.arange(0, 1, 0.1)[::-1])
    
    
    layout = Layout(400, 600)
    layout.add(p1, [0, 0])
    layout.add(p2, [250, 0])
    
    r = CairoRenderer('/tmp/hello.svg', width=400, height=200)
    r.render(layout.get_primitives())



def test_text():
    object = TextBox('Hello', [0, 0])
    c = Container(object)
    r = CairoRenderer('/tmp/hello.svg', width=300, height=300)
    r.render(c)
