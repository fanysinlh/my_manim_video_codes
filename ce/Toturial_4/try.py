from manim import *

class Try(Scene):
    def construct(self):
        c = Circle()
        t = Triangle()
        self.add(c, t)
        self.wait()
        self.play(t.animate.scale(2), c.animate.scale(2))
        self.wait()
