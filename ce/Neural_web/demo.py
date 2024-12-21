from manim import *
from manim_ml.neural_network import *
from torchvision import datasets
from icecream import ic
import numpy as np
from utils import *

test_data = datasets.MNIST(root="./data/", train=False, download=True)
image = np.asarray(test_data[0][0])
some_data = [test_data[i] for i in range(20)]
images = [np.asarray(t[0]) for t in some_data]
signs = [t[1] for t in some_data]

class Demo(Scene):
    def construct(self):
        brain = SVGMobject("icons/brain.svg").scale(1.5)
        nn = NeuralNetwork([
            FeedForwardLayer(num_nodes=3),
            FeedForwardLayer(num_nodes=6),
            FeedForwardLayer(num_nodes=3)
        ], layer_spacing=1).scale(1.5)
        bulb = SVGMobject("icons/bulb.svg")
        self.play(Create(nn), run_time=2)
        self.wait()
        self.play(nn.animate.move_to(RIGHT * 3))
        self.play(Create(brain.move_to(LEFT * 3)))
        self.wait()
        self.play(FadeIn(bulb.move_to(UP * 2), scale=0.1), run_time=1)
        self.wait()
        self.play(FadeOut(bulb, brain), nn.animate.move_to(ORIGIN))
        self.wait()
        manim_image = ImageMesh(images, signs, 4, 5).scale(0.6).next_to(nn, LEFT)
        self.play(FadeIn(manim_image))
        self.play(*[Indicate(i, scale_factor=1.1) for i in manim_image.images])
        self.play(*[Indicate(i, scale_factor=1.2, color=ORANGE) for i in manim_image.signs])
        self.wait()
        self.play(FadeOut(manim_image, scale=0.1, shift=RIGHT * 2.5))
        self.wait()
        forward_pass = nn.make_forward_pass_animation(run_time=2)
        self.play(forward_pass)
        self.wait()

        one_image = ImageAndSign(images[0], signs[0]).scale(3)
        one_image.remove(one_image.sign).next_to(nn, LEFT)
        one_num = DecimalNumber(signs[0], num_decimal_places=0).scale(3).next_to(nn, RIGHT, buff=1.25)
        self.play(FadeIn(one_image))
        self.wait()
        self.play(FadeOut(one_image, scale=0.1, shift=RIGHT * 2.5))
        self.wait()
        self.play(forward_pass)
        self.wait()
        self.play(FadeIn(one_num, scale=0.1, shift=RIGHT * 2))
        self.play(Indicate(one_num))
        self.wait()
        self.play(FadeOut(one_num))

        nnbox = SurroundingRectangle(nn, color=YELLOW)
        nns = Group(nn, nnbox)
        self.play(Create(nnbox))
        self.wait()
        subset = MathTex(r"\subset").scale(2)
        mcl = Text("Machine Learning", t2c={
            "Machine": BLUE,
            "Learning": GREEN,
        }).next_to(subset, RIGHT)
        self.play(nns.animate.next_to(subset, LEFT))
        self.play(Write(subset))
        self.play(Write(mcl))
        self.wait()
        self.play(FadeOut(subset, mcl))

        self.wait()
        dpl = Text("Deep Learning", t2c={
            "Deep": YELLOW,
            "Learning": RED,
        }).move_to(UP * 1.5)
        self.play(nns.animate.next_to(dpl, DOWN))
        self.play(Write(dpl))
        self.wait()

        self.play(FadeOut(nns, dpl))
        self.wait()

class Demo2(Scene):
    def construct(self):
        mcl = Text(" Neural\nNetwork",t2c = {
            "Neural": BLUE,
            "Network": GREEN
        }, fill_opacity=0.5)
        dashedtext = DashedVMobject(SurroundingRectangle(mcl, buff=0.5))
        mcls = VGroup(mcl, dashedtext)
        arr = Arrow(ORIGIN, RIGHT*2, stroke_width=12, max_stroke_width_to_length_ratio=24, color=RED)
        mcls.next_to(arr, LEFT)
        bicycle = SVGMobject("icons/bicycle4.svg").scale(1.2).next_to(arr, RIGHT)
        self.play(Create(mcls))
        self.play(Create(arr))
        self.play(FadeIn(bicycle))
        self.wait()
        self.play(FadeOut(mcls, arr, bicycle))
        self.wait()

        # 2016年起
        timeline = Line(start=LEFT*6, end=RIGHT*6, stroke_width=2).shift(UP*3)
        time = DecimalNumber(2016, num_decimal_places=0).next_to(timeline, UP)
        self.play(FadeIn(timeline, time))
        self.wait()
        bicycles = [SVGMobject(f"icons/bicycle{i + 1}.svg").scale(0.5) for i in range(4)]
        poses = [[1.3, 2, 0], [1.5, 1.4, 0], [-1.6, 2.4, 0], [-1.2, -3.3, 0], 
                 [4.7, 1.1, 0], [3.6, 2.7, 0], [-5.2, 2.4, 0], [3.1, 0.4, 0], 
                 [6.2, -2.7, 0], [6.7, 2.1, 0], [-1.2, 1.5, 0], [-5.2, -2.2, 0],
                 [-4.6, -1, 0], [-2.4, -0.7, 0], [-6.2, 0.8, 0], [3, 1.5, 0],
                 [1.5, -2.2, 0], [5.7, 1.5, 0], [7.9, 1.2, 0], [-4, 0.5, 0],
                 [5, 2.5, 0], [3, -0.7, 0], [-2, -2.5, 0], [2, 0.5, 0]
                ]
        signs = [0, 1, 3, 0, 
                 2, 2, 1, 0, 
                 3, 1, 1, 3,
                 0, 1, 2, 3,
                 3, 3, 0, 2,
                 0, 3, 1, 2
                ]
        for i in range(8):
            self.add(bicycles[signs[i * 3]].copy().move_to(poses[i * 3]))
            self.wait(0.2)
            self.add(bicycles[signs[i * 3 + 1]].copy().move_to(poses[i * 3 + 1]))
            self.wait(0.2)
            self.add(bicycles[signs[i * 3 + 2]].copy().move_to(poses[i * 3 + 2]))
            self.wait(0.2)
            time.set_value(2016 + i + 1)
            self.wait(0.2)
        self.wait()
        maxrec = Rectangle(width=7, height=2.8, color=YELLOW).move_to(ORIGIN, aligned_edge=DL)
        minrec = Rectangle(width=7, height=2.8, color=ORANGE).move_to(DOWN * 0.3, aligned_edge=UL)
        self.play(Create(maxrec), Create(minrec))
        duo = Text("多", color=YELLOW).scale(2).next_to(maxrec, LEFT)
        shao = Text("少", color=ORANGE).scale(2).next_to(minrec, LEFT)
        self.play(Write(duo), Write(shao))
        self.wait()
        self.play(FadeOut(duo, shao, maxrec, minrec, time, timeline))
        self.wait()
        self.play(*[UpdateFromAlphaFunc(mob, get_spiral_out(mob, PI * mob.get_center()[1])) for mob in self.mobjects])
        self.remove(*self.mobjects)

        exp = ExpMachine().scale(0.8)
        self.play(FadeIn(exp, scale=0.1))
        self.wait()
        indata = Text("(2024, 12, 31)\nCentral Street", 
                      font="Consolas", color=RED,
                      line_spacing=1).scale(0.8).next_to(exp, LEFT)
        outdata = Text("35", color=GREEN, font="Consolas").scale(2).next_to(exp, RIGHT, buff=1.6)
        self.play(FadeIn(indata, shift=RIGHT*1.5))
        self.play(FadeOut(indata, shift=RIGHT*2))
        self.play(FadeIn(outdata, shift=RIGHT*2))
        self.play(FadeOut(outdata, shift=RIGHT*2))
        indata2 = Text("(2025, 6, 1)\nKindergarten",
                       font="Consolas", color=RED,
                       line_spacing=1).scale(0.8).next_to(exp, LEFT)
        outdata2 = Text("98", color=GREEN, font="Consolas").scale(2).next_to(exp, RIGHT, buff=1.6)
        self.wait()
        self.play(FadeIn(indata2, shift=RIGHT*1.5))
        self.play(FadeOut(indata2, shift=RIGHT*2))
        self.play(FadeIn(outdata2, shift=RIGHT*2))
        self.play(FadeOut(outdata2, shift=RIGHT*2))
        self.wait()
        self.play(FadeOut(exp))
        self.wait()
        
from math import exp

class Demo3(Scene):
    def construct(self):
        ax = Axes(x_range=[-3, 4], y_range=[-1, 10], x_length=10.5, y_length=5.5, color=WHITE).shift(LEFT * 1.5)
        ex = ax.plot(exp, color=BLUE)
        taylor = MathTex(r"e^x \approx 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots",
                         tex_to_color_map={
                             r"e^x": BLUE,
                             r" \approx": WHITE,
                             r"1 ": GREEN,
                             r"+ x ": GREEN,
                             r"+ \frac{x^2}{2!} ": GREEN,
                             r"+ \frac{x^3}{3!} ": GREEN,
                             r"+ \cdots": GREEN,
                         }).shift(UP * 1.5 + RIGHT * 2.5)
        surec = SurroundingRectangle(taylor, color=BLACK, fill_opacity=0.7, stroke_opacity=0)
        self.wait()
        self.play(FadeIn(ax, ex, surec, taylor[0: 2]))
        self.wait()
        tc1 = ax.plot(lambda x: 1 + x, color=GREEN)
        self.play(Create(tc1), FadeIn(taylor[2: 5]))
        def sc_func(func):
            self.bring_to_back(tc1)
        self.add_updater(sc_func)
        self.wait()
        tc2 = ax.plot(lambda x: 1 + x + x**2/2, color=GREEN)
        self.play(tc1.animate.become(tc2), FadeIn(taylor[5]))
        self.wait()
        tc3 = ax.plot(lambda x: 1 + x + x**2/2 + x**3/6, color=GREEN)
        self.play(tc1.animate.become(tc3), FadeIn(taylor[6]))
        self.wait()
        self.play(tc1.animate.become(ex.copy().set_color(GREEN)), FadeIn(taylor[7]))
        self.wait(2)
        self.remove_updater(sc_func)
        self.play(FadeOut(tc1, ex, surec, ax), taylor.animate.center())
        self.wait()

        addfunc = MathTex(r"f(x) \approx a_1f_1(x) + a_2f_2(x) + a_3f_3(x) + \cdots",
                          tex_to_color_map={
                              r"f(x) ": BLUE,
                              r"\approx ": WHITE,
                              r"+ ": WHITE,
                              r"a_1": RED,
                              r"f_1(x) ": GREEN,
                              r"a_2": RED,
                              r"f_2(x) ": GREEN,
                              r"a_3": RED,
                              r"f_3(x) ": GREEN,
                              r"\cdots": GREEN,
                          })
        self.play(taylor.animate.shift(UP * 0.7), FadeIn(addfunc.shift(DOWN * 0.7)))
        self.wait()
        self.play(FadeOut(taylor), addfunc.animate.shift(DOWN * 1.5))
        nn = NN().shift(DOWN)
        self.play(Create(nn))
        self.play(addfunc[0].animate.move_to(nn.lastcircle),
                  addfunc[3].animate.move_to(nn.circles1[0]),
                  addfunc[6].animate.move_to(nn.circles1[1]),
                  addfunc[9].animate.move_to(nn.circles1[2]),
                  addfunc[2].animate.move_to(nn.lines[0]),
                  addfunc[5].animate.move_to(nn.lines[1]),
                  addfunc[8].animate.move_to(nn.lines[2]),
                  FadeOut(addfunc[1: 11: 3], addfunc[11]))
        self.wait()
        self.play(*[Indicate(addfunc[i]) for i in [3, 6, 9]])
        self.play(*[Indicate(addfunc[i]) for i in [2, 5, 8]])
        self.wait()
        self.play(Indicate(addfunc[0]))
        self.wait(2)

        self.play(FadeOut(*[i for i in nn if i is not nn.circles1[0]], *[addfunc[i] for i in [0, 6, 9, 2, 5, 8]]))
        neural = VGroup(nn.circles1[0], addfunc[3])
        eq = MathTex(r"=").next_to(neural, RIGHT)
        what = MathTex(r"?", color=YELLOW).next_to(eq, RIGHT)
        Vg = VGroup(neural.copy(), eq, what).arrange(RIGHT).center()
        self.play(neural.animate.move_to(Vg[0]))
        self.wait()
        self.play(Write(eq), Write(what))
        self.wait()
        

class Demo4(Scene):
    def construct(self):
        circle1 = Circle(color=YELLOW, radius=0.6)
        firstfunc = MathTex(r"f_1(x)", color=GREEN).move_to(circle1)
        neural = VGroup(circle1, firstfunc)
        eq = MathTex(r"=")
        what = MathTex(r"?", color=YELLOW)
        Vg = VGroup(neural, eq, what).arrange(RIGHT).center()
        self.add(Vg)
        self.wait()
        sig = MathTex(r"1\over1+e^{-x-a}", tex_to_color_map={
            r"1\over1+e^{-x-": YELLOW,
            r"a": RED,
        }).next_to(eq, RIGHT)
        self.play(FadeTransform(what, sig))
        self.wait()
        Vg.remove(what).add(sig)
        self.play(Vg.animate.to_corner(UL))
        ax = Axes(x_range=[-10, 10], y_range=[0, 2], x_length=8, y_length=3, color=WHITE) \
            .shift(DOWN)
        aeq = MathTex(r"a=", tex_to_color_map={r"a": RED}).scale(1.2)
        anum = DecimalNumber(0, num_decimal_places=2).scale(1.2).next_to(aeq, RIGHT)
        aeqnum = VGroup(aeq, anum).to_corner(UR, buff=1)
        self.play(Create(ax))
        siggraph = ax.plot(lambda x: 1/(1+exp(-x)), color=GREEN)
        self.play(Write(aeqnum), Create(siggraph))
        self.wait()
        zeroyu = Rectangle(width=(ax.c2p(-3, 0) - ax.c2p(-10, 0))[0],
                           height=ax.y_length/4, color=YELLOW, fill_opacity=0.3, stroke_opacity=0) \
                           .move_to(ax.c2p(-10, 0), aligned_edge=LEFT)
        oneyu = zeroyu.copy().move_to(ax.c2p(10, 1), aligned_edge=RIGHT)
        self.play(FadeIn(zeroyu))
        self.play(FadeOut(zeroyu))
        self.wait()
        self.play(FadeIn(oneyu))
        self.play(FadeOut(oneyu))
        self.wait()

        Sax = MathTex(r"S_{{a}}(x)={1\over1+e^{-x-a}}",
                      tex_to_color_map={
                          r"S_": GREEN,
                          r"(x)": GREEN,
                          r"a": RED,
                          r"1\over1+e^{-x-": YELLOW
                      }).to_corner(UL)
        nn = OnlyOneNN().scale(0.7)
        x = MathTex("x").scale_to_fit_width(0.6*0.5)
        Sa = MathTex("S_a", tex_to_color_map={"S_": GREEN, "a": RED}).scale_to_fit_width(0.6*0.7)
        y = MathTex("y").scale_to_fit_width(0.6*0.5)
        omega1 = MathTex("\\omega_1", color=RED).scale_to_fit_width(0.6*0.7)
        omega2 = MathTex("\\omega_2", color=RED).scale_to_fit_width(0.6*0.7)
        x.move_to(nn.circles[2])
        y.move_to(nn.circles[0])
        Sa.move_to(nn.circles[1])
        omega1.next_to(nn.lines[1], LEFT)
        omega2.next_to(nn.lines[0], LEFT)
        nngroup = VGroup(nn, x, Sa, y, omega1, omega2).to_corner(DL, buff=1)
        self.play(FadeIn(nngroup))
        self.wait()
        self.play(FadeTransform(neural, Sax[0: 3]),
                  FadeTransform(eq, Sax[3]),
                  FadeTransform(sig, Sax[4:]))
        yx = MathTex(r"y=\omega_2S_a(\omega_1x)",
                     tex_to_color_map={
                          r"y": GREEN,
                          r"\omega_2": RED,
                          r"a": RED,
                          r"\omega_1": RED,
                          r"S_": YELLOW,
                          r"(": YELLOW,
                          r"x)": YELLOW,
                     }).next_to(Sax, DOWN, buff=0.5)
        yx.shift((Sax[3].get_x() - yx[1].get_x())*RIGHT)
        omega1eq = MathTex(r"\omega_1=", tex_to_color_map={r"\omega_1": RED}).scale(1.2)
        omega2eq = MathTex(r"\omega_2=", tex_to_color_map={r"\omega_2": RED}).scale(1.2)
        omega1num = DecimalNumber(1, num_decimal_places=2).scale(1.2).next_to(omega1eq, RIGHT)
        omega2num = DecimalNumber(1, num_decimal_places=2).scale(1.2).next_to(omega2eq, RIGHT)
        omega1eqnum = VGroup(omega1eq, omega1num).next_to(aeqnum, DOWN, buff=0.5)
        omega2eqnum = VGroup(omega2eq, omega2num).next_to(omega1eqnum, DOWN, buff=0.5)
        omega1eqnum.shift((aeqnum[1].get_x() - omega1eqnum[1].get_x())*RIGHT)
        omega2eqnum.shift((omega1eqnum.get_x() - omega2eqnum.get_x())*RIGHT)
        self.play(*[Write(i) for i in [yx, omega1eqnum, omega2eqnum]])
        self.wait()

        atracker = ValueTracker(0)
        omega1tracker = ValueTracker(1)
        omega2tracker = ValueTracker(1)
        def sigfunc(a, o1, o2):
            def func(x):
                return o2/(1+exp(-o1*x-a))
            return func
        siggraph.add_updater(lambda m: m.become(
            ax.plot(sigfunc(
                atracker.get_value(), 
                omega1tracker.get_value(), 
                omega2tracker.get_value()), color=GREEN
                )))
        anum.add_updater(lambda m: m.set_value(atracker.get_value()))
        omega1num.add_updater(lambda m: m.set_value(omega1tracker.get_value()))
        omega2num.add_updater(lambda m: m.set_value(omega2tracker.get_value()))
        self.add(atracker, omega1tracker, omega2tracker)
        self.play(atracker.animate.set_value(4))
        self.play(atracker.animate.set_value(-4))
        self.play(atracker.animate.set_value(0))
        self.wait()
        self.play(omega1tracker.animate.set_value(3))
        self.play(omega1tracker.animate.set_value(-1))
        self.play(omega1tracker.animate.set_value(1))
        self.wait()
        self.play(omega2tracker.animate.set_value(3))
        self.play(omega2tracker.animate.set_value(-1))
        self.play(omega2tracker.animate.set_value(1))
        self.wait(3)
        mobs = [i for i in self.mobjects if i not in [nngroup, siggraph]]
        self.play(FadeOut(*mobs), Uncreate(siggraph))
        self.wait()

        self.play(nngroup.animate.center())
        self.wait()
        nnn = NeuralNetwork([
            FeedForwardLayer(num_nodes=1, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
            FeedForwardLayer(num_nodes=5, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
            FeedForwardLayer(num_nodes=1, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
        ], layer_spacing=0.7).rotate(PI/2)
        
        self.play(FadeOut(nngroup), FadeIn(nnn))
        self.wait()

        anims = nnn.make_forward_pass_animation()
        self.play(anims.animations[2], run_time=2)
        self.wait()
        nnn2 = NeuralNetwork([
            FeedForwardLayer(num_nodes=1, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
            FeedForwardLayer(num_nodes=5, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
            FeedForwardLayer(num_nodes=5, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
            FeedForwardLayer(num_nodes=1, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
        ], layer_spacing=0.7).rotate(PI/2)
        self.play(ReplacementTransform(nnn, nnn2))
        self.wait()
        anims2 = nnn2.make_forward_pass_animation()
        self.play(anims2.animations[4], run_time=2)
        self.wait()
        self.play(anims2.animations[2], run_time=2)
        self.play(anims2.animations[3], run_time=2)
        self.wait()


class Demo5(Scene):
    def construct(self):
        nnn2 = NeuralNetwork([
            FeedForwardLayer(num_nodes=1, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
            FeedForwardLayer(num_nodes=5, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
            FeedForwardLayer(num_nodes=5, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
            FeedForwardLayer(num_nodes=1, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
        ], layer_spacing=0.7).rotate(PI/2)
        self.add(nnn2)
        aeq = MathTex(r"a", color=RED)
        what = MathTex(r"=\;?", tex_to_color_map={
            r"?": YELLOW,
        }).next_to(aeq, RIGHT).shift(0.05*UP)
        omegaeq = MathTex(r"\omega", color=RED)
        what2 = what.copy().next_to(omegaeq, RIGHT).shift(0.05*UP)
        omegas = VGroup(omegaeq, what2).scale(1.2)
        aas = VGroup(aeq, what).scale(1.2)
        aas.to_corner(UL, buff=1.5)
        omegas.next_to(aas, DOWN, buff=0.5)
        self.wait()
        self.play(Write(aas), Write(omegas))
        self.wait(1)
        tb = MathTable(
            [[r"a", 0.35, 0.12, -0.88, r"\cdots"], 
             [r"\omega", -0.78, -0.04, 0.61, r"\cdots"]],
             include_outer_lines=True).scale(0.8).shift(DOWN*2)
        tb.get_entries((1, 1)).scale(1.2*1.25).set_color(RED)
        tb.get_entries((2, 1)).scale(1.2*1.25).set_color(RED)
        tbc = tb.copy()
        tbc.get_entries((1, 1)).set_opacity(0)
        tbc.get_entries((2, 1)).set_opacity(0)
        self.play(nnn2.animate.rotate(-PI/2).shift(UP*1.5).scale(0.7),
                  FadeOut(what, what2))
        self.play(Create(tbc),
                  ReplacementTransform(aeq, tb.get_entries((1, 1))),
                  ReplacementTransform(omegaeq, tb.get_entries((2, 1))))
        self.remove(tbc)
        self.add(tb)
        self.wait()
        anims = nnn2.make_forward_pass_animation()
        atracker1 = ValueTracker(0.35)
        atracker2 = ValueTracker(0.12)
        atracker3 = ValueTracker(-0.88)
        atrackers = [atracker1, atracker2, atracker3]
        otracker1 = ValueTracker(-0.78)
        otracker2 = ValueTracker(-0.04)
        otracker3 = ValueTracker(0.61)
        otrackers = [otracker1, otracker2, otracker3]
        self.add(atracker1, atracker2, atracker3, otracker1, otracker2, otracker3)
        for i in range(3):
            tb.get_entries((1, i+2)).add_updater(lambda m, i=i: m.become(MathTex(f"{round(atrackers[i].get_value(), 2)}").scale_to_fit_height(m.get_height()).move_to(m)))
            tb.get_entries((2, i+2)).add_updater(lambda m, i=i: m.become(MathTex(f"{round(otrackers[i].get_value(), 2)}").scale_to_fit_height(m.get_height()).move_to(m)))
        self.play(anims, run_time=2)
        arr = Vector(LEFT*4, color=BLUE).next_to(nnn2, DOWN)
        self.play(GrowArrow(arr))
        self.play(FadeOut(arr, shift=2*LEFT, scale=0.1))
        self.play(atracker1.animate.set_value(0.51),
                  atracker2.animate.set_value(0.22),
                  atracker3.animate.set_value(-0.45),
                  otracker1.animate.set_value(-0.63),
                  otracker2.animate.set_value(-0.11),
                  otracker3.animate.set_value(0.36),
                  )
        self.wait()

        self.play(anims, run_time=2)
        arr = Vector(LEFT*4, color=BLUE).next_to(nnn2, DOWN)
        self.play(GrowArrow(arr))
        self.play(FadeOut(arr, shift=2*LEFT, scale=0.1))
        self.play(atracker1.animate.set_value(0.64),
                  atracker2.animate.set_value(0.27),
                  atracker3.animate.set_value(-0.49),
                  otracker1.animate.set_value(-0.69),
                  otracker2.animate.set_value(0.12),
                  otracker3.animate.set_value(0.31),
                  )
        self.wait(2)

        self.play(nnn2.animate.shift(LEFT*2))
        anims = nnn2.make_forward_pass_animation()
        inputnum = DecimalNumber(2, color=GREEN).scale(1.2).next_to(nnn2, LEFT)
        outnum = DecimalNumber(30.5, color=BLUE).scale(1.2).next_to(nnn2, RIGHT)
        self.play(FadeIn(inputnum, shift=RIGHT))
        self.play(FadeOut(inputnum, shift=RIGHT))
        self.play(anims, run_time=2)
        self.play(FadeIn(outnum, shift=RIGHT))
        self.wait()
        expect = Text("Expected output:", font_size=30)
        loss = Text("Loss:", font_size=30)
        epnum = DecimalNumber(11, color=BLUE).scale(1.2)
        lsnum = DecimalNumber(19.50, color=YELLOW).scale(1.2)
        expect.to_corner(UR, buff=1).shift(LEFT)
        loss.next_to(expect, DOWN, buff=0.5, aligned_edge=RIGHT)
        epnum.next_to(expect, RIGHT)
        lsnum.next_to(loss, RIGHT)
        self.play(Write(expect), Write(loss), run_time=1)
        self.play(FadeIn(epnum))
        self.play(FadeIn(lsnum))
        self.wait()

        arr.shift(LEFT*2)
        self.play(GrowArrow(arr), FadeOut(outnum, shift=LEFT), FadeOut(epnum, lsnum))
        self.play(FadeOut(arr, shift=2*LEFT, scale=0.1))
        self.play(atracker1.animate.set_value(0.56),
                  atracker2.animate.set_value(0.29),
                  atracker3.animate.set_value(-0.55),
                  otracker1.animate.set_value(-0.69),
                  otracker2.animate.set_value(0.32),
                  otracker3.animate.set_value(0.41),
                  )
        self.wait(2)

        inputnum.set_value(8)
        outnum.set_value(77.2)
        epnum.set_value(70)
        lsnum.set_value(7.2)
        self.play(FadeIn(inputnum))
        self.play(FadeOut(inputnum, shift=RIGHT))
        self.play(anims, run_time=2)
        self.play(FadeIn(outnum, shift=RIGHT))
        self.play(FadeIn(epnum, lsnum))
        self.play(GrowArrow(arr), FadeOut(outnum, shift=LEFT), FadeOut(epnum, lsnum))
        self.play(FadeOut(arr, shift=2*LEFT, scale=0.1))
        self.play(atracker1.animate.set_value(0.59),
                  atracker2.animate.set_value(0.24),
                  atracker3.animate.set_value(-0.50),
                  otracker1.animate.set_value(-0.61),
                  otracker2.animate.set_value(0.39),
                  otracker3.animate.set_value(0.46),
                  )
        self.wait()

        inputnum.set_value(11).next_to(nnn2, LEFT)
        outnum.set_value(45.5)
        epnum.set_value(45)
        lsnum.set_value(0.5)
        self.play(FadeIn(inputnum))
        self.play(FadeOut(inputnum, shift=RIGHT))
        self.play(anims, run_time=2)
        self.play(FadeIn(outnum, shift=RIGHT))
        self.play(FadeIn(epnum, lsnum))
        self.play(GrowArrow(arr), FadeOut(outnum, shift=LEFT), FadeOut(epnum, lsnum))
        self.play(FadeOut(arr, shift=2*LEFT, scale=0.1))
        self.play(atracker1.animate.set_value(0.55),
                  atracker2.animate.set_value(0.23),
                  atracker3.animate.set_value(-0.49),
                  otracker1.animate.set_value(-0.58),
                  otracker2.animate.set_value(0.31),
                  otracker3.animate.set_value(0.42),
                  )
        self.wait()

        inputnum.set_value(20).next_to(nnn2, LEFT)
        outnum.set_value(71.9)
        epnum.set_value(72)
        lsnum.set_value(0.1)
        self.play(FadeIn(inputnum))
        self.play(FadeOut(inputnum, shift=RIGHT))
        self.play(anims, run_time=2)
        self.play(FadeIn(outnum, shift=RIGHT))
        self.play(FadeIn(epnum, lsnum))
        rec = SurroundingRectangle(lsnum, color=RED)
        self.play(Create(rec))
        self.wait()
        self.play(Uncreate(rec))
        rec2 = SurroundingRectangle(tb, color=RED)
        self.play(Create(rec2))
        self.wait()
        self.play(Uncreate(rec2))
        self.wait(2)


class Demo6(Scene):
    def construct(self):
        date = Text("2022-01-01", font_size=60, font="Consolas", t2c={
            "2022": BLUE,
            "01": GREEN,
            "01": GREEN
        })
        bike = SVGMobject("icons/bicycle1.svg")
        vec = Vector([2, 0, 0], stroke_width=8)
        VGroup(date, vec, bike).arrange(RIGHT).center()
        self.play(AnimationGroup(Write(date, run_time=0.5), Create(vec, run_time=0.5), FadeIn(bike, run_time=0.5), lag_ratio=0.5, run_time=1.5))
        no = MathTex(r"\times", color=RED, font_size=150).move_to(vec)
        self.play(FadeIn(no, run_time=0.5))
        self.wait()
        self.play(FadeOut(no, date, vec, bike))
        self.wait()

        rec1 = Rectangle(width=4, height=4, color=RED)
        rec2 = rec1.copy().set_color(GREEN)
        VGroup(rec1, rec2).arrange(RIGHT, buff=2).shift(0.5*UP)
        nnn1 = NeuralNetwork([
            FeedForwardLayer(num_nodes=1, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
            FeedForwardLayer(num_nodes=5, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
            FeedForwardLayer(num_nodes=5, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
            FeedForwardLayer(num_nodes=1, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
        ], layer_spacing=0.7).rotate(PI/2).scale_to_fit_height(3.5).move_to(rec1)
        nnn2 = NeuralNetwork([
            FeedForwardLayer(num_nodes=4, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
            FeedForwardLayer(num_nodes=5, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
            FeedForwardLayer(num_nodes=5, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
            FeedForwardLayer(num_nodes=1, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
        ], layer_spacing=0.7).rotate(PI/2).scale_to_fit_height(3.5).move_to(rec2)
        old = Text("Old Model", color=RED, font="Consolas").next_to(rec1, DOWN)
        better = Text("Better Model", color=GREEN, font="Consolas").next_to(rec2, DOWN)
        self.play(FadeIn(nnn1, rec1, run_time=0.5))
        self.play(Write(old, run_time=0.5))
        self.wait(0.5)
        self.play(FadeIn(nnn2, rec2, run_time=0.5))
        self.play(Write(better, run_time=0.5))
        self.wait(2)
        self.play(FadeOut(nnn1, rec1, old, nnn2, rec2, better))
        self.wait()


from manim_ml.neural_network.activation_functions.sigmoid import SigmoidFunction
class Title(Scene):
    def construct(self):
        title = Text("走进Ai之神经网络", t2c={
            "走进Ai": YELLOW,
            "神经网络": GREEN,
        }).scale(1.5)
        title[0: 2].align_to(title[6], UP)
        nnn1 = NeuralNetwork([
            FeedForwardLayer(num_nodes=1, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
            FeedForwardLayer(num_nodes=5, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
            FeedForwardLayer(num_nodes=5, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
            FeedForwardLayer(num_nodes=1, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
        ], layer_spacing=0.7).rotate(-PI/3).scale_to_fit_height(2)
        bike = SVGMobject("icons/bicycle2.svg").scale(0.7).rotate(-0.6)
        self.add(title, nnn1.move_to(DOWN*2 + LEFT*5), bike.move_to(RIGHT*5 + UP*3))
        sig = SigmoidFunction(function_name="").scale(3.5).to_corner(DR).rotate(0.5)
        vecs = VGroup(Vector([-2, 0, 0], color=RED, stroke_width=8), Vector([2, 0, 0], color=GREEN, stroke_width=8)).arrange(DOWN).to_corner(UL, buff=1).rotate(0.3)
        self.add(sig, vecs)


class Thanks(Scene):
    def construct(self):
        text = Text("特别鸣谢", font_size=72).to_edge(UP, buff=1.5)
        animauthor = Text("动画制作：梵hxj", font_size=36)
        shulai = Text("数据来源：集智俱乐部", font_size=36)
        vg = VGroup(text, animauthor, shulai)
        VGroup(animauthor, shulai).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        vg.shift(DOWN*0.5)
        self.add(vg)