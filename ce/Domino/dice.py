from manim import *

class Dice(VGroup):
    def __init__(self, value, **kwargs):
        faces = VGroup(
            VGroup(
              Square(side_length=2, fill_color=BLACK, fill_opacity=1),
            ),
            VGroup(
              Square(side_length=2, fill_color=BLACK, fill_opacity=1),
              Dot([0,0,0], radius=0.2),
            ),
            VGroup(
              Square(side_length=2, fill_color=BLACK, fill_opacity=1),
              Dot([-0.67,-0.67,0], radius=0.2),
              Dot([+0.67,+0.67,0], radius=0.2),
            ),
            VGroup(
              Square(side_length=2, fill_color=BLACK, fill_opacity=1),
              Dot([-0.67,-0.67,0], radius=0.2),
              Dot([0,0,0], radius=0.2),
              Dot([+0.67,+0.67,0], radius=0.2),
            ),
            VGroup(
              Square(side_length=2, fill_color=BLACK, fill_opacity=1),
              Dot([-0.67,-0.67,0], radius=0.2),
              Dot([+0.67,+0.67,0], radius=0.2),
              Dot([-0.67,+0.67,0], radius=0.2),
              Dot([+0.67,-0.67,0], radius=0.2),
            ),
            VGroup(
              Square(side_length=2, fill_color=BLACK, fill_opacity=1),
              Dot([-0.67,-0.67,0], radius=0.2),
              Dot([+0.67,+0.67,0], radius=0.2),
              Dot([0,0,0], radius=0.2),
              Dot([-0.67,+0.67,0], radius=0.2),
              Dot([+0.67,-0.67,0], radius=0.2),
            ),
            VGroup(
              Square(side_length=2, fill_color=BLACK, fill_opacity=1),
              Dot([-0.67,-0.67,0], radius=0.2),
              Dot([+0.67,+0.67,0], radius=0.2),
              Dot([-0.67,+0.67,0], radius=0.2),
              Dot([+0.67,-0.67,0], radius=0.2),
              Dot([+0.67,0,0], radius=0.2),
              Dot([-0.67,0,0], radius=0.2),
            ),
        )
        super().__init__(**kwargs)
        self.face = faces[value]
        self.add(self.face)


class TwoDice(VGroup):
    def __init__(self, first, second, **kwargs):
        super().__init__(**kwargs)
        dice1 = Dice(first)
        dice2 = Dice(second).next_to(dice1, buff=0)
        l = Line(dice1.get_corner(UR), dice1.get_corner(DR), color="#0f0f0f", buff=0.07, stroke_width=4)
        self.add(dice1, dice2, l)
        self.center()

class Try(Scene):
    def construct(self):
        self.add(TwoDice(1, 5))
