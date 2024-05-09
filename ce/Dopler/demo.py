from manim import *

class Demo(Scene):
    def construct(self):
        s = SVGMobject("ce/Dopler/外星.svg").scale(0.5)
        receive = s.copy().to_edge(RIGHT)
        times = DecimalNumber(0, 0).next_to(receive, UP)
        miu = ValueTracker(0)
        viu = MathTex(rf"\nu = {int(miu.get_value())}").to_corner(UR)
        viu.add_updater(lambda m: m.become(MathTex(rf"\nu = {int(miu.get_value())}") \
                                           .to_corner(UR)))
        self.add(miu)
        self.play(FadeIn(VGroup(s, receive, times, viu)))
        s.add_updater(lambda mob, dt: mob.shift(dt*RIGHT*0.25))
        cmap = {}
        def c_updater(mob: DecimalNumber):
            for key, values in cmap.items():
                if (
                    values and
                    sum((key.points[0] - key.get_center())**2)
                    >= sum((receive.get_center() - key.get_center())**2) - 0.1
                ):
                    mob.set_value(mob.get_value() + 100)
                    cmap[key] = False
        times.add_updater(c_updater)

        tm = self.renderer.time
        num = times.get_value()
        def n_updater(mob: ValueTracker):
            nonlocal tm, num
            if (
                times.get_value() != num
            ):
                mob.set_value(100/(self.renderer.time - tm))
                tm = self.renderer.time
                num = times.get_value()
        miu.add_updater(n_updater)

        def change():
            for _ in range(10):
                c = Circle(radius=0.1, fill_opacity=0, stroke_color=RED).move_to(s.get_center())
                def sc(s):
                    return lambda mob, dt: mob.scale_to_fit_width(mob.width + dt)
                c.add_updater(sc(self))
                self.add(c)
                self.add(receive, times, viu)
                cmap[c] = True
                self.wait(1)

        change()
        s.clear_updaters()
        s.add_updater(lambda mob, dt: mob.shift(dt*RIGHT*0.15))
        change()
        s.clear_updaters()
        s.add_updater(lambda mob, dt: mob.shift(dt*LEFT*0.25))
        change()
        self.wait(10)

class Demo2(Scene):
    def construct(self):
        s = SVGMobject("ce/Dopler/外星.svg").scale(0.5)
        receive = s.copy().to_edge(RIGHT)
        times = DecimalNumber(0, 0).next_to(receive, UP)
        miu = ValueTracker(0)
        viu = MathTex(rf"\nu = {int(miu.get_value())}").to_corner(UR)
        viu.add_updater(lambda m: m.become(MathTex(rf"\nu = {int(miu.get_value())}") \
                                           .to_corner(UR)))
        self.add(miu)
        self.play(FadeIn(VGroup(s, receive, times, viu)))
        cmap = {}
        def c_updater(mob: DecimalNumber):
            for key, values in cmap.items():
                if (
                    values and
                    sum((key.points[0] - key.get_center())**2)
                    >= sum((receive.get_center() - key.get_center())**2) - 0.1
                ):
                    mob.set_value(mob.get_value() + 100)
                    cmap[key] = False
        times.add_updater(c_updater)

        tm = self.renderer.time
        num = times.get_value()
        def n_updater(mob: ValueTracker):
            nonlocal tm, num
            if (
                times.get_value() != num
            ):
                mob.set_value(100/(self.renderer.time - tm))
                tm = self.renderer.time
                num = times.get_value()
        miu.add_updater(n_updater)

        cgtm = self.renderer.time
        def change(mob: SVGMobject):
            nonlocal cgtm
            if self.renderer.time - cgtm >= 1:
                c = Circle(radius=0.1, fill_opacity=0, stroke_color=RED).move_to(s.get_center())
                def sc(s):
                    return lambda mob, dt: mob.scale_to_fit_width(mob.width + dt)
                c.add_updater(sc(self))
                self.add(c)
                self.add(receive, times, viu)
                cmap[c] = True
                cgtm = self.renderer.time

        s.add_updater(change)

        c = Arc(angle=180*DEGREES, arc_center=RIGHT)
        cp = Arc(angle=180*DEGREES, arc_center=LEFT)
        dl = Line(start=2*LEFT, end=2.5*DOWN, path_arc=50*DEGREES)
        dr = Line(2.5*DOWN, 2*RIGHT, path_arc=50*DEGREES)
        poly = Polygon(*c.get_all_points(), *cp.get_all_points(), 
                       *dl.get_all_points(), *dr.get_all_points()).scale(1.5).shift(UP)
        self.play(s.animate.move_to(poly.get_start()), run_time=0.5)
        self.wait(0.5)
        self.play(MoveAlongPath(s, poly), run_time=60, rate_func=linear)
        self.wait(0.5)
        self.play(s.animate.move_to(poly.get_start()), run_time=0.5)
        self.wait(0.5)
        self.play(MoveAlongPath(s, poly), run_time=60, rate_func=linear)
        self.wait(10)
        

class Intro(Scene):
    def construct(self):
        alien = SVGMobject("ce/Dopler/外星.svg")
        text = Text("这是个外星飞船，它正在不停地发出信号。").next_to(alien, UP*3)
        self.add(alien, text)
