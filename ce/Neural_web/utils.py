from manim import *

class ImageAndSign(Group):
    def __init__(self, image, sign, **kwargs):
        super().__init__(**kwargs)
        self.image = ImageMobject(image).scale_to_fit_width(1)
        self.sign = DecimalNumber(sign, num_decimal_places=0).scale_to_fit_height(0.2).next_to(self.image, DOWN, buff=0.1)
        self.image_rectangle = Rectangle(height=self.image.get_height(), width=self.image.get_width(), stroke_color=WHITE, fill_opacity=0)
        self.add(self.image_rectangle, self.image, self.sign)

class ImageMesh(Group):
    def __init__(self, images, signs, row, col, **kwargs):
        super().__init__(**kwargs)
        self.image_and_signs = [ImageAndSign(image, sign) for image, sign in zip(images, signs)]
        self.images = [i.image for i in self.image_and_signs]
        self.signs = [i.sign for i in self.image_and_signs]
        self.add(*self.image_and_signs)
        self.arrange_in_grid(row, col, buff=0.1)
        self.box = SurroundingRectangle(self, stroke_color=YELLOW)
        self.add(self.box)

class ExpMachine(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.exptext = Text("共享单车\n  预测器", t2c={
            "共享单车": BLUE,
            "预测器": YELLOW,
        }, line_spacing=0.8)
        self.exprec = SurroundingRectangle(self.exptext, buff=0.2, color=WHITE)
        rec_ul = self.exprec.get_corner(UL)
        rec_ur = self.exprec.get_corner(UR)
        rec_dr = self.exprec.get_corner(DR)
        rec_dl = self.exprec.get_corner(DL)
        self.expin = Polygon(rec_dl, rec_ul, 
                        rec_ul + UL + LEFT, rec_dl + DL + LEFT,
                        color=WHITE)
        self.expout = Polygon(rec_ur, rec_dr, 
                         rec_dr + DR + RIGHT, rec_ur + UR + RIGHT,
                         color=WHITE)
        self.expintext = Text("输\n入", color=RED).move_to(self.expin.get_center())
        self.expouttext = Text("输\n出", color=GREEN).move_to(self.expout.get_center())
        self.add(self.exptext, self.exprec, 
                 self.expin, self.expout, 
                 self.expintext, self.expouttext)


class NN(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        circle1 = Circle(color=YELLOW, radius=0.6)
        circle2 = circle1.copy()
        circle3 = circle1.copy()
        lastcircle = circle1.copy()
        self.circles1 = VGroup(circle1, circle2, circle3).arrange(RIGHT, buff=1)
        self.lastcircle = lastcircle.next_to(self.circles1, UP, buff=2)
        line1 = Line(circle1.get_center(), lastcircle.get_center(), color=WHITE, buff=0.6)
        line2 = Line(circle2.get_center(), lastcircle.get_center(), color=WHITE, buff=0.6)
        line3 = Line(circle3.get_center(), lastcircle.get_center(), color=WHITE, buff=0.6)
        self.lines = VGroup(line1, line2, line3)
        self.add(circle1, circle2, circle3, lastcircle, line1, line2, line3)


class OnlyOneNN(VGroup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        circle1 = Circle(color=YELLOW, radius=0.6)
        circle2 = circle1.copy()
        circle3 = circle1.copy()
        VGroup(circle1, circle2, circle3).arrange(DOWN, buff=1)
        line1 = Line(circle1.get_center(), circle2.get_center(), color=WHITE, buff=0.6)
        line2 = Line(circle2.get_center(), circle3.get_center(), color=WHITE, buff=0.6)
        self.lines = [line1, line2]
        self.circles = [circle1, circle2, circle3]
        self.add(circle1, circle2, circle3, line1, line2)

# 旋转飞出的动画
def get_spiral_out(mob, angle):
    tr = mob.get_center()
    def spiral_out(mb: Mobject, t):
        mb.rotate(angle * t * 0.5)
        mb.shift(tr * t * 0.5)
    return spiral_out
