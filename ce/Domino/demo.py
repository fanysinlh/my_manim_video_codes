from typing import Sequence
from manim import *
from dice import TwoDice
import random
class SickChess(VGroup):
    def __init__(self, factor, **kwargs):
        super().__init__(**kwargs)
        self.factor = factor
        for i in range(factor):
            for j in range(factor):
                cl = WHITE if (i + j) % 2 else BLACK
                self.add(Square(fill_opacity=1, color=cl, stroke_color = GREY, stroke_width=3)
                            .scale(0.5).move_to((i - 3.5)*LEFT + (j - 3.5)*UP))
        self[0].set_stroke(opacity=0)
        self[self.factor**2 - 1].set_stroke(opacity=0)
                
    def get(self, i, j):
        return self[self.factor**2 - 1 - i * self.factor - j]
    
    def get_width(self):
        return self[0].get_width()
    

# 判断棋盘里还能不能放
def can_put(m, f):
    for i in range(1, f):
        for j in range(1, f):
            if m[i][j] and (m[i - 1][j] or m[i][j - 1]):
                return True
    return False


class Chesses(VGroup):
    def __init__(self, s: SickChess, **kwargs):
        super().__init__(**kwargs)
        self.is_rotate = [False for _ in range(s.factor**2//2 - 1)]
        for _ in range(s.factor**2//2 - 1):
            rand1 = random.randint(1, 6)
            rand2 = random.randint(1, 6)
            c = TwoDice(rand1, rand2).scale_to_fit_height(s.get_width())
            self.add(c)
        self.arrange_in_grid(4, 8).center().shift(DOWN * 2.5)

    # def random_go(self, s: SickChess):
    #     matrix = [[1 for _ in range(s.factor)] for _ in range(s.factor)]
    #     matrix[0][0] = matrix[s.factor - 1][s.factor - 1] = 0
    #     self.random_go_one_step(s, matrix, 0)

    # def random_go_one_step(self, s: SickChess, m, index):
    #     f = s.factor
    #     if not can_put(m, f):
    #         return False
    #     if index == f**2//2 - 3:
    #         for _ in range(100):  # 限制尝试次数，避免死循环
    #             rdm1 = random.randint(1, f - 1)
    #             rdm2 = random.randint(1, f - 1)
    #             if m[rdm1][rdm2] == 1:
    #                 m[rdm1][rdm2] = 0
    #                 if m[rdm1][rdm2 - 1] == 1:
    #                     m[rdm1][rdm2 - 1] = 0
    #                     self[index].move_to(s.get(rdm1, rdm2).get_left())
    #                     return True
    #                 m[rdm1][rdm2 - 1] = 1
    #                 if m[rdm1 - 1][rdm2] == 1:
    #                     m[rdm1 - 1][rdm2] = 0
    #                     self[index].rotate(90*DEGREES).move_to(s.get(rdm1, rdm2).get_top())
    #                     return True
    #                 m[rdm1 - 1][rdm2] = 0
    #             m[rdm1][rdm2] = 1
    #         return False  # 如果在尝试后未找到位置，返回 False

    #     for _ in range(100):  # 限制尝试次数
    #         rdm1 = random.randint(1, f - 1)
    #         rdm2 = random.randint(1, f - 1)
    #         if m[rdm1][rdm2] == 1:
    #             m[rdm1][rdm2] = 0
    #             if m[rdm1][rdm2 - 1] == 1:
    #                 m[rdm1][rdm2 - 1] = 0
    #                 if self.random_go_one_step(s, m, index + 1):
    #                     self[index].move_to(s.get(rdm1, rdm2).get_left())
    #                     return True
    #                 m[rdm1][rdm2 - 1] = 1  # 恢复状态以便回溯
    #             if m[rdm1 - 1][rdm2] == 1:
    #                 m[rdm1 - 1][rdm2] = 0
    #                 if self.random_go_one_step(s, m, index + 1):
    #                     self[index].rotate(90*DEGREES).move_to(s.get(rdm1, rdm2).get_top())
    #                     return True
    #                 m[rdm1 - 1][rdm2] = 1  # 恢复状态以便回溯
    #             m[rdm1][rdm2] = 1  # 恢复状态以便回溯
    #     return False  # 如果在尝试后未找到位置，返回 False

    def arrange_chesses_1(self, s: SickChess):
        # 手动设置30个骨牌的位置，确保棋盘左上和右下角没有被占用
        positions_x = [
            (2, 0), (4, 0), (6, 0), (1, 1),
            (3, 1), (5, 1), (7, 1), (1, 2),
            (3, 2), (5, 2), (7, 2), (1, 3),
            (3, 3), (5, 3), (7, 3), (1, 4),
            (3, 4), (5, 4), (7, 4), (1, 5),
            (3, 5), (5, 5), (7, 5), (1, 6),
            (3, 6), (5, 6), (7, 6), (1, 7),
            (3, 7), (5, 7),
        ]

        positions_y = [

        ]

        anims = []
        for i, (x, y) in enumerate(positions_x):
            if self.is_rotate[i]:
                anims.append(RotateWithMove(
                    self[i], -90*DEGREES, s.get(x, y).get_left()
                ))
                self.is_rotate[i] = False
            else:
                anims.append(self[i].animate.move_to(s.get(x, y).get_left()))
        for i, (x, y) in enumerate(positions_y):
            if self.is_rotate[i + len(positions_x)]:
                anims.append(self[i + len(positions_x)].animate.move_to(s.get(x, y).get_top()))
            else:
                anims.append(RotateWithMove(
                    self[i + len(positions_x)], 90*DEGREES, s.get(x, y).get_top()
                ))
                self.is_rotate[i + len(positions_x)] = True
        return anims

    def arrange_chesses_2(self, s: SickChess):
        # 手动设置30个骨牌的位置，确保棋盘左上和右下角没有被占用
        positions_x = [
            (2, 0), (5, 0), (7, 0), (2, 1),
            (5, 1), (7, 1), (2, 2), (5, 2),
            (7, 2), (1, 7), (3, 7), (5, 7),
        ]

        positions_y = [
            (0, 4), (1, 4), (2, 4), (3, 4), 
            (4, 4), (5, 4), (6, 4), (7, 4),
            (0, 6), (1, 6), (2, 6), (3, 6),
            (4, 6), (5, 6), (6, 6), (7, 6),
            (3, 1), (0, 2)
        ]

        anims = []
        for i, (x, y) in enumerate(positions_x):
            if self.is_rotate[i]:
                anims.append(RotateWithMove(
                    self[i], -90*DEGREES, s.get(x, y).get_left()
                ))
                self.is_rotate[i] = False
            else:
                anims.append(self[i].animate.move_to(s.get(x, y).get_left()))
        for i, (x, y) in enumerate(positions_y):
            if self.is_rotate[i + len(positions_x)]:
                anims.append(self[i + len(positions_x)].animate.move_to(s.get(x, y).get_top()))
            else:
                anims.append(RotateWithMove(
                    self[i + len(positions_x)], 90*DEGREES, s.get(x, y).get_top()
                ))
                self.is_rotate[i + len(positions_x)] = True
        return anims

    def arrange_chesses_3(self, s: SickChess):
        # 手动设置30个骨牌的位置，确保棋盘左上和右下角没有被占用
        positions_y = [
            (2, 0), (4, 0), (6, 0), (1, 1),
            (3, 1), (5, 1), (7, 1), (1, 2),
            (3, 2), (5, 2), (7, 2), (1, 3),
            (3, 3), (5, 3), (7, 3), (1, 4),
            (3, 4), (5, 4), (7, 4), (1, 5),
            (3, 5), (5, 5), (7, 5), (1, 6),
            (3, 6), (5, 6), (7, 6), (1, 7),
            (3, 7), (5, 7),
        ]

        positions_x = [

        ]

        anims = []
        for i, (x, y) in enumerate(positions_x):
            if self.is_rotate[i]:
                anims.append(RotateWithMove(
                    self[i], -90*DEGREES, s.get(y, x).get_left()
                ))
                self.is_rotate[i] = False
            else:
                anims.append(self[i].animate.move_to(s.get(y, x).get_left()))
        for i, (x, y) in enumerate(positions_y):
            if self.is_rotate[i + len(positions_x)]:
                anims.append(self[i + len(positions_x)].animate.move_to(s.get(y, x).get_top()))
            else:
                anims.append(RotateWithMove(
                    self[i + len(positions_x)], 90*DEGREES, s.get(y, x).get_top()
                ))
                self.is_rotate[i + len(positions_x)] = True
        return anims

    def arrange_chesses_4(self, s: SickChess):
        # 手动设置30个骨牌的位置，确保棋盘左上和右下角没有被占用
        positions_y = [
            (2, 0), (5, 0), (7, 0), (2, 1),
            (5, 1), (7, 1), (2, 2), (5, 2),
            (7, 2), (1, 7), (3, 7), (5, 7),
        ]

        positions_x = [
            (0, 4), (1, 4), (2, 4), (3, 4), 
            (4, 4), (5, 4), (6, 4), (7, 4),
            (0, 6), (1, 6), (2, 6), (3, 6),
            (4, 6), (5, 6), (6, 6), (7, 6),
            (3, 1), (0, 2)
        ]

        anims = []
        for i, (x, y) in enumerate(positions_x):
            if self.is_rotate[i]:
                anims.append(RotateWithMove(
                    self[i], -90*DEGREES, s.get(y, x).get_left()
                ))
                self.is_rotate[i] = False
            else:
                anims.append(self[i].animate.move_to(s.get(y, x).get_left()))
        for i, (x, y) in enumerate(positions_y):
            if self.is_rotate[i + len(positions_x)]:
                anims.append(self[i + len(positions_x)].animate.move_to(s.get(y, x).get_top()))
            else:
                anims.append(RotateWithMove(
                    self[i + len(positions_x)], 90*DEGREES, s.get(y, x).get_top()
                ))
                self.is_rotate[i + len(positions_x)] = True
        return anims

    def return_position(self):
        anims = []
        cp = self.copy()
        for i in range(len(cp.submobjects)):
            if cp.is_rotate[i] == True:
                cp[i].rotate(-90 * DEGREES)
        cp.arrange_in_grid(4, 8).center().shift(DOWN * 2.5)
        for i in range(len(self.submobjects)):
            if self.is_rotate[i] == True:
                anims.append(RotateWithMove(self[i], -90*DEGREES, cp[i]))
                self.is_rotate[i] = False
            else:
                anims.append(self[i].animate.move_to(cp[i]))
        return anims
    

class RotateWithMove(Transform):
    def __init__(
        self,
        mobject: Mobject,
        angle: float = PI,
        target_mobject: Sequence[float] | None = None,
        **kwargs,
    ) -> None:
        if "path_arc" not in kwargs:
            kwargs["path_arc"] = angle
        if "path_arc_axis" not in kwargs:
            kwargs["path_arc_axis"] = OUT
        self.angle = angle
        self.target = target_mobject
        self.about_point = mobject.get_center()
        tm = mobject.copy().rotate(self.angle).move_to(target_mobject)
        super().__init__(mobject, path_arc_centers=self.about_point, target_mobject=tm, **kwargs)

    def create_target(self) -> Mobject:
        target = self.mobject.copy()
        target.rotate(
            self.angle,
        ).move_to(self.target)
        return target


class Demo(Scene):
    def construct(self):
        s = SickChess(8).scale(0.5)
        chesses = Chesses(s).shift(DOWN*10 + LEFT*20)
        self.wait()
        self.play(FadeIn(s))
        self.wait(3)
        self.play(Indicate(s[0], scale_factor=1), Indicate(s[s.factor**2 - 1], scale_factor=1))
        self.wait()
        self.play(s.animate.shift(UP*1.5))
        self.play(AnimationGroup(*[i.animate.shift(UP*10 + RIGHT*20) for i in chesses], lag_ratio=0.1))
        self.wait()
        self.play(AnimationGroup(*chesses.arrange_chesses_1(s), lag_ratio=0))
        self.wait()
        self.play(AnimationGroup(*chesses.arrange_chesses_2(s), lag_ratio=0))
        self.wait()
        self.play(AnimationGroup(*chesses.arrange_chesses_3(s), lag_ratio=0))
        self.wait()
        self.play(AnimationGroup(*chesses.arrange_chesses_4(s), lag_ratio=0))
        self.wait(5)
        self.play(AnimationGroup(*chesses.return_position(), lag_ratio=0))
        self.wait(2)

        wdt = s.get_width()
        horzontal_rec = Rectangle(color=YELLOW, height=wdt, 
                                  width=wdt*2).move_to(s.get(2, 0).get_left())
        vertical_rec = Rectangle(color=YELLOW, height=wdt*2, 
                                 width=wdt).move_to(s.get(0, 4).get_top())
        self.play(Create(horzontal_rec), Create(vertical_rec))
        self.wait()
        self.play(horzontal_rec.animate.shift(RIGHT*wdt),
                  vertical_rec.animate.shift(DOWN*wdt))
        self.wait()
        self.play(horzontal_rec.animate.shift(RIGHT*wdt),
                  vertical_rec.animate.shift(RIGHT*wdt))
        self.wait()
        self.play(horzontal_rec.animate.shift(DOWN*wdt),
                  vertical_rec.animate.shift(DOWN*wdt))
        self.wait()
        self.play(Uncreate(horzontal_rec), Uncreate(vertical_rec))
        self.wait()

        left_pos = s.get(0, 0).get_center() + (4.5*RIGHT + 8*LEFT)*wdt
        down_pos = left_pos + 1.5*DOWN
        anims = []
        w_num = 0
        b_num = 0
        for i in range(8):
            for j in range(8):
                if (i == 0 and j == 0) or (i == 7 and j == 7):
                    continue
                if (i + j) % 2 == 1: # 白色
                    if w_num <= 15:
                        anims.append(s.get(j, i).animate.move_to(left_pos + w_num*wdt*RIGHT))
                    else:
                        anims.append(s.get(j, i).animate.move_to(down_pos + (w_num - 16)*wdt*RIGHT))
                    w_num += 1
                else:
                    if b_num <= 15:
                        anims.append(s.get(j, i).animate.move_to(left_pos + b_num*wdt*RIGHT + wdt*DOWN))
                    else:
                        anims.append(s.get(j, i).animate.move_to(down_pos + (b_num - 16)*wdt*RIGHT + wdt*DOWN))
                    b_num += 1
        self.play(AnimationGroup(*anims, lag_ratio=0.1))
        self.wait()

        new_anims = []
        for i in range(30):
            if i <= 15:
                new_anims.append(
                    RotateWithMove(chesses[i], 90*DEGREES, left_pos + 0.5*DOWN*wdt + i*RIGHT*wdt)
                )
            else:
                new_anims.append(
                    RotateWithMove(chesses[i], 90*DEGREES, down_pos + 0.5*DOWN*wdt + (i - 16)*RIGHT*wdt)
                )
        self.play(AnimationGroup(*new_anims, lag_ratio=0.1))
        self.wait()
        self.add(chesses[30])
        self.play(chesses[30].animate.move_to(down_pos + 14.5*RIGHT*wdt))
        self.wait()
