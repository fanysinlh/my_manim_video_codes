from manimlib import *
from random import random, seed

class RedBagRain(Scene):
    def construct(self):
        seed(1737517807.018937)
        PMNUM = 10
        RBNUM = 200
        pm = ImageMobject("./assets/paimeng.png").scale(0.5)
        red_bag = Rectangle(color=RED, fill_opacity=1, stroke_color=WHITE).scale(0.3).rotate(70*DEGREES)
        width, height = FRAME_WIDTH, FRAME_HEIGHT
        pmrd = [((random() - 0.5)*(width - pm.get_width()), (random() - 0.5)*(height - pm.get_height()), 0) for _ in range(PMNUM)]
        pms = Group(*[pm.copy().move_to(pmrd[i]) for i in range(PMNUM)])
        rbrd = [(random()*width*2 - width/2, random()*height*2 + height/2 + 1, 0) for _ in range(RBNUM)]
        rbs = Group(*[red_bag.copy().move_to(rbrd[i]) for i in range(RBNUM)])
        self.add(rbs)
        rbs.add_updater(lambda mob, dt: mob.shift(1.3*dt*(LEFT*np.cos(70*DEGREES) + DOWN*np.sin(70*DEGREES))))
        for i in pms:
            self.play(FadeInFromPoint(i, i.get_center()))
        self.wait(1)
        self.play(FadeOut(rbs))
        self.play(*[FadeOut(pms[i]) for i in range(2, PMNUM)])
        self.wait()
        yue = Tex(r"\mathbf{\approx}", font_size=144)
        ag = Group(pms[0].copy().scale(2), yue, pms[1].copy().scale(2)).arrange(RIGHT).center()
        self.play(pms[0].animate.scale(2).move_to(ag[0]), pms[1].animate.scale(2).move_to(ag[2]))
        self.play(FadeIn(yue))
        self.wait()
        s = ScreenRectangle(height=FRAME_HEIGHT + 0.05, stroke_color=WHITE)
        self.add(s)
        self.play(self.frame.animate.shift(UP*0.5).scale(1.4))
        self.play(FadeOut(yue), FadeOut(pms[1]), pms[0].animate.scale(0.5).next_to(s, UP, aligned_edge=LEFT, buff=-0.1))
        less7 = Tex(r"< \hspace{0.3em} 7", font_size=72, t2c={"<": YELLOW}).next_to(pms[0], RIGHT)
        pmsc = Group(*[pm.copy().move_to(pmrd[i]) for i in range(PMNUM)])
        self.play(AnimationGroup(*[FadeIn(pmsc[i]) for i in range(5)], lag_ratio=0.2), FadeIn(less7))
        self.wait()
        k = SurroundingRectangle(pmsc[0], color=YELLOW, buff=-0.1, stroke_width=8)
        self.play(ShowCreation(k))
        self.wait(0.5)
        self.play(Uncreate(k))
        more = Tex(">", font_size=72, t2c={">": YELLOW}).move_to(less7[0])
        self.play(AnimationGroup(*[FadeIn(pmsc[i]) for i in range(5, 10)], lag_ratio=0.2), FadeTransform(less7[0], more))
        self.wait()
        k2 = SurroundingRectangle(pmsc[9], color=YELLOW, buff=-0.1, stroke_width=8)
        self.play(ShowCreation(k2))
        self.wait(0.5)
        self.play(Uncreate(k2))
        self.wait()
        self.play(*[FadeOut(i) for i in self.mobjects])
        self.wait()


class GeneFunc(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 6, 1], x_axis_config={
            "include_numbers": True,
            "include_tip": True
        }, y_range=[0, 6, 7], y_axis_config={
            "include_tip": True
        })
        curve = ax.get_graph(lambda x: -(x - 2.5)**2 / 2 + 5, x_range=[0, 5, 0.01], color=BLUE)
        line1 = ax.get_v_line(ax.c2p(5, -2.5**2 / 2 + 5), color=GREEN)
        line2 = ax.get_v_line(ax.c2p(2.5, 5), color=GREEN)
        self.play(ShowCreation(ax, run_time=1))
        self.play(ShowCreation(curve, run_time=1))
        self.play(ShowCreation(line1, run_time=1), ShowCreation(line2, run_time=1))
        self.wait()
        high = Dot(ax.c2p(2.5, 5), fill_color=YELLOW)
        value = ValueTracker(5)
        lefthigh = 5 - 2.5**2 / 2
        curve.add_updater(lambda x: x.become(ax.get_graph(
            lambda x: -x*(x - 5)/2.5**2 * (value.get_value() - lefthigh) + lefthigh, 
            x_range=[0, 5, 0.01], 
            color=BLUE
        )))
        high.add_updater(lambda x: x.move_to(ax.c2p(2.5, value.get_value())))
        line2.add_updater(lambda x: x.become(ax.get_v_line(ax.c2p(2.5, value.get_value()), color=GREEN)))
        self.play(FadeIn(high))
        self.play(value.animate.set_value(6))
        self.play(value.animate.set_value(4))
        self.play(value.animate.set_value(5))
        self.wait()
        graph = ax.get_riemann_rectangles(curve, x_range=[0, 5], dx=0.01, colors=[YELLOW], stroke_width=0)
        self.play(FadeOut(line2), FadeOut(high))
        self.play(ShowCreation(graph))
        self.wait()
        def Shining(mob: Mobject, times, time):
            true_time = time/times/3
            for _ in range(times):
                self.wait(true_time)
                self.play(mob.animate.set_opacity(0), run_time=true_time)
                self.play(mob.animate.set_opacity(1), run_time=true_time)
        Shining(graph, 3, 3)
        self.wait()
        self.play(*[Uncreate(i) for i in self.mobjects])
        self.wait()

class GeneOther(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 6, 5], x_axis_config={
            "include_numbers": True,
            "include_tip": True,
        }, y_range=[0, 0.4, 0.2], y_axis_config={
            "include_tip": True,
            "unit_size": 8
        })
        curve = ax.get_graph(lambda x: 0.2, [0, 5, 1], color=BLUE)
        line1 = ax.get_v_line_to_graph(5, curve, color=GREEN)
        fifth = DecimalNumber(0.2, font_size=24, num_decimal_places=1).next_to(ax.c2p(0, 0.2), LEFT)
        self.play(ShowCreation(ax))
        self.play(ShowCreation(curve))
        self.play(ShowCreation(line1), ShowCreation(fifth))
        area = ax.get_riemann_rectangles(curve, [0, 5], 1, colors=[YELLOW], stroke_width=0)
        self.wait()
        self.play(FadeIn(area))
        self.wait()
        self.play(FadeOut(area))
        self.wait()
        self.play(*[Uncreate(i) for i in self.mobjects])


class GeneDx(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 6, 5], x_axis_config={
            "include_numbers": True,
            "include_tip": True,
        }, y_range=[0, 0.4, 0.2], y_axis_config={
            "include_tip": True,
            "unit_size": 8
        })
        curve = ax.get_graph(lambda x: 0.2, [0, 5, 1], color=BLUE)
        line1 = ax.get_v_line_to_graph(5, curve, color=GREEN)
        fifth = DecimalNumber(0.2, font_size=24, num_decimal_places=1).next_to(ax.c2p(0, 0.2), LEFT)
        self.add(ax, fifth, line1, curve)
        self.wait()
        line2 = ax.get_v_line_to_graph(1, curve, color=GREEN)
        self.play(ShowCreation(line2))
        self.wait()
        numtr = ValueTracker(1.7)
        under = ax.get_riemann_rectangles(curve, [1, 1.7], 0.01, colors=[YELLOW], stroke_width=0)
        twothere = VGroup(Dot(ax.c2p(1, 0)), Dot(ax.c2p(1.7, 0)))
        tx = Tex(r"\Delta x", t2c={r"\Delta x": RED}, font_size=24)
        brc = Brace(twothere, font_size=20, buff=0.01).put_at_tip(tx, buff=0.01)
        self.play(ShowCreation(under))
        self.play(Write(brc), Write(tx))
        self.wait()
        self.add(numtr)
        under.add_updater(lambda x: x.become(
            ax.get_riemann_rectangles(curve, [1, numtr.get_value()], 0.01, colors=[YELLOW], stroke_width=0)
        ))
        def twoupdater(mob: VGroup):
            mob[1].move_to(ax.c2p(numtr.get_value(), 0))
            return mob
        self.add(twothere.set_opacity(0))
        twothere.add_updater(twoupdater)
        brc.add_updater(lambda x: x.become(
            Brace(twothere, font_size=20, buff=0.01)
        ))
        def txupdater(mob: VMobject):
            brc.put_at_tip(mob, buff=0.01)
            return mob
        tx.add_updater(txupdater)
        self.play(numtr.animate.set_value(3))
        self.play(numtr.animate.set_value(1.2))
        self.wait()
        dx = Tex(r"dx", t2c={"dx": RED}, font_size=24)
        brc.put_at_tip(dx, buff=0.01)
        self.play(FadeTransform(tx, dx))
        self.wait()


class GeneChangeGraph(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 7, 1], x_axis_config={
            "include_tip": True,
        }, y_range=[0, 4, 1], y_axis_config={
            "include_tip": True,
        })
        curve = ax.get_graph(lambda x: 0.2, x_range=[0, 5, 1], color=BLUE)
        line = ax.get_v_line_to_graph(5, curve, color=GREEN)
        dot1 = Dot(ax.c2p(5, 0), fill_opacity=0)
        dot2 = Dot(ax.c2p(0, 0.2), fill_opacity=0)
        xlabel = Tex(r"\frac{2(10 - x)}{3}", font_size=24).next_to(dot1, DOWN, 0.05)
        ylabel = Tex(r"\frac{3}{2(10 - x)}", font_size=24).next_to(dot2, LEFT, 0.05)
        self.play(ShowCreation(ax))
        self.play(ShowCreation(curve))
        self.play(*[ShowCreation(i) for i in [line, xlabel, ylabel]])
        self.add(dot1, dot2)
        xeq = Tex("x=", t2c={"x=": RED}).to_corner(UL)
        num = DecimalNumber(number=2.5, color=YELLOW, font_size=32).next_to(xeq, RIGHT)
        self.wait()
        self.play(Write(VGroup(xeq, num)))
        self.wait()
        vt = ValueTracker(2.5)
        self.add(vt)
        num.add_updater(lambda x: x.set_value(vt.get_value()))
        curve.add_updater(lambda x: x.become(
            ax.get_graph(lambda x: 3/(2*(10 - vt.get_value())), [0, (2*(10 - vt.get_value()))/3, 0.01], color=BLUE)
        ))
        line.add_updater(lambda x: x.become(
            ax.get_v_line(ax.c2p(2*(10 - vt.get_value())/3, 3/(2*(10 - vt.get_value()))), color=GREEN)
        ))
        dot1.add_updater(lambda x: x.move_to(
            ax.c2p((2*(10 - vt.get_value()))/3, 0)
        ))
        dot2.add_updater(lambda x: x.move_to(
            ax.c2p(0, 3/(2*(10 - vt.get_value())))
        ))        
        xlabel.add_updater(lambda x: x.next_to(dot1, DOWN, 0.05))
        ylabel.add_updater(lambda x: x.next_to(dot2, LEFT, 0.05))
        self.play(vt.animate.set_value(5))
        self.play(vt.animate.set_value(0.01))
        self.play(vt.animate.set_value(2.5))
        self.wait()
        self.remove(vt, dot1, dot2)
        self.play(*[FadeOut(i) for i in [curve, line, xlabel, ylabel, xeq, num]])
        self.wait()
        color_nums = 10
        graphs = []
        for x in np.linspace(0, 5, color_nums + 1):
            nm = 2*(10 - x)/3
            curve = ax.get_graph(lambda x: 1/nm, [0, nm, 0.01])
            cl = interpolate_color(RED, GREEN, x / 5)
            gr = ax.get_riemann_rectangles(curve, [0, nm], 0.01, colors=[cl], stroke_width=0)
            graphs.append(gr)
        for i in range(color_nums):
            graphs[i + 1].next_to(graphs[i], UP, buff=0, aligned_edge=LEFT)
        for i in graphs:
            i.shift(8*UP)
            self.add(i)
            self.play(i.animate.shift(8*DOWN), run_time=0.3)
        this_one = VGroup(
            Arrow(graphs[5].get_corner(UR) + [2, 1, 0], graphs[5].get_corner(UR), buff=0.1),
            Tex(r"x = 2.5", t2c = {"x = 2.5": interpolate_color(RED, GREEN, 5 / color_nums)}).move_to(graphs[5].get_corner(UR) + [2, 1.3, 0])
        )
        self.play(FadeIn(this_one))
        self.wait()
        pos1 = graphs[5].get_corner(UR)
        pos2 = ax.c2p(ax.p2c(pos1)[0], 0)
        sr = Polygon(pos1, pos2, pos2 + LEFT*0.05, pos1 + LEFT*0.05)
        self.play(ShowCreationThenFadeOut(sr), run_time=2)
        self.wait()


class Sum1(Scene):
    def construct(self):
        xeq5 = Tex("x = 5")
        fruit1 = Tex(r"\frac{1}{5} \times dx \times \frac{3}{2(10 - 5)} " +
            r"= \frac{3}{2(10 - 5)} \times \frac{1}{5} \times dx")
        renyi = Tex(r"\frac{3}{2(10 - x)} \times \frac{1}{5} \times dx")
        xeq5.next_to(fruit1, UP, aligned_edge=LEFT, buff=1)
        renyi.next_to(fruit1, DOWN, aligned_edge=LEFT, buff=1)
        xeq5[0].set_color(RED)
        xeq5[2].set_color(YELLOW)
        fruit1[14].set_color(YELLOW)
        fruit1[24].set_color(YELLOW)
        fruit1[4:6].set_color(GREEN)
        fruit1[31:].set_color(GREEN)
        renyi[7].set_color(YELLOW)
        renyi[14:].set_color(GREEN)
        self.play(Write(xeq5))
        self.wait()
        self.play(Write(fruit1[:6]))
        self.wait()
        self.play(Write(fruit1[6:16]))
        self.wait()
        self.play(Write(fruit1[16:]))
        self.wait(2)
        self.play(Write(renyi))
        self.wait(3)
        self.play(*[FadeOut(i) for i in [xeq5, fruit1]])
        self.play(renyi.animate.move_to(UP*2))
        adds = Tex(r"\frac{3}{2(10 - 0)} \times \frac{1}{5} \times dx + \cdots " + 
            r"&+ \frac{3}{2(10 - x)} \times \frac{1}{5} \times dx + \cdots \\" +
            r"+ \frac{3}{2(10 - 5)} &\times \frac{1}{5} \times dx").move_to(DOWN)
        for i in [7, 28, 49]:
            adds[i].set_color(YELLOW)
        for i in [14, 35, 56]:
            adds[i:i+2].set_color(GREEN)
        self.play(Write(adds))
        self.wait(2)
        self.play(FadeOut(renyi))
        self.play(adds.animate.move_to(UP*2))
        self.wait()
        sumtx = Tex(r"\int_{0}^{5} \frac{3}{2(10 - x)} \frac{1}{5} dx")
        sumtx.move_to(DOWN)
        sumtx[10].set_color(YELLOW)
        sumtx[15:].set_color(GREEN)
        self.play(Write(sumtx))
        self.wait()
        self.play(FadeOut(adds))
        self.play(sumtx.animate.center())
        self.wait()
        sr = SurroundingRectangle(sumtx[2], color=RED)
        self.play(ShowCreationThenFadeOut(sr))
        self.wait()
        sr = SurroundingRectangle(sumtx[1], color=RED)
        self.play(ShowCreationThenFadeOut(sr))
        self.wait()
        fruit = Tex(r"= \frac{3}{10} ln2").next_to(sumtx, RIGHT)
        self.play(VGroup(sumtx, fruit.set_opacity(0)).animate.center())
        self.remove(fruit)
        fruit.set_opacity(1)
        self.wait()
        self.play(Write(fruit))


class GeneChangeGraph2(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 7, 1], x_axis_config={
            "include_tip": True,
        }, y_range=[0, 4, 1], y_axis_config={
            "include_tip": True,
        })
        color_nums = 10
        graphs = []
        for x in np.linspace(0, 5, color_nums + 1):
            nm = 2*(10 - x)/3
            curve = ax.get_graph(lambda x: 1/nm, [0, nm, 0.01])
            cl = interpolate_color(RED, GREEN, x / 5)
            gr = ax.get_riemann_rectangles(curve, [0, nm], 0.01, colors=[cl], stroke_width=0)
            graphs.append(gr)
        for i in range(color_nums):
            graphs[i + 1].next_to(graphs[i], UP, buff=0, aligned_edge=LEFT)
        this_one = VGroup(
            Arrow(graphs[5].get_corner(UR) + [2, 1, 0], graphs[5].get_corner(UR), buff=0.1),
            Tex(r"x = 2.5", t2c = {"x = 2.5": interpolate_color(RED, GREEN, 5 / color_nums)}).move_to(graphs[5].get_corner(UR) + [2, 1.3, 0])
        )
        self.add(ax, *graphs, this_one)
        self.wait()
        pos1 = graphs[5].get_corner(DR)
        pos2 = ax.c2p(ax.p2c(pos1)[0], 0)
        sr = Polygon(pos1, pos2, pos2 + RIGHT*0.05, pos1 + RIGHT*0.05)
        self.play(ShowCreationThenFadeOut(sr), run_time=2)
        self.wait()


class Sum2(Scene):
    def construct(self):
        sumtx = Tex(r"\int_{0}^{2.5} \frac{3}{2(10 - x)} \frac{1}{5} dx")
        sumtx[12].set_color(YELLOW)
        sumtx[17:].set_color(GREEN)
        self.wait()
        self.play(Write(sumtx))
        self.wait()
        sumtxy = Tex(r"\int_{0}^{y} \frac{3}{2(10 - x)} \frac{1}{5} dx")
        sumtxy[10].set_color(YELLOW)
        sumtxy[15:].set_color(GREEN)
        self.play(ReplacementTransform(sumtx[0], sumtxy[0]),
                  FadeTransform(sumtx[1:4], sumtxy[1:2]),
                  ReplacementTransform(sumtx[4:], sumtxy[2:]))
        self.wait()
        fy = Tex(r"f(y) = \frac{3}{10} \times (ln10 - ln\frac{3}{2} y)").shift(DOWN)
        self.play(sumtxy.animate.move_to(UP*2))
        self.play(Write(fy))
        self.wait()
        self.play(FadeOut(sumtxy), fy.animate.to_edge(UP))

        ax = Axes(x_range=[0, 8, 1], x_axis_config={
            "include_tip": True,
        }, y_range=[0, 0.5, 1], y_axis_config={
            "include_tip": True,
            "unit_size": 8
        })
        self.play(ShowCreation(ax))
        self.wait()
        def f(x):
            if x <= 10/3:
                return 3/10*np.log(2)
            else:
                return 3/10*(np.log(10) - np.log(3/2*x))
        graph = ax.get_graph(f, [0, 20/3, 0.01], color=BLUE)
        dot1 = Dot(ax.c2p(10/3, 0), fill_opacity=0)
        dot2 = Dot(ax.c2p(20/3, 0), fill_opacity=0)
        dot3 = Dot(ax.c2p(0, f(0)), fill_opacity=0)
        self.add(dot1, dot2, dot3)
        xlabel1 = Tex(r"\frac{10}{3}", font_size=36).next_to(dot1, DOWN, 0.05)
        xlabel2 = Tex(r"\frac{20}{3}", font_size=36).next_to(dot2, DOWN, 0.05)
        ylabel = Tex(r"\frac{3}{10} ln2", font_size=36).next_to(dot3, LEFT, 0.05)
        self.play(ShowCreation(graph))
        line1 = ax.get_v_line_to_graph(10/3, graph, color=GREEN)
        self.play(FadeIn(xlabel1), FadeIn(xlabel2), FadeIn(ylabel), FadeIn(line1))
        self.wait()


class Int1(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 8, 1], x_axis_config={
            "include_tip": True,
        }, y_range=[0, 0.5, 1], y_axis_config={
            "include_tip": True,
            "unit_size": 8
        })
        def f(x):
            if x <= 10/3:
                return 3/10*np.log(2)
            else:
                return 3/10*(np.log(10) - np.log(3/2*x))
        graph = ax.get_graph(f, [0, 20/3, 0.01], color=BLUE)
        dot1 = Dot(ax.c2p(10/3, 0), fill_opacity=0)
        dot2 = Dot(ax.c2p(20/3, 0), fill_opacity=0)
        dot3 = Dot(ax.c2p(0, f(0)), fill_opacity=0)
        xlabel1 = Tex(r"\frac{10}{3}", font_size=36).next_to(dot1, DOWN, 0.05)
        xlabel2 = Tex(r"\frac{20}{3}", font_size=36).next_to(dot2, DOWN, 0.05)
        ylabel = Tex(r"\frac{3}{10} ln2", font_size=36).next_to(dot3, LEFT, 0.05)
        line1 = ax.get_v_line_to_graph(10/3, graph, color=GREEN)
        self.add(ax, graph, dot1, dot2, dot3, xlabel1, xlabel2, ylabel, line1)
        self.wait()
        self.play(Uncreate(line1), Uncreate(xlabel1))
        dot1.move_to(ax.c2p(2, 0))
        x = Tex("x", t2c={"x": YELLOW}).next_to(dot1, DOWN, 0.05)
        dot2.move_to(ax.c2p(4, 0))
        y = Tex("y", t2c={"y": YELLOW}).next_to(dot2, DOWN, 0.05)
        self.play(FadeIn(x), dot1.animate.set_opacity(1))
        self.wait()
        self.play(FadeIn(y), dot2.animate.set_opacity(1))
        self.wait()
        y.add_updater(lambda x: x.next_to(dot2, DOWN, 0.05))
        self.play(dot2.animate.move_to(ax.c2p(6, 0)))
        self.play(dot2.animate.move_to(ax.c2p(3, 0)))
        self.play(dot2.animate.move_to(ax.c2p(4, 0)))        
        self.play(FadeOut(y), FadeOut(dot2))
        shade = ax.get_riemann_rectangles(graph, [2, 20/3], 0.01, fill_opacity=1, stroke_width=0, colors=[YELLOW])
        self.wait()
        for _ in range(3):
            self.play(FadeIn(shade), run_time=0.3)
            self.wait(0.3)
            self.play(FadeOut(shade), run_time=0.3)
        self.play(FadeIn(shade), run_time=0.3)
        self.wait()
        self.play(FadeOut(shade))
        self.wait()
        shader2 = ax.get_riemann_rectangles(graph, [2, 20/3], 0.3, fill_opacity=1, colors=[YELLOW, RED])
        self.play(ShowCreation(shader2))
        self.wait()
        twothere = VGroup(Dot(ax.c2p(2.38, 0), fill_opacity=0), Dot(ax.c2p(2.52, 0), fill_opacity=0))
        tx = Tex(r"dy", t2c={r"dy": RED}, font_size=24)
        brc = Brace(twothere, font_size=10, buff=0.01).put_at_tip(tx, buff=0.01)
        self.play(Write(brc), Write(tx))
        self.wait()
        twothere2 = VGroup(Dot(ax.c2p(2, 0.02), fill_opacity=0), Dot(ax.c2p(2, 3/10*np.log(2) - 0.02), fill_opacity=0))
        tx2 = Tex(r"f(y)", t2c={r"f(y)": RED}, font_size=24)
        brc2 = Brace(twothere2, font_size=10, buff=0.01, direction=LEFT).put_at_tip(tx2, buff=0.01)
        self.play(Write(brc2), Write(tx2))
        self.wait()


class Sum3(Scene):
    def construct(self):
        fruit1 = Tex(r"f(x)dy + \cdots + f(y)dy + \cdots + f(\frac{20}{3})dy", 
                     t2c={r"dy": GREEN})
        self.wait()
        self.play(Write(fruit1))
        self.wait()
        ints = Tex(r"\int_{x}^{\frac{20}{3}}f(y)dy")
        self.play(fruit1.animate.shift(UP*2))
        self.play(Write(ints))
        self.wait()
        mianji = Tex(r"\int_{x}^{\frac{20}{3}}f(y)dy \times \frac{1}{5} dx", t2c={"dx": GREEN})
        self.play(FadeOut(fruit1), ints.animate.shift(UP*2))
        self.play(Write(mianji))
        self.wait()
        self.play(FadeOut(ints), mianji.animate.shift(UP*2))
        adds = Tex(r"\int_{0}^{\frac{20}{3}}f(y)dy \times \frac{1}{5} dx + \cdots &+ \int_{x}^{\frac{20}{3}}f(y)dy \times \frac{1}{5} dx \\" +
                   r"+ \cdots+ \int_{5}^{\frac{20}{3}}f(&y)dy \times \frac{1}{5} dx", t2c={"dx": GREEN})
        self.play(Write(adds.shift(DOWN)))
        self.wait()
        ints2 = Tex(r"\int_{0}^{5}(\int_{x}^{\frac{20}{3}}f(y)dy)\frac{1}{5} dx")
        self.play(FadeOut(mianji), adds.animate.shift(UP*3))
        self.play(Write(ints2.shift(DOWN)))
        self.wait()


class GetYuan(Scene):
    def construct(self):
        pm = ImageMobject("assets/paimeng.png").scale(0.5)
        pms = Group(*[pm.copy() for _ in range(4)])
        pms.arrange(DOWN, buff=-0.3).shift(LEFT*4)
        pmas = VGroup(
            Tex("x", t2c={"x": YELLOW}),
            Tex(r"y = \frac{2}{3}(10 - x)", t2c={"x": YELLOW, "y": GREEN}),
            Tex(r"10 - x - y", t2c={"x": YELLOW, "y": GREEN}),
            Tex(r"10 - x - y", t2c={"x": YELLOW, "y": GREEN}),
        )
        for i in range(4):
            pmas[i].next_to(pms[i], RIGHT).set_x(0)
        pmbs = VGroup(
            Tex(r"5"),
            Tex(r"\frac{20}{3}"),
            Tex(r"10"),
            Tex(r"10"),
        )
        for i in range(4):
            pmbs[i].next_to(pms[i], RIGHT).set_x(4)
        for i in range(4):
            self.wait()
            self.play(FadeIn(pms[i]))
            self.wait()
            self.play(Write(pmas[i]))
            self.wait()
            self.play(Write(pmbs[i]))
        self.wait()


class BecomeLower(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 8, 1], x_axis_config={
            "include_tip": True,
        }, y_range=[0, 0.5, 1], y_axis_config={
            "include_tip": True,
            "unit_size": 8
        })
        def f(x):
            if x <= 3:
                return 0.3
            else:
                return 0.3-0.3/4*(x - 3)**2
        graph = ax.get_graph(f, [0, 5, 0.01], color=BLUE)
        self.add(ax, graph)
        self.wait()
        self.play(
            graph.animate.stretch_about_point(8/5, 0, graph.get_left()) \
                 .stretch_about_point(5/8, 1, graph.get_bottom()),
            run_time=3
        )
        self.wait()


class TheFinal1(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 8, 1], x_axis_config={
            "include_tip": True,
        }, y_range=[0, 0.5, 1], y_axis_config={
            "include_tip": True,
            "unit_size": 8
        })
        def f(x):
            if x <= 3:
                return 0.3
            else:
                return 0.3-0.3/9*(x - 3)**2
        self.add(ax)
        graph = ax.get_graph(f, [0, 6, 0.01], color=BLUE)
        self.play(ShowCreation(graph))
        self.wait()
        dot1 = Dot(ax.c2p(1, 0))
        dot2 = Dot(ax.c2p(3.5, 0))
        dot3 = Dot(ax.c2p(6, 0))
        dot4 = Dot(ax.c2p(7, 0))
        x = Tex("x", t2c={"x":YELLOW}).next_to(dot1, DOWN, 0.15)
        a = Tex("a", t2c={"a":YELLOW}).next_to(dot2, DOWN, 0.15)
        b = Tex("b", t2c={"b":YELLOW}).next_to(dot3, DOWN, 0.05)
        c = Tex("c", t2c={"c":YELLOW}).next_to(dot4, DOWN, 0.15)
        line1 = ax.get_v_line_to_graph(1, graph, color=GREEN)
        line2 = ax.get_v_line_to_graph(3.5, graph, color=GREEN)
        self.play(
            *[FadeIn(i) for i in [dot1, dot2, dot3, dot4, x, a, b, c, line1, line2]]
        )
        self.wait()
        s1 = Tex(r"S_1", t2c={"S_1": YELLOW}, font_size=72).move_to(ax.c2p(2.2, 0.15))
        s2 = Tex(r"S_2", t2c={"S_2": GREEN}, font_size=72).move_to(ax.c2p(4.8, 0.1))
        ss1 = ax.get_riemann_rectangles(graph, [1, 3.5], 0.01, fill_opacity=1, stroke_width=0, colors=[YELLOW])
        ss2 = ax.get_riemann_rectangles(graph, [3.5, 6], 0.01, fill_opacity=1, stroke_width=0, colors=[GREEN])
        self.play(Write(s1))
        for _ in range(3):
            self.play(FadeIn(ss1), run_time=0.3)
            self.wait(0.3)
            self.play(FadeOut(ss1), run_time=0.3)
        self.wait()
        self.play(Write(s2))
        for _ in range(3):
            self.play(FadeIn(ss2), run_time=0.3)
            self.wait(0.3)
            self.play(FadeOut(ss2), run_time=0.3)
        self.wait()


class Int2(Scene):
    def construct(self):
        s1gai = Tex(r"\int_{0}^{a}S_1f_1(x)dx")
        self.wait()
        self.play(Write(s1gai))
        self.wait()
        s2gai = Tex(r"\int_{0}^{b}(S_1 + S_2)f_3(z)dz")
        self.play(s1gai.animate.shift(UP))
        self.play(Write(s2gai.shift(DOWN)))
        self.wait()
        self.play(Indicate(s2gai[7:9]), run_time=2)
        self.wait()
        self.play(s1gai[:5].animate.set_opacity(0.2),
                  s1gai[10:].animate.set_opacity(0.2),
                  s2gai[:10].animate.set_opacity(0.2),
                  s2gai[15:].animate.set_opacity(0.2))
        self.play(s1gai[5:10].animate.move_to(LEFT),
                  s2gai[10:15].animate.move_to(RIGHT))
        self.wait()
        maxer = Tex(r">", t2c={">": YELLOW})
        self.play(FadeIn(maxer))
        self.wait()


class TheFinal2(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 8, 1], x_axis_config={
            "include_tip": True,
        }, y_range=[0, 0.5, 1], y_axis_config={
            "include_tip": True,
            "unit_size": 8
        })
        def f(x):
            if x <= 3:
                return 0.3
            else:
                return 0.3-0.3/9*(x - 3)**2
        graph = ax.get_graph(f, [0, 6, 0.01], color=BLUE)
        dot1 = Dot(ax.c2p(1, 0))
        dot2 = Dot(ax.c2p(3.5, 0))
        dot3 = Dot(ax.c2p(6, 0))
        dot4 = Dot(ax.c2p(7, 0))
        x = Tex("x", t2c={"x":YELLOW}).next_to(dot1, DOWN, 0.15)
        a = Tex("a", t2c={"a":YELLOW}).next_to(dot2, DOWN, 0.15)
        b = Tex("b", t2c={"b":YELLOW}).next_to(dot3, DOWN, 0.05)
        c = Tex("c", t2c={"c":YELLOW}).next_to(dot4, DOWN, 0.15)
        line1 = ax.get_v_line_to_graph(1, graph, color=GREEN)
        line2 = ax.get_v_line_to_graph(3.5, graph, color=GREEN)
        s1 = Tex(r"S_1", t2c={"S_1": YELLOW}, font_size=72).move_to(ax.c2p(2.2, 0.15))
        s2 = Tex(r"S_2", t2c={"S_2": GREEN}, font_size=72).move_to(ax.c2p(4.8, 0.1))
        self.add(ax, graph, dot1, dot2, dot3, dot4, x, a, b, c, line1, line2, s1, s2)
        self.wait()
        self.play(*[i.animate.shift(RIGHT*2) for i in [
            ax, graph, dot1, dot2, dot3, dot4, x, a, b, c, line1, line2, s1, s2
        ]])
        vl = ValueTracker(3.5)
        dot2.add_updater(lambda d: d.move_to(ax.c2p(vl.get_value(), 0)))
        a.add_updater(lambda d: d.next_to(dot2, DOWN, 0.15))
        line2.add_updater(lambda l: l.become(ax.get_v_line_to_graph(vl.get_value(), graph, color=GREEN)))
        s1.add_updater(lambda s: s.move_to(ax.c2p((1 + vl.get_value())/2 - 0.05, 0.15)))
        s2.add_updater(lambda s: s.move_to(ax.c2p((6 + vl.get_value())/2 + 0.05, 0.1 - 0.05*(vl.get_value() - 3.5))))
        pm = ImageMobject("assets/paimeng.png").scale(0.5)
        pms = Group(*[pm.copy() for _ in range(8)]).arrange_in_grid(4, 2, buff=0).to_edge(LEFT)
        self.play(FadeIn(pms[::2]))
        self.wait()
        self.play(FadeOut(pms[6]), vl.animate(rate_func=linear).set_value(4), run_time=1)
        self.play(FadeOut(pms[4]), vl.animate(rate_func=linear).set_value(4.5), run_time=1)
        self.wait()
        for i in [4, 6, 1, 3, 5]:
            self.play(FadeIn(pms[i]), vl.animate(rate_func=linear).set_value(vl.get_value() - 0.5), run_time=1)
        self.wait()
        line2.suspend_updating()
        self.play(*[i.animate.set_opacity(0.2) for i in self.mobjects if i not in [pms[5], graph]],
                    graph.animate.set_stroke(opacity=0.2))
        self.wait()
        self.play(pms[5].animate.move_to(LEFT*1.5))
        eq7 = Tex(r"=7", t2c={r"7": YELLOW}, font_size=72)
        self.play(Write(eq7))
        self.wait()
        self.embed()


class TheFinal3(Scene):
    def construct(self):
        pm = ImageMobject("assets/paimeng.png").scale(0.5)
        pms = Group(*[pm.copy() for _ in range(4)])
        pms.arrange(RIGHT, buff=0).shift(UP)
        baifen = Tex(r"27.5\%", t2c={r"27.5\%": YELLOW}, font_size=72).next_to(pms[0], DOWN)
        self.play(AnimationGroup(*[FadeIn(i) for i in pms], lag_ratio=0.5))
        self.wait()
        self.play(Write(baifen))
        self.play(Indicate(baifen))
        self.wait()
        self.play(FadeOut(baifen))
        self.wait()
        pms2 = Group(*[pm.copy() for _ in range(20)])
        pms2.arrange_in_grid(3, 7, buff=0).shift(UP)
        self.play(pms.animate.move_to(pms2.get_corner(UL), aligned_edge=UL))
        self.play(AnimationGroup(*[FadeIn(i) for i in pms2[4:]], lag_ratio=0.2))
        self.wait()
        baifen2 = Tex(r"10\%", t2c={r"10\%": YELLOW}, font_size=72).next_to(pms2[19], DOWN)
        self.play(Write(baifen2))
        self.play(Indicate(baifen2))
        self.wait()
