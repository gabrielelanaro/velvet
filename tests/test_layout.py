from velvet.layout import Container, Layout
from velvet.elements import Panel, Rectangle
from velvet.geometry import Transformation
from .tools import npeq_

def test_layout():
    
    layout = Layout()
    # Add a rectangle at position
    layout.add(Rectangle(40, 40), [0, 0])

    # Panel is a container for data
    p = Panel(400, 400, xlim=[0, 10], ylim=[0, 10])
    p.scatter([0, 5], [0, 5])
    
    layout.add(p, [10, 10])
    
    #t = Text("Hello", size=12)
    #layout.add(p, 10, 20)
    
    prim = layout.get_primitives()

    rect = prim[0]
    
    assert rect['type'] == 'rect'
    npeq_(rect['position'], [0, 0])
    assert rect['width'] == 40
    assert rect['height'] == 40
    
    point1 = prim[1]
    assert point1['type'] == 'point'
    npeq_(point1['position'], [10, 10])
    
    point2 = prim[2]
    assert point2['type'] == 'point'
    npeq_(point2['position'], [10 + 200, 10 + 200])
