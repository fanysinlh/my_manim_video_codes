from manim import *
class Demo(Scene):
    def construct(self):
        # 爱
        s1 = Square(color=RED, fill_opacity=0.5)
        c1 = Circle(color=RED, fill_opacity=0.5).move_to(s1.get_top())
        c2 = c1.copy().move_to(s1.get_right())
        heart = VGroup(s1, c1, c2).rotate(45*DEGREES)
        self.play(Create(s1), Create(c1), Create(c2))
        self.wait()
        self.play(heart.animate.to_edge(LEFT, buff=1.5))
        self.wait()

        # 死
        r1 = Rectangle(color=RED, fill_opacity=0.5, 
                       height=4, width=4/5).rotate(45*DEGREES)
        r2 = r1.copy().rotate(90*DEGREES)
        death = VGroup(r1, r2)
        self.play(Create(r1), Create(r2))
        self.wait()

        # 机器人
        s2 = Square(color=RED, fill_opacity=0.5, 
                    side_length=(4 + 4/5)/2**0.5)
        c_small1 = Circle(fill_color=BLACK, stroke_color=RED, fill_opacity=0.5,
                          radius=0.5).move_to([-0.7, 0.7, 0])
        c_small2 = c_small1.copy().move_to([0.7, 0.7, 0])
        robot = VGroup(s2, c_small1, c_small2).to_edge(RIGHT, buff=1.5)
        self.play(Create(s2))
        self.play(Create(c_small1), Create(c_small2))
        self.wait()

        # 变透明度
        biggroup = VGroup(heart, death, robot)
        self.play(biggroup.animate.set_opacity(1))
        self.wait()
