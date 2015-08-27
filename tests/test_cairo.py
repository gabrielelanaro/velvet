from velvet.layout import Container
from velvet.elements import Panel
from velvet.cairo_ import CairoRenderer
from nose.tools import eq_, ok_



def test_render_box():
    object = Panel([0, 0], [10, 10])
    
    c = Container(object)
    r = CairoRenderer('/tmp/hello.svg', width=300, height=300)
    r.render(c)

def test_plot():
    object = Panel([0, 0], [10, 10])
    object.plot([0, 1], [0, 1])
    
    c = Container(object)
    r = CairoRenderer('/tmp/hello.svg', width=300, height=300)
    r.render(c)
