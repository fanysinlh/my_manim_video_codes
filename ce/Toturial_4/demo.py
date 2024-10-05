from manim import *

class Demo_1(Scene):
    def construct(self):
        plane = NumberPlane()
        for i in plane.submobjects:
            i.set_opacity(0.3)
        self.play(Create(plane))
        self.wait()

        s = Square()
        self.play(Create(s))
        self.wait()
        self.play(s.animate.scale(2))
        self.wait()
        self.play(Uncreate(s))
        self.wait()

        c = Circle()
        self.play(Create(c))
        self.wait()
        self.play(c.animate.scale(2))
        self.wait()
        self.play(Uncreate(c))
        self.wait()

        a = Arc()
        self.play(Create(a))
        self.wait()
        self.play(a.animate.become(Arc(radius=2)))
        self.wait()
        self.play(a.animate.become(Arc(radius=2, start_angle=-TAU / 4)))
        self.wait()
        self.play(a.animate.become(Arc(radius=2, start_angle=-TAU / 4, angle=TAU / 2)))
        self.wait(5)
        self.play(a.animate.become(Arc(radius=2, start_angle=-TAU / 4, angle=TAU / 2, arc_center=LEFT)))
        self.wait()
        self.play(Uncreate(a))
        self.wait()

        r = Rectangle()
        self.play(Create(r))
        self.wait()
        self.play(r.animate.stretch_to_fit_height(4).stretch_to_fit_width(2))
        self.wait()
        self.play(Uncreate(r))
        self.wait()

        t = Triangle()
        self.play(Create(t))
        self.wait()
        self.play(Uncreate(t))
        self.wait()

        p = Polygon(LEFT, RIGHT, UP, UL)
        self.play(Create(p))
        self.wait()
        self.play(Uncreate(p))
        self.wait(5)


        l = Line()
        self.play(Create(l))
        self.wait()
        self.play(l.animate.become(Line(buff=0.2)))
        self.wait()
        self.play(l.animate.become(Line(path_arc=PI)))
        self.wait()
        self.play(l.animate.become(Line(path_arc=-PI)))
        self.wait()
        self.play(Uncreate(l))
        self.wait()

        ar = Arrow()
        self.play(Create(ar))
        self.wait()
        self.play(ar.animate.become(Arrow(buff=0)))
        self.wait()
        self.play(Uncreate(ar))
        self.wait(5)


        d = Dot()
        self.play(Create(d))
        self.wait()
        self.play(Uncreate(d))
        self.wait()


        e = Ellipse().move_to(UP*3.4)
        an = Annulus().scale(0.5).move_to(UP*1.5)
        se = Sector().scale(2).move_to(DOWN*0.5)
        anse = AnnularSector().move_to(DOWN*2.9)
        for i in [e, an, se, anse]:
            self.play(Create(i))
            self.wait()
        self.play(Uncreate(VGroup(e, an, se, anse)))
        self.wait()
