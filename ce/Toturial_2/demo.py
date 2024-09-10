from manim import *


class CodeScene(VGroup):
    def __init__(self, file_name=None, code=None, stroke_color=WHITE, rate=0.45, *args, **kwargs):
        super().__init__()
        if file_name:
            self.code = Code(
                file_name, font="Courier New", tab_width=2, line_spacing=0.7,
                background="window", language="Python", *args, **kwargs
            )
        elif code:
            self.code = Code(
                code=code, font="Courier New", tab_width=2, line_spacing=0.7,
                background="window", language="Python", *args, **kwargs
            )
        self.screen = ScreenRectangle(
            stroke_opacity=1, stroke_color=stroke_color, stroke_width=1
        ).scale(rate*2).to_edge(LEFT)
        VGroup(
            self.screen, self.code.scale_to_fit_height(self.screen.get_height())
        ).arrange(LEFT)
        self.box = Rectangle(height=1.5, width=5, stroke_width=1, color=YELLOW) \
            .next_to(self.screen, UP)
        self.add(self.code, self.screen)

    def in_and_out(self, i, o):
        for t in i:
            self.code[2][t].set_opacity(1)
        for t in o:
            self.code[2][t].set_opacity(0.3)
        return self

    def all_out(self):
        self.code[2].set_opacity(0.3)
        return self

    def fade_another(self, i):
        return self.in_and_out([i + 1], [i])
    
    def updates(self):
        self.code.next_to(self.screen, LEFT)
        self.box.next_to(self.screen, UP)
        return self
    
    @property
    def b_center(self):
        return self.box.get_center()
    
    @property
    def s_center(self):
        return self.screen.get_center()


class Demo(Scene):
    def construct(self):
        my_scene = CodeScene("ce/Toturial_2/try.py")
        self.add(my_scene)
        self.wait()
        self.play(my_scene.animate.all_out())
        self.wait()
        self.play(my_scene.animate.in_and_out([0], []))
        self.wait()
        c = Circle(fill_opacity=1).scale(0.45).move_to(my_scene.b_center).shift(LEFT)
        ctext = Text("c", color=RED).scale(0.5).next_to(c, DOWN)
        cg = VGroup(c, ctext)
        s = Square(color=YELLOW, fill_opacity=1).scale(0.45).move_to(my_scene.b_center).shift(RIGHT)
        stext = Text("s", color=YELLOW).scale(0.5).next_to(s, DOWN)
        sg = VGroup(s, stext)
        self.play(my_scene.animate.in_and_out([1, 2], [0]))
        self.wait()
        self.play(my_scene.animate.in_and_out([3], [1, 2]))
        self.wait()
        self.play(FadeIn(cg))
        self.wait()
        self.play(my_scene.animate.fade_another(3))
        self.wait()
        self.play(FadeIn(sg))
        self.wait()
        self.play(Indicate(cg, color=RED),Indicate(sg), run_time=2.5)
        self.wait()
        self.play(my_scene.animate.fade_another(4))
        self.wait()
        cp = c.copy()
        self.play(FadeIn(cp.move_to(my_scene.s_center)))
        self.wait()
        self.play(my_scene.animate.fade_another(5))
        self.wait()
        self.play(my_scene.animate.fade_another(6))
        self.wait()
        self.play(Transform(cp, s.copy().move_to(my_scene.s_center)))
        self.wait()
        self.play(my_scene.animate.fade_another(7))
        self.wait()
        self.play(my_scene.animate.fade_another(8))
        self.wait()
        self.play(FadeOut(cp))
        self.wait()
        self.play(my_scene.animate.fade_another(9))
        self.wait()


class Demo2(Scene):
    def construct(self):
        dmmb = DEFAULT_MOBJECT_TO_MOBJECT_BUFFER
        rate = 0.45
        scenecode = '''from manim import *
class Try(Scene):
    def construct(self):
        c = Circle()
        s = Square().next_to(c)
        self.add(c, s)
        self.remove(c)'''
        my_scene = CodeScene(code=scenecode)
        self.add(my_scene)
        self.remove(*my_scene.code[2][5:7])
        c = Circle().scale(rate).move_to(my_scene.b_center).shift(LEFT)
        ctext = Text("c", color=RED).scale(0.5).next_to(c, DOWN)
        cg = VGroup(c, ctext)
        s = Square().scale(rate).move_to(my_scene.b_center).shift(RIGHT)
        stext = Text("s", color=YELLOW).scale(0.5).next_to(s, DOWN)
        sg = VGroup(s, stext)
        self.add(cg, sg)
        self.wait()
        self.play(Write(my_scene.code[2][5]))
        cp = c.copy().move_to(my_scene.s_center)
        sp = s.copy().next_to(cp, buff=dmmb*rate)
        self.add(cp, sp)
        self.wait()
        self.play(Write(my_scene.code[2][6]))
        self.remove(sp)
        self.wait()
        pos = my_scene.screen.get_center()
        scenecode2 = '''from manim import *
class Try(Scene):
    def construct(self):    
        c = Circle()
        s = Square().next_to(c)
        self.play(FadeIn(c))
        self.play(FadeOut(c), 
                  FadeIn(s))'''
        my_scene2 = CodeScene(code=scenecode2)
        my_scene2.screen.move_to(pos)
        my_scene2.updates()
        self.play(
            ReplacementTransform(my_scene.code[0], my_scene2.code[0]),
            FadeTransform(my_scene.code[1], my_scene2.code[1]),
            VGroup(*my_scene.code[2][0:5]).animate \
                .scale_to_fit_height(VGroup(*my_scene2.code[2][0:5]).get_height()) \
                .move_to(VGroup(*my_scene2.code[2][0:5])),
            ReplacementTransform(my_scene.screen, my_scene2.screen),
            FadeOut(cp, *my_scene.code[2][5:])
        )
        self.remove(*my_scene.code[2][0:5])
        self.add(*my_scene2.code[2][0:5])
        self.wait()
        self.play(Write(my_scene2.code[2][5]))
        self.wait()
        cp.move_to(my_scene2.s_center)
        sp.copy().next_to(c, buff=rate*dmmb)
        self.play(FadeIn(cp))
        self.wait()
        self.play(Write(VGroup(*my_scene2.code[2][6:8])))
        self.wait()
        self.play(FadeOut(cp), FadeIn(sp))
        self.wait()
        scenecode3 = '''from manim import *
class Try(Scene):
    def construct(self):
        c = Circle()
        self.play(FadeIn(c))
        self.wait()
        self.play(FadeOut(c))'''
        my_scene3 = CodeScene(code=scenecode3)
        my_scene3.screen.move_to(pos)
        my_scene3.updates()
        self.play(
            ReplacementTransform(my_scene2.code[0], my_scene3.code[0]),
            FadeTransform(my_scene2.code[1], my_scene3.code[1]),
            VGroup(*my_scene2.code[2][0:4]).animate \
                .scale_to_fit_height(VGroup(*my_scene3.code[2][0:4]).get_height()) \
                .move_to(VGroup(*my_scene3.code[2][0:4])),
            ReplacementTransform(my_scene2.screen, my_scene3.screen),
            FadeOut(sp, *my_scene2.code[2][4:], sg),
            cg.animate.move_to(my_scene2.b_center)
        )
        self.remove(*my_scene2.code[2][0:4])
        self.add(*my_scene3.code[2][0:4])
        self.wait()
        self.play(*[Write(my_scene3.code[2][t]) for t in range(4, 7)])
        self.wait()
        self.play(FadeIn(cp))
        self.wait()
        self.play(FadeOut(cp))
        self.wait()
        scenecode4 = '''from manim import *
class Try(Scene):
    def construct(self):
        c = Circle()
        self.play(FadeIn(c))
        self.wait(0.1)
        self.play(FadeOut(c))'''
        my_scene4 = CodeScene(code=scenecode4)
        my_scene4.screen.move_to(pos)
        my_scene4.updates()
        self.play(
            ReplacementTransform(my_scene3.code[0], my_scene4.code[0]),
            FadeTransform(my_scene3.code[1], my_scene4.code[1]),
            VGroup(*my_scene3.code[2][0:5]).animate \
                .scale_to_fit_height(VGroup(*my_scene4.code[2][0:5]).get_height()) \
                .move_to(VGroup(*my_scene4.code[2][0:5])),
            my_scene3.code[2][6].animate \
                .scale_to_fit_height(my_scene4.code[2][6].get_height()) \
                .move_to(my_scene4.code[2][6]),
            VGroup(*my_scene3.code[2][5][:-1]).animate \
                .scale_to_fit_height(VGroup(*my_scene4.code[2][5][:-4]).get_height()) \
                .move_to(VGroup(*my_scene4.code[2][5][:-4])),
            ReplacementTransform(my_scene3.code[2][5][-1], my_scene4.code[2][5][-1]),
            FadeIn(VGroup(*my_scene4.code[2][5][-4:-1])),
            ReplacementTransform(my_scene3.screen, my_scene4.screen),
        )
        self.remove(*my_scene3.code[2][0:5], my_scene3.code[2][6], *my_scene3.code[2][5][:-1])
        self.add(*my_scene4.code[2][0:5], my_scene4.code[2][6], my_scene4.code[2][5][:-4])
        self.wait()
        self.play(FadeIn(cp))
        self.wait(0.1)
        self.play(FadeOut(cp))
        self.wait()

        scenecodetry = '''from manim import *
class Try(Scene):
    def construct(self):
        c = Circle(fill_opacity=1)
        s = Square(color=YELLOW, fill_opacity=1)
        self.play(FadeIn(c))
        self.wait()
        self.play(ReplacementTransform(
            c, s
        ))
        self.wait()
        self.play(FadeOut(s))
        self.wait()

'''
        my_scene5 = CodeScene(code=scenecodetry)
        my_scene5.screen.move_to(pos)
        my_scene5.updates()
        cp.move_to(my_scene5.b_center)
        sp.move_to(my_scene5.s_center)
        self.play(
            ReplacementTransform(my_scene4.screen, my_scene5.screen),
            FadeTransform(my_scene4.code, my_scene5.code, stretch=False),
            cg.animate.move_to(my_scene5.b_center + LEFT).set_opacity(1),
            FadeIn(sg.move_to(my_scene5.b_center + RIGHT)
                .set_opacity(1).set_color(YELLOW))
        )
        self.wait()
        s1 = SurroundingRectangle(my_scene5.code[2][5][12:-4], buff=0.05, stroke_width=2)
        s2 = SurroundingRectangle(my_scene5.code[2][7][12:-1], buff=0.05, stroke_width=2)
        s3 = SurroundingRectangle(my_scene5.code[2][11][12:-4], buff=0.05, stroke_width=2)
        self.play(AnimationGroup(*[Create(i) for i in [s1, s2, s3]], lag_ratio=1))
        self.wait()
        self.play(FadeOut(s1, s2, s3))
        scenecode5 = '''from manim import *
class Try(Scene):
    def construct(self):
        c = Circle(fill_opacity=1)
        s = Square(color=YELLOW, fill_opacity=1)
        self.play(FadeIn(c))
        self.wait()
        self.play(ReplacementTransform(
            c, s, run_time=3
        ))
        self.wait()
        self.play(FadeOut(s))
        self.wait()'''
        my_scene6 = CodeScene(code=scenecode5)
        my_scene6.screen.move_to(pos)
        my_scene6.updates()
        self.play(Write(my_scene6.code[2][8][-12:].set_color(YELLOW)))
        cp.move_to(my_scene6.s_center).set_opacity(1)
        sp.move_to(my_scene6.s_center).set_color(YELLOW).set_opacity(1)
        self.wait()
        self.play(FadeIn(cp))
        self.wait()
        cpp = cp.copy()
        spp = sp.copy()
        self.play(ReplacementTransform(
            cp, sp, run_time=3
        ))
        self.wait()
        self.play(FadeOut(sp))
        scenecode6 = '''from manim import *
class Try(Scene):
    def construct(self):
        c = Circle(fill_opacity=1)
        s = Square(color=YELLOW, fill_opacity=1)
        self.play(FadeIn(c))
        self.wait()
        self.play(Transform(
            c, s, rate_func=there_and_back
        ))
        self.wait()
        self.play(FadeOut(c))
        self.wait()'''
        my_scene7 = CodeScene(code=scenecode6)
        my_scene7.screen.move_to(pos)
        my_scene7.updates()
        self.play(Unwrite(my_scene6.code[2][8][-10:]))
        self.play(
            Write(my_scene7.code[2][8][-24:].set_color(YELLOW)),
            ReplacementTransform(my_scene5.code[2][7][-21:], 
                                 my_scene7.code[2][7][-10:].set_color(YELLOW)),
            ReplacementTransform(my_scene5.code[2][-2][-3], 
                                 my_scene7.code[2][-2][-3].set_color(YELLOW))
        )
        self.wait()
        self.play(FadeIn(cpp))
        self.wait()
        self.play(Transform(cpp, spp, rate_func=there_and_back))
        self.wait()
        self.play(FadeOut(cpp))
        self.wait()
        self.play(FadeOut(*self.mobjects))

class Mobs(Scene):
    def construct(self):
        vt = ValueTracker(0)
        l = Line(LEFT, RIGHT, path_arc=0)
        arcCode = Text("Line(LEFT, RIGHT, path_arc=0)", font="Courier New").scale(0.5).shift(UP*2)
        aleft = arcCode.get_left()
        self.add(vt)
        self.play(Write(arcCode), Create(l))
        self.wait()
        arcCode.add_updater(lambda mob: mob.become(
                                Text(f"Line(LEFT, RIGHT, path_arc={round(vt.get_value(), 2)})",
                                      font="Courier New"
                            ).scale(0.5).move_to(aleft, aligned_edge=LEFT)))
        l.add_updater(lambda mob: mob.set_path_arc(vt.get_value()))
        self.play(vt.animate(rate_func=there_and_back, run_time=3).set_value(1.5*PI))
        self.wait()
        t = Text("蓝色，红色，黄色", t2c={"蓝色": BLUE, "红色": RED, "黄色": YELLOW})
        tCode = Text("Text(\"蓝色，红色，黄色\", "
                     "t2c={\"蓝色\": BLUE, \"红色\": RED, \"黄色\": YELLOW})", font="Courier New") \
                     .scale(0.5).shift(2*UP)
        l.clear_updaters()
        arcCode.clear_updaters()
        self.play(FadeOut(l, arcCode, vt))
        self.play(Write(tCode))
        self.play(Write(t))
        self.wait()
        self.play(FadeOut(tCode, t))
        curve = ParametricFunction(
            lambda t: (np.sin(2 * t), np.sin(3 * t), 0), t_range=[0, TAU])
        cCode = Text("ParametricFunction(\n"
                     "\tlambda t: (np.sin(2 * t), np.sin(3 * t), 0), t_range=[0, TAU])", 
                     font="Courier New").scale(0.5).shift(2*UP)
        self.play(Write(cCode))
        self.play(Create(curve))
        self.wait()
        self.play(FadeOut(cCode, curve))
        c1 = Circle(color=ORANGE)
        c2 = Circle().shift(RIGHT)
        c3 = Circle().scale(2)
        ciCode = Text("c1 = Circle(color=ORANGE)\n"
        "c2 = Circle().shift(RIGHT)\n"
        "c3 = Circle().scale(2)", font="Courier New").scale(0.5).shift(3*UP)
        self.play(Write(ciCode))
        self.play(AnimationGroup(*[Create(i) for i in [c1, c2, c3]], lag_ratio=1))
        self.wait()


class Try(Scene):
    def construct(self):
        scenecode = '''from manim import *
class Try(Scene):
    def construct(self):
        c = Circle()
        s = Square().next_to(c)
        self.add(c, s)
        self.remove(c)'''
        my_scene = CodeScene(code=scenecode)
        self.add(my_scene, *[index_labels(my_scene.code[2][t]) for t in range(0, 7)])
