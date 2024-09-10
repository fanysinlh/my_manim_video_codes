from manim import *

class HXJBrace(Brace):
    def get_tex(self, *text, **kwargs):
        tex_mob = MathTex(*text, **kwargs)
        self.put_at_tip(tex_mob)
        return tex_mob
    
# manim ce/Toturial_3/demo.py -pql --renderer=opengl --write_to_movie
class DemoOpenGL(Scene):
    def construct(self):
        self.camera.set_euler_angles(phi=2*PI/5, theta=PI/5)
        axes = ThreeDAxes(
            x_range=[-7.5, 7.5, 1], y_range=[-5, 5, 1], x_length=15, y_length=10
        ).scale(0.8)
        self.play(Create(axes))
        self.wait()
        self.play(
            self.camera.animate.set_euler_angles(phi=0, theta=0),
            axes.animate.scale(1.25),
            run_time=3
        )
        self.wait()
        plane = NumberPlane()
        self.play(FadeOut(axes), FadeIn(plane), run_time=3)
        self.wait()

# manim ce/Toturial_3/demo.py -pql
class Demo1Cairo(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)
        d = Dot(color=RED)
        text = MathTex(R"(0, 0, 0)").next_to(d, UR)
        self.play(FadeIn(d), Write(text))
        self.wait()

        brw = HXJBrace(plane[2], color=YELLOW)
        brh = HXJBrace(
            plane[3], direction=LEFT, color=GREEN_E
        )
        textw = brw.get_tex(R"w = \frac{128}{9}", color=YELLOW)
        texth = brh.get_tex(R"h = 8", color=GREEN_E)
        self.play(FadeIn(brh), Write(texth), run_time=1)
        self.wait()
        self.play(FadeIn(brw), Write(textw), run_time=1)
        self.wait()
        self.play(*[Unwrite(i) for i in [brh, brw, texth, textw, d, text]])
        self.wait()

class Demo2Cairo(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)
        cdot = Dot([1, 1, 0], color=RED)
        ctext = MathTex("(1, 1, 0)").next_to(cdot, UR)
        sdot = Dot([-1, 2, 0], color=YELLOW)
        stext = MathTex("(-1, 2, 0)").next_to(sdot, UR)
        c = Circle().move_to(cdot)
        s = Square(color=YELLOW).move_to(sdot)
        self.wait()
        self.play(Create(c))
        self.wait()
        self.play(Create(s))
        self.wait()
        self.play(FadeIn(cdot, sdot))
        self.wait()
        self.play(Write(ctext), Write(stext))
        self.wait()
        self.play(*[Unwrite(i) for i in [c, s, ctext, stext, cdot, sdot]])
        self.wait()

class Demo3Cairo(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)
        c = Circle()
        s = Square(color=YELLOW)
        d = Dot(color=ORANGE)
        text = MathTex("(0, 0, 0)").next_to(d, UR)
        self.play(Create(c))
        self.play(Create(s))
        self.wait()
        self.play(FadeIn(d), Write(text))
        self.wait(3)
        self.play(FadeOut(d), Unwrite(text))
        self.wait()
        screen = ScreenRectangle(
            fill_color=self.camera.background_color, fill_opacity=1,
            stroke_color=YELLOW
        ).scale(0.5).to_corner(UL)
        self.play(FadeIn(screen))
        self.wait()
        mvt = Text("move_to", font="Courier New", font_size=20, color=YELLOW) \
            .move_to(screen.get_center() + UP/3)
        sx = Text("set_x", font="Courier New", font_size=20, color=RED)
        sy = Text("set_y", font="Courier New", font_size=20, color=BLUE)
        sz = Text("set_z", font="Courier New", font_size=20, color=GREEN)
        sg = VGroup(sx, sy, sz).arrange(RIGHT).move_to(screen.get_center() + DOWN/3)
        self.play(AnimationGroup(*[Write(i) for i in [mvt, sx, sy, sz]], lag_ratio=1))
        self.wait()
        self.play(FadeOut(sg, mvt))
        self.wait()
        dot110 = Dot([1, 1, 0], color=RED)

        # move_to及其aligned_edge
        self.play(Create(dot110), c.animate.move_to([1, 1, 0]))
        self.wait()
        self.play(c.animate.move_to([1, 1, 0], aligned_edge=RIGHT))
        self.wait()
        self.play(c.animate.move_to([1, 1, 0]))
        self.wait(2)
        self.play(c.animate.move_to([1, 1, 0], aligned_edge=RIGHT))
        self.wait()
        self.play(c.animate.move_to([1, 1, 0], aligned_edge=LEFT))
        self.wait()
        self.play(c.animate.move_to([1, 1, 0], aligned_edge=UP))
        self.wait()
        self.play(c.animate.move_to([1, 1, 0], aligned_edge=DOWN))
        self.wait(5)

        # 四个对角对齐
        self.play(c.animate.move_to([1, 1, 0], aligned_edge=UR))
        self.wait()
        self.play(c.animate.move_to([1, 1, 0], aligned_edge=DL))
        self.wait()
        self.play(c.animate.move_to([1, 1, 0], aligned_edge=DR))
        self.wait()
        self.play(c.animate.move_to([1, 1, 0], aligned_edge=UL))
        self.play(FadeOut(dot110))
        self.wait(3)

        # move_to(mob)
        self.play(s.animate.scale(2))
        self.wait(2)
        self.play(s.animate.move_to(c))
        self.wait(3)
        self.play(s.animate.move_to(c, aligned_edge=UR))
        self.wait()
        self.play(s.animate.move_to(c, aligned_edge=UL))
        self.wait()
        self.play(s.animate.move_to(c, aligned_edge=LEFT))

        # set类方法
        self.play(c.animate.set_x(0))
        self.wait(5)
        self.play(c.animate.set_x(0, direction=RIGHT))
        self.wait(3)

        self.play(FadeOut(s))


class Demo4Cairo(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)
        c = Circle().move_to(LEFT)
        screen = ScreenRectangle(
            fill_color=self.camera.background_color, fill_opacity=1,
            stroke_color=YELLOW
        ).scale(0.5).to_corner(UL)
        self.add(screen, c)
        self.wait()
        ct = Text("center", font="Courier New", font_size=20, color=YELLOW) \
            .move_to(screen.get_center() + UP/3)
        te = Text("to_edge", font="Courier New", font_size=20, color=RED)
        tc = Text("to_corner", font="Courier New", font_size=20, color=BLUE)
        VGroup(te, tc).arrange(RIGHT).move_to(screen.get_center() + DOWN/3)
        self.play(FadeIn(ct, te, tc))
        self.wait()
        self.play(FadeOut(ct, te, tc))
        self.wait()
        self.play(c.animate.center())
        self.wait()
        self.play(c.animate.to_edge(UP))
        self.wait(3)
        for i in [DOWN, LEFT, RIGHT]:
            self.play(c.animate.to_edge(i))
            self.wait(0.5)
        self.wait(3)
        self.play(c.animate.to_edge(UP))
        self.wait()
        self.play(c.animate.to_edge(DOWN))
        self.wait(2)
        self.play(c.animate.to_edge(LEFT))
        self.wait()
        self.play(c.animate.to_edge(RIGHT))
        self.wait(2)

        # buff
        self.play(c.animate.to_edge(RIGHT, buff=0))
        self.wait(2)

        # to_corner
        for i in [UL, DL, UR, DR]:
            self.play(c.animate.to_corner(i))
            self.wait()
        self.wait(2)
        self.play(c.animate.to_corner(DR, buff=0))
        self.wait()
        self.play(c.animate.to_corner(DR, buff=0.5))
        self.wait(2)


class Demo5Cairo(Scene):
    def construct(self):
        plane = NumberPlane()
        self.add(plane)
        c = Circle().to_corner(DR)
        screen = ScreenRectangle(
            fill_color=self.camera.background_color, fill_opacity=1,
            stroke_color=YELLOW
        ).scale(0.5).to_corner(UL)
        self.add(screen, c)
        self.wait()
        sf = Text("shift", font="Courier New", font_size=20, color=YELLOW) \
            .move_to(screen.get_center() + UP/3)
        nt = Text("next_to", font="Courier New", font_size=20, color=RED)
        at = Text("align_to", font="Courier New", font_size=20, color=BLUE)
        VGroup(nt, at).arrange(RIGHT).move_to(screen.get_center() + DOWN/3)
        self.play(FadeIn(sf, nt, at))
        self.wait()
        self.play(FadeOut(sf, nt, at))
        self.wait()

        # shift
        self.play(c.animate.shift(LEFT))
        self.wait(4)

        # next_to
        s = Square(color=YELLOW).scale(2)
        self.play(Create(s))
        self.wait(2)
        self.play(c.animate.next_to(s))
        self.wait(2)
        for i in [UR, LEFT, RIGHT]:
            self.play(c.animate.next_to(s, i))
            self.wait(1)
        # buff
        self.wait(3)

        # align_to
        self.wait(3)
        self.play(c.animate.align_to(s, UP))
        self.wait(2)
        self.play(c.animate.align_to(s, RIGHT))
        self.wait(2)
        for i in [UR, DR]:
            self.play(c.animate.align_to(s, i))
            self.wait()
        # 为啥不用move_to？
        self.wait(2)

        # 也可以坐标点
        dot110 = Dot([1, -1, 0], color=ORANGE)
        self.play(FadeIn(dot110))
        self.play(c.animate.next_to([1, -1, 0]))
        self.wait()
        dot200 = Dot([-2, 0, 0], color=ORANGE)
        self.play(FadeOut(dot110), FadeIn(dot200))
        self.play(c.animate.align_to([-2, 0, 0], LEFT))
        self.wait(3)
        self.play(FadeOut(dot200))

        # match方法
        sf = Text("match_x", font="Courier New", font_size=20, color=YELLOW) \
            .move_to(screen.get_center() + UP/3)
        nt = Text("match_y", font="Courier New", font_size=20, color=RED)
        at = Text("match_z", font="Courier New", font_size=20, color=BLUE)
        VGroup(nt, at).arrange(RIGHT).move_to(screen.get_center() + DOWN/3)
        self.play(FadeIn(sf, nt, at))
        self.wait(3)
        self.play(FadeOut(sf, nt, at))
        self.wait(2)
        self.play(c.animate.match_x(s))
        self.wait(5)

        # direction定位尴尬
        self.play(c.animate.match_x(s, RIGHT))
        self.wait(4)
        self.play(c.animate.match_x(s, UP))
        self.wait(3)
        self.play(Uncreate(c), Uncreate(s), Uncreate(screen), Uncreate(plane))
        self.wait()

class Demo6Cairo(Scene):
    def construct(self):
        r = Rectangle(color=YELLOW, fill_opacity=1)
        c = Circle(fill_opacity=1)
        VGroup(c, r).arrange(RIGHT, buff=2).shift(UP)
        tr = Tex("r").next_to(r, UP)
        tc = Tex("c").next_to(c, UP).add_updater(lambda mob: mob.next_to(c, UP))
        self.play(Create(r), Create(c))
        self.wait()
        self.play(Write(tr), Write(tc), run_time=0.5)
        self.wait()
        code1 = Text(
            "c.match_color(r)", font="Courier New", font_size=40, color=BLUE
        ).shift(DOWN*2)
        self.play(Write(code1), run_time=0.5)
        self.wait()
        self.play(c.animate.match_color(r))
        self.wait()
        self.play(FadeOut(code1), run_time=0.5)
        self.wait()
        code2 = Text(
            "c.match_width(r)", font="Courier New", font_size=40, color=RED
        ).shift(DOWN*2)
        self.play(Write(code2), run_time=0.5)
        self.wait()
        self.play(c.animate.match_width(r))
        self.wait()
        self.play(FadeOut(code2), run_time=0.5)
        self.wait()
        code3 = Text(
            "c.match_height(r)", font="Courier New", font_size=40, color=GREEN
        ).shift(DOWN*2)
        self.play(Write(code3), run_time=0.5)
        self.wait()
        self.play(c.animate.match_height(r))
        self.wait()
        self.play(FadeOut(code3), run_time=0.5)
        self.wait(3)

class Demo7Cairo(Scene):
    def construct(self):
        r = Rectangle(color=YELLOW, fill_opacity=1)
        c = Circle(color=YELLOW, fill_opacity=1)
        vg = VGroup(c, r).arrange(RIGHT, buff=2).shift(UP)
        tr = Tex("r").next_to(r, UP)
        tc = Tex("c").next_to(c, UP)
        self.add(vg, tr, tc)
        gc = Text(
            R"r.get_center()", font="Courier New", font_size=40, color=BLUE
        ).shift(DOWN*1.5)
        gcfruit = Text(
            f"Output: {r.get_center()}", font="Courier New", font_size=40, color=GREEN
        ).shift(DOWN*2.5)
        self.play(Write(gc))
        self.wait()
        d = Dot(r.get_center(), color=RED)
        self.play(Create(d))
        self.wait(2)
        self.play(Write(gcfruit))
        self.wait(2)
        self.play(FadeOut(gc, gcfruit))
        self.wait()
        gx = Text(
            R"r.get_x()", font="Courier New", font_size=40, color=BLUE
        ).shift(DOWN*1.5)
        gxfruit = Text(
            f"Output: {r.get_x()}", font="Courier New", font_size=40, color=GREEN
        ).shift(DOWN*2.5)
        gy = Text(
            R"r.get_y()", font="Courier New", font_size=40, color=BLUE
        ).shift(DOWN*1.5)
        gyfruit = Text(
            f"Output: {r.get_y()}", font="Courier New", font_size=40, color=GREEN
        ).shift(DOWN*2.5)
        self.play(FadeIn(gx, gxfruit))
        self.play(FadeTransform(gx, gy), FadeTransform(gxfruit, gyfruit))
        self.wait()
        self.play(FadeOut(gy, gyfruit, d))

        gl = Text(
            R"r.get_left()", font="Courier New", font_size=40, color=BLUE
        ).shift(DOWN*1.5)
        glfruit = Text(
            f"Output: {r.get_left()}", font="Courier New", font_size=40, color=GREEN
        ).shift(DOWN*2.5)
        dl = Dot(r.get_left(), color=RED)
        gr = Text(
            R"r.get_right()", font="Courier New", font_size=40, color=BLUE
        ).shift(DOWN*1.5)
        grfruit = Text(
            f"Output: {r.get_right()}", font="Courier New", font_size=40, color=GREEN
        ).shift(DOWN*2.5)
        dr = Dot(r.get_right(), color=RED)
        gt = Text(
            R"r.get_top()", font="Courier New", font_size=40, color=BLUE
        ).shift(DOWN*1.5)
        gtfruit = Text(
            f"Output: {r.get_top()}", font="Courier New", font_size=40, color=GREEN
        ).shift(DOWN*2.5)
        dt = Dot(r.get_top(), color=RED)
        gb = Text(
            R"r.get_bottom()", font="Courier New", font_size=40, color=BLUE
        ).shift(DOWN*1.5)
        gbfruit = Text(
            f"Output: {r.get_bottom()}", font="Courier New", font_size=40, color=GREEN
        ).shift(DOWN*2.5)
        db = Dot(r.get_bottom(), color=RED)
        gcur = Text(
            R"r.get_corner(UR)", font="Courier New", font_size=40, color=BLUE
        ).shift(DOWN*1.5)
        gcurfruit = Text(
            f"Output: {r.get_corner(UR)}", font="Courier New", font_size=40, color=GREEN
        ).shift(DOWN*2.5)
        dcur = Dot(r.get_corner(UR), color=RED)
        gcul = Text(
            R"r.get_corner(UL)", font="Courier New", font_size=40, color=BLUE
        ).shift(DOWN*1.5)
        gculfruit = Text(
            f"Output: {r.get_corner(UL)}", font="Courier New", font_size=40, color=GREEN
        ).shift(DOWN*2.5)
        dcul = Dot(r.get_corner(UL), color=RED)

        self.play(Write(gl))
        self.play(Create(dl))
        self.play(Write(glfruit))
        self.wait(2)
        self.play(
            FadeTransform(gl, gr),
            FadeTransform(glfruit, grfruit),
            FadeTransform(dl, dr),
        )
        self.wait()
        self.play(
            FadeTransform(gr, gt),
            FadeTransform(grfruit, gtfruit),
            FadeTransform(dr, dt),
        )
        self.wait()
        self.play(
            FadeTransform(gt, gb),
            FadeTransform(gtfruit, gbfruit),
            FadeTransform(dt, db),
        )
        self.wait(3)
        self.play(
            FadeTransform(gb, gcur),
            FadeTransform(gbfruit, gcurfruit),
            FadeTransform(db, dcur),
        )
        self.wait()
        self.play(
            FadeTransform(gcur, gcul),
            FadeTransform(gcurfruit, gculfruit),
            FadeTransform(dcur, dcul),
        )
        self.wait(4)
