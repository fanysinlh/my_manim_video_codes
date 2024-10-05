from manim import *

class Try(Scene):
    def construct(self):
        e = Ellipse().move_to(UP*3.4)
        an = Annulus().scale(0.5).move_to(UP*1.5)
        se = Sector().scale(2).move_to(DOWN*0.5)
        anse = AnnularSector().move_to(DOWN*2.9)
        self.add(e, an, se, anse)
