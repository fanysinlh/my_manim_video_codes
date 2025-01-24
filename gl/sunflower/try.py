from manimlib import *
class Try(Scene):
    def construct(self):
        c = Circle(fill_opacity=0.5)
        e = Ellipse(fill_opacity=0.5).next_to(c, LEFT).scale(2)
        un = Union(c, e)
        ungroup = VGroup()
        for i in range(3):
            ungroup.add(un.copy().rotate(i*PI*2/3, about_point=ORIGIN).set_stroke(Color().set_hsl((i/3, 1, 1))))
        self.embed()