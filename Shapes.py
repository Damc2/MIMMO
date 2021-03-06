
from  manimlib.imports import *

class Shapes(Scene):
    #A few simple shapes
    def construct(self):
        circle = Circle()
        square = Square()
        #line=Line(np.array([3,0,0]),np.array([5,0,0]))
        line=Line((3,0,0),(5,0,0))
        triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))
        triangle2=Polygon(np.array([5, 0, 0]),np.array([5,5,0]),np.array([1,-1,0]))
        sector = Sector()
        
        self.play(ShowCreation(circle))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.add(line)
        self.play(Transform(square,triangle))
        self.play(Transform(line,triangle2))
