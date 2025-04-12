from janim.imports import *

class Table(Group):
    def __init__(self, rols, cols, unit_length, unit_height, if_corner=False, **kwargs):
        super().__init__(**kwargs)
        self.rols = rols
        self.cols = cols
        self.unit_length = unit_length
        self.unit_height = unit_height
        self.if_corner = if_corner
        self.create_table()
        self.points.to_center()
        if if_corner:
            self.add_corner()

    def create_table(self):
        for i in range(self.rols):
            for j in range(self.cols):
                rect = Rect(self.unit_length, self.unit_height, fill_alpha=0.5, fill_color=BLACK)
                rect.points.move_to([i*self.unit_length,  - j*self.unit_height, 0])
                self.add(rect)

    def add_corner(self):
        c_cell = self.get_cell(0,0)
        self.up = Polygon(c_cell.points.box.get(UL), c_cell.points.box.get(DR), c_cell.points.box.get(UR))
        self.down = Polygon(c_cell.points.box.get(UL), c_cell.points.box.get(DR), c_cell.points.box.get(DL))
        self.add(self.up, self.down)

    def get_cell(self, rol, col) -> Rect:
        return self[col*self.rols+rol]
    
    def get_corner(self, if_up):
        if not self.if_corner:
            raise ValueError("The table is not a corner table")
        if if_up:
            return self.up
        else:
            return self.down
    

class Demo1(Timeline):
    def construct(self):
        table = Table(3, 3, 2.2, 1, True)
        table.points.scale(1.5)
        self.show(table)
        a = Text("A", color=RED)
        pos = table.get_cell(0, 0).points.box.center
        a.points.move_to(pos + DL*0.3).scale(1.5)
        b = Text("B", color=BLUE)
        b.points.move_to(pos + UR*0.3).scale(1.5)
        self.show(a, b)
        s_b = SVGItem(r"images\straight_blue.svg")
        b_b = SVGItem(r"images\back_blue.svg")
        s_b.points.scale(3).move_to(table.get_cell(0, 1))
        b_b.points.scale(3).move_to(table.get_cell(0, 2))
        s_r = SVGItem(r"images\straight_red.svg")
        b_r = SVGItem(r"images\back_red.svg")
        s_r.points.scale(3).move_to(table.get_cell(1, 0))
        b_r.points.scale(3).move_to(table.get_cell(2, 0))
        self.show(s_b, b_b, s_r, b_r)
        self.forward(4)

        def rec_anim(rols, cols, rols_first=True, run_time=1):
            if rols_first:
                self.play(AnimGroup(
                    *[table.get_cell(rols, i).anim.fill.set(RED) for i in range(3)],
                    duration=run_time
                ))
                def cl(i):
                    if i == rols:
                        return PURPLE
                    else:
                        return BLUE
                self.play(AnimGroup(
                    *[table.get_cell(i, cols).anim.fill.set(cl(i)) for i in range(3)],
                    duration=run_time
                ))
            else:
                self.play(AnimGroup(
                    *[table.get_cell(i, cols).anim.fill.set(BLUE) for i in range(3)],
                    duration=run_time
                ))
                def cl(i):
                    if i == cols:
                        return PURPLE
                    else:
                        return RED
                self.play(AnimGroup(
                    *[table.get_cell(rols, i).anim.fill.set(cl(i)) for i in range(3)],
                    duration=run_time
                ))
 
        def rec_anim_back(rols, cols):
            self.play(AnimGroup(
                *[table.get_cell(rols, i).anim.fill.set(BLACK) for i in range(3)],
                *[table.get_cell(i, cols).anim.fill.set(BLACK) for i in range(3)]
            ))

        rec_anim(1, 2)
        self.forward()
        pm1 = Text("+10 -10")
        pm1.points.move_to(table.get_cell(1, 2).points.box.center).scale(1.5)
        for i in pm1[0][0:3]: 
            i.color.set(RED)
        for i in pm1[0][3:]: 
            i.color.set(BLUE)
        self.play(Write(pm1[0][0:3]))
        self.forward()
        self.play(Write(pm1[0][3:]))
        rec_anim_back(1, 2)
        self.forward()

        rec_anim(2, 1, False)
        self.forward()
        pm2 = Text("-10 +10")
        pm2.points.move_to(table.get_cell(2, 1).points.box.center).scale(1.5)
        for i in pm2[0][0:3]: 
            i.color.set(RED)
        for i in pm2[0][3:]: 
            i.color.set(BLUE)
        self.play(Write(pm2[0][3:]))
        self.forward(0.5)
        self.play(Write(pm2[0][0:3]))
        rec_anim_back(2, 1)
        self.forward(0.5)

        rec_anim(2, 2, True, 0.5)
        self.forward(2)
        pm3 = Text("0 0")
        pm3.points.move_to(table.get_cell(2, 2).points.box.center).scale(1.5)
        for i in pm3[0][0:1]: 
            i.color.set(RED)
        for i in pm3[0][1:]: 
            i.color.set(BLUE)
        self.play(Write(pm3))
        rec_anim_back(2, 2)
        self.forward()

        rec_anim(1, 1, True, 0.5)
        self.forward(2)
        pm4 = Text("-1000 -1000")
        pm4.points.move_to(table.get_cell(1, 1).points.box.center).scale(1.5)
        for i in pm4[0][0:5]: 
            i.color.set(RED)
        for i in pm4[0][5:]: 
            i.color.set(BLUE)
        self.play(Write(pm4))
        rec_anim_back(1, 1)
        self.forward()


class Demo2(Timeline):
    def construct(self):
        table = Table(3, 3, 2.2, 1, True)
        table.points.scale(1.5)
        self.show(table)
        ru = SVGItem(r"images\ru.svg")
        pos = table.get_cell(0, 0).points.box.center
        ru.points.move_to(pos + DL*0.3 + LEFT*0.3).scale(2)
        us = SVGItem(r"images\us.svg")
        us.points.move_to(pos + UR*0.3 + RIGHT*0.3).scale(2)
        self.show(ru, us)
        s_b = SVGItem(r"images\bomb_blue.svg")
        b_b = SVGItem(r"images\peace_blue.svg")
        s_b.points.scale(0.2).move_to(table.get_cell(0, 1))
        b_b.points.scale(0.2).move_to(table.get_cell(0, 2))
        s_r = SVGItem(r"images\bomb_red.svg")
        b_r = SVGItem(r"images\peace_red.svg")
        s_r.points.scale(0.2).move_to(table.get_cell(1, 0))
        b_r.points.scale(0.2).move_to(table.get_cell(2, 0))
        self.show(s_b, b_b, s_r, b_r)
        pm1 = Text("+10 -10")
        pm1.points.move_to(table.get_cell(1, 2).points.box.center).scale(1.5)
        for i in pm1[0][0:3]: 
            i.color.set(RED)
        for i in pm1[0][3:]: 
            i.color.set(BLUE)
        pm2 = Text("-10 +10")
        pm2.points.move_to(table.get_cell(2, 1).points.box.center).scale(1.5)
        for i in pm2[0][0:3]: 
            i.color.set(RED)
        for i in pm2[0][3:]: 
            i.color.set(BLUE)
        pm3 = Text("0 0")
        pm3.points.move_to(table.get_cell(2, 2).points.box.center).scale(1.5)
        for i in pm3[0][0:1]: 
            i.color.set(RED)
        for i in pm3[0][1:]: 
            i.color.set(BLUE)
        pm4 = Text("-1000 -1000")
        pm4.points.move_to(table.get_cell(1, 1).points.box.center).scale(1.5)
        for i in pm4[0][0:5]: 
            i.color.set(RED)
        for i in pm4[0][5:]: 
            i.color.set(BLUE)
        self.show(pm1, pm2, pm3, pm4)
        self.forward(4)
        def rec_anim(num, if_rol=True, run_time=1, pu=None):
            if if_rol:
                if pu != None:
                    def cl(i):
                        if i == pu:
                            return PURPLE
                        else:
                            return RED
                    self.play(AnimGroup(
                        *[table.get_cell(num, i).anim.fill.set(cl(i)) for i in range(3)],
                        duration=run_time
                    ))
                else:
                    self.play(AnimGroup(
                        *[table.get_cell(num, i).anim.fill.set(RED) for i in range(3)],
                        duration=run_time
                    ))
            else:
                if pu != None:
                    def cl(i):
                        if i == pu:
                            return PURPLE
                        else:
                            return BLUE
                    self.play(AnimGroup(
                        *[table.get_cell(i, num).anim.fill.set(cl(i)) for i in range(3)],
                        duration=run_time
                    ))
                else:
                    self.play(AnimGroup(
                        *[table.get_cell(i, num).anim.fill.set(BLUE) for i in range(3)],
                        duration=run_time
                    ))
        def rec_anim_back(num, if_rol=True):
            if if_rol:
                self.play(AnimGroup(
                    *[table.get_cell(num, i).anim.fill.set(BLACK) for i in range(3)],
                ))
            else:
                self.play(AnimGroup(
                    *[table.get_cell(i, num).anim.fill.set(BLACK) for i in range(3)],
                ))

        rec_anim(1)
        self.forward(5)
        rec_anim(1, False, 1, 1)
        self.forward(5)
        

class Demo3(Timeline):
    def construct(self):
        table = Table(3, 3, 2.2, 1, True)
        table.points.scale(1.5)
        self.show(table)
        ru = SVGItem(r"images\so.svg")
        pos = table.get_cell(0, 0).points.box.center
        ru.points.move_to(pos + DL*0.3 + LEFT*0.3).scale(0.13)
        us = SVGItem(r"images\us.svg")
        us.points.move_to(pos + UR*0.3 + RIGHT*0.3).scale(2)
        self.show(ru, us)
        s_b = SVGItem(r"images\bomb_blue.svg")
        b_b = SVGItem(r"images\peace_blue.svg")
        s_b.points.scale(0.2).move_to(table.get_cell(0, 1))
        b_b.points.scale(0.2).move_to(table.get_cell(0, 2))
        s_r = SVGItem(r"images\bomb_red.svg")
        b_r = SVGItem(r"images\peace_red.svg")
        s_r.points.scale(0.2).move_to(table.get_cell(1, 0))
        b_r.points.scale(0.2).move_to(table.get_cell(2, 0))
        self.show(s_b, b_b, s_r, b_r)
        pm1 = Text("+10 -10")
        pm1.points.move_to(table.get_cell(1, 2).points.box.center).scale(1.5)
        for i in pm1[0][0:3]: 
            i.color.set(RED)
        for i in pm1[0][3:]: 
            i.color.set(BLUE)
        pm2 = Text("-10 +10")
        pm2.points.move_to(table.get_cell(2, 1).points.box.center).scale(1.5)
        for i in pm2[0][0:3]: 
            i.color.set(RED)
        for i in pm2[0][3:]: 
            i.color.set(BLUE)
        pm3 = Text("0 0")
        pm3.points.move_to(table.get_cell(2, 2).points.box.center).scale(1.5)
        for i in pm3[0][0:1]: 
            i.color.set(RED)
        for i in pm3[0][1:]: 
            i.color.set(BLUE)
        pm4 = Text("-1000 -1000")
        pm4.points.move_to(table.get_cell(1, 1).points.box.center).scale(1.5)
        for i in pm4[0][0:5]: 
            i.color.set(RED)
        for i in pm4[0][5:]: 
            i.color.set(BLUE)
        self.show(pm1, pm2, pm3, pm4)
        self.forward(4)
        def rec_anim(num, if_rol=True, run_time=1, pu=None):
            if if_rol:
                if pu != None:
                    def cl(i):
                        if i == pu:
                            return PURPLE
                        else:
                            return RED
                    self.play(AnimGroup(
                        *[table.get_cell(num, i).anim.fill.set(cl(i)) for i in range(3)],
                        duration=run_time
                    ))
                else:
                    self.play(AnimGroup(
                        *[table.get_cell(num, i).anim.fill.set(RED) for i in range(3)],
                        duration=run_time
                    ))
            else:
                if pu != None:
                    def cl(i):
                        if i == pu:
                            return PURPLE
                        else:
                            return BLUE
                    self.play(AnimGroup(
                        *[table.get_cell(i, num).anim.fill.set(cl(i)) for i in range(3)],
                        duration=run_time
                    ))
                else:
                    self.play(AnimGroup(
                        *[table.get_cell(i, num).anim.fill.set(BLUE) for i in range(3)],
                        duration=run_time
                    ))

        rec_anim(1, False)
        self.forward(2)
        rec_anim(1, True, 1, 1)
        self.forward(7)
        self.play(AnimGroup(
            table.get_cell(1, 0).anim.fill.set(BLACK),
            table.get_cell(1, 1).anim.fill.set(BLUE),
            table.get_cell(1, 2).anim.fill.set(BLACK),
            table.get_cell(2, 0).anim.fill.set(RED),
            table.get_cell(2, 1).anim.fill.set(PURPLE),
            table.get_cell(2, 2).anim.fill.set(RED),
        ))
        self.forward()
        self.play(AnimGroup(
            table.get_cell(0, 1).anim.fill.set(BLACK),
            table.get_cell(1, 1).anim.fill.set(BLACK),
            table.get_cell(2, 1).anim.fill.set(RED),
            table.get_cell(0, 2).anim.fill.set(BLUE),
            table.get_cell(1, 2).anim.fill.set(BLUE),
            table.get_cell(2, 2).anim.fill.set(PURPLE),
        ))
        self.forward(4)


class Demo4(Timeline):
    def construct(self):
        table = Table(3, 3, 2.2, 1, True)
        table.points.scale(1.5)
        self.show(table)
        ru = SVGItem(r"images\female.svg")
        pos = table.get_cell(0, 0).points.box.center
        ru.points.move_to(pos + DL*0.3 + LEFT*0.3).scale(3)
        us = SVGItem(r"images\male.svg")
        us.points.move_to(pos + UR*0.3 + RIGHT*0.3).scale(3)
        self.show(ru, us)
        s_b = SVGItem(r"images\angry_blue.svg")
        b_b = SVGItem(r"images\happy_blue.svg")
        s_b.points.scale(4).move_to(table.get_cell(0, 1))
        b_b.points.scale(4).move_to(table.get_cell(0, 2))
        s_r = SVGItem(r"images\angry_red.svg")
        b_r = SVGItem(r"images\happy_red.svg")
        s_r.points.scale(4).move_to(table.get_cell(1, 0))
        b_r.points.scale(4).move_to(table.get_cell(2, 0))
        self.show(s_b, b_b, s_r, b_r)
        pm1 = Text("+10 -10")
        pm1.points.move_to(table.get_cell(1, 2).points.box.center).scale(1.5)
        for i in pm1[0][0:3]: 
            i.color.set(RED)
        for i in pm1[0][3:]: 
            i.color.set(BLUE)
        pm2 = Text("-10 +10")
        pm2.points.move_to(table.get_cell(2, 1).points.box.center).scale(1.5)
        for i in pm2[0][0:3]: 
            i.color.set(RED)
        for i in pm2[0][3:]: 
            i.color.set(BLUE)
        pm3 = Text("0 0")
        pm3.points.move_to(table.get_cell(2, 2).points.box.center).scale(1.5)
        for i in pm3[0][0:1]: 
            i.color.set(RED)
        for i in pm3[0][1:]: 
            i.color.set(BLUE)
        pm4 = Text("-1000 -1000")
        pm4.points.move_to(table.get_cell(1, 1).points.box.center).scale(1.5)
        for i in pm4[0][0:5]: 
            i.color.set(RED)
        for i in pm4[0][5:]: 
            i.color.set(BLUE)
        self.show(pm1, pm2, pm3, pm4)
        self.forward(4)
        straight_b = SVGItem(r"images\straight_blue.svg")
        straight_r = SVGItem(r"images\straight_red.svg")
        back_b = SVGItem(r"images\back_blue.svg")
        back_r = SVGItem(r"images\back_red.svg")
        straight_b.points.scale(4).move_to(table.get_cell(0, 1))
        straight_r.points.scale(4).move_to(table.get_cell(1, 0))
        back_b.points.scale(4).move_to(table.get_cell(0, 2))
        back_r.points.scale(4).move_to(table.get_cell(2, 0))

        for _ in range(4):
            self.play(Indicate(s_b))
        self.forward()
        for _ in range(3):
            self.play(Indicate(s_r))
        self.forward(1)
        self.play(FadeTransform(s_b, straight_b), FadeTransform(s_r, straight_r))
        self.forward(0.5)
        self.play(FadeTransform(straight_b, s_b), FadeTransform(straight_r, s_r))
        self.play(FadeTransform(b_b, back_b), FadeTransform(b_r, back_r))
        self.forward(1)
        self.play(FadeTransform(back_b, b_b), FadeTransform(back_r, b_r))
        self.forward(1)

        self.prepare(
            table.get_cell(1, 0).anim.fill.set(RED),
            table.get_cell(1, 1).anim.fill.set(PURPLE),
            table.get_cell(1, 2).anim.fill.set(RED),
            table.get_cell(0, 1).anim.fill.set(BLUE),
            table.get_cell(2, 1).anim.fill.set(BLUE),
            duration=8
        )
        for _ in range(8):
            self.play(AnimGroup(
                Indicate(s_r), 
                Indicate(s_b)
            ))
        h_b = SVGItem(r"images\heart_blue.svg")
        h_r = SVGItem(r"images\heart_red.svg")
        h_b.points.scale(3).move_to(us).shift(UP)
        h_r.points.scale(3).move_to(ru).shift(LEFT*1.7)
        self.play(FadeIn(h_b), FadeIn(h_r))
        cry1 = ImageItem(r"images\cry.png")
        cry2 = ImageItem(r"images\cry.png")
        cry1.points.move_to(s_r).scale(0.3)
        cry2.points.move_to(s_b).scale(0.3)
        self.play(FadeTransform(s_r, cry1), FadeTransform(s_b, cry2))
        self.forward(3)


class Demo5(Timeline):
    def construct(self):
        table = Table(3, 3, 2.2, 1, True)
        table.points.scale(1.5)
        self.show(table)
        a = Text("A", color=RED)
        pos = table.get_cell(0, 0).points.box.center
        a.points.move_to(pos + DL*0.3).scale(1.5)
        b = Text("B", color=BLUE)
        b.points.move_to(pos + UR*0.3).scale(1.5)
        self.show(a, b)
        s_b = SVGItem(r"images\straight_blue.svg")
        b_b = SVGItem(r"images\back_blue.svg")
        s_b.points.scale(3).move_to(table.get_cell(0, 1))
        b_b.points.scale(3).move_to(table.get_cell(0, 2))
        s_r = SVGItem(r"images\straight_red.svg")
        b_r = SVGItem(r"images\back_red.svg")
        s_r.points.scale(3).move_to(table.get_cell(1, 0))
        b_r.points.scale(3).move_to(table.get_cell(2, 0))
        self.show(s_b, b_b, s_r, b_r)
        pm1 = Text("+10 -10")
        pm1.points.move_to(table.get_cell(1, 2).points.box.center).scale(1.5)
        for i in pm1[0][0:3]: 
            i.color.set(RED)
        for i in pm1[0][3:]: 
            i.color.set(BLUE)
        pm2 = Text("-10 +10")
        pm2.points.move_to(table.get_cell(2, 1).points.box.center).scale(1.5)
        for i in pm2[0][0:3]: 
            i.color.set(RED)
        for i in pm2[0][3:]: 
            i.color.set(BLUE)
        pm3 = Text("0 0")
        pm3.points.move_to(table.get_cell(2, 2).points.box.center).scale(1.5)
        for i in pm3[0][0:1]: 
            i.color.set(RED)
        for i in pm3[0][1:]: 
            i.color.set(BLUE)
        pm4 = Text("-1000 -1000")
        pm4.points.move_to(table.get_cell(1, 1).points.box.center).scale(1.5)
        for i in pm4[0][0:5]: 
            i.color.set(RED)
        for i in pm4[0][5:]: 
            i.color.set(BLUE)
        self.show(pm1, pm2, pm3, pm4)
        self.forward(2)
        self.play(
            table.get_cell(2, 0).anim.fill.set(RED),
            table.get_cell(2, 1).anim.fill.set(RED),
            table.get_cell(2, 2).anim.fill.set(PURPLE),
            table.get_cell(0, 2).anim.fill.set(BLUE),
            table.get_cell(1, 2).anim.fill.set(BLUE),
        )
        self.forward(3)
        gantan = ImageItem(r"images\!.png")
        rect1 = SurroundingRect(pm3[0][0], buff=0.1)
        rect2 = SurroundingRect(pm1[0][0:3], buff=0.1)
        gantan.points.move_to(a).shift(LEFT*0.7 + UP*0.2).scale(0.3)
        self.play(FadeInFromPoint(gantan, a.points.box.center), FadeIn(rect1))
        self.forward()
        self.play(FadeOutToPoint(gantan, a.points.box.center))
        self.play(
            table.get_cell(2, 0).anim.fill.set(BLACK),
            table.get_cell(2, 1).anim.fill.set(BLACK),
            table.get_cell(2, 2).anim.fill.set(BLUE),
            table.get_cell(1, 0).anim.fill.set(RED),
            table.get_cell(1, 1).anim.fill.set(RED),
            table.get_cell(1, 2).anim.fill.set(PURPLE),
            Transform(rect1, rect2)
        )
        self.forward(1)
        self.play(FadeOut(rect2))
        self.forward(2)
        rect3 = SurroundingRect(pm1[0][4:], buff=0.1)
        rect4 = SurroundingRect(pm4[0][6:], buff=0.1)
        self.play(FadeIn(rect3))
        self.play(
            table.get_cell(0, 2).anim.fill.set(BLACK),
            table.get_cell(1, 2).anim.fill.set(RED),
            table.get_cell(2, 2).anim.fill.set(BLACK),
            table.get_cell(0, 1).anim.fill.set(BLUE),
            table.get_cell(1, 1).anim.fill.set(PURPLE),
            table.get_cell(2, 1).anim.fill.set(BLUE),
            Transform(rect3, rect4),
        )
        self.play(
            table.get_cell(0, 2).anim.fill.set(BLUE),
            table.get_cell(1, 2).anim.fill.set(PURPLE),
            table.get_cell(2, 2).anim.fill.set(BLUE),
            table.get_cell(0, 1).anim.fill.set(BLACK),
            table.get_cell(1, 1).anim.fill.set(RED),
            table.get_cell(2, 1).anim.fill.set(BLACK),
            Transform(rect4, rect3),
        )
        self.play(
            table.get_cell(0, 2).anim.fill.set(BLACK),
            table.get_cell(1, 2).anim.fill.set(RED),
            table.get_cell(2, 2).anim.fill.set(BLACK),
            table.get_cell(0, 1).anim.fill.set(BLUE),
            table.get_cell(1, 1).anim.fill.set(PURPLE),
            table.get_cell(2, 1).anim.fill.set(BLUE),
            Transform(rect3, rect4),
        )
        self.play(
            table.get_cell(0, 2).anim.fill.set(BLUE),
            table.get_cell(1, 2).anim.fill.set(PURPLE),
            table.get_cell(2, 2).anim.fill.set(BLUE),
            table.get_cell(0, 1).anim.fill.set(BLACK),
            table.get_cell(1, 1).anim.fill.set(RED),
            table.get_cell(2, 1).anim.fill.set(BLACK),
            Transform(rect4, rect3),
        )
        self.forward(1)
        self.play(FadeOut(rect3))
        self.forward(2)
        devil1 = SVGItem(r"images\devil.svg")
        devil2 = ImageItem(r"images\devil2.png")
        devil1.points.move_to(a).shift(LEFT*0.7).scale(3)
        self.play(FadeIn(devil1))
        self.forward(5)
        devil2.points.move_to(b).shift(RIGHT*0.7).scale(0.2)
        self.play(FadeIn(devil2))
        rect5 = SurroundingRect(pm4[0][0:5], buff=0.1)
        rect6 = SurroundingRect(pm2[0][0:3], buff=0.1)
        self.play(
            table.get_cell(0, 2).anim.fill.set(BLACK),
            table.get_cell(1, 2).anim.fill.set(RED),
            table.get_cell(2, 2).anim.fill.set(BLACK),
            table.get_cell(0, 1).anim.fill.set(BLUE),
            table.get_cell(1, 1).anim.fill.set(PURPLE),
            table.get_cell(2, 1).anim.fill.set(BLUE),
        )
        self.play(FadeIn(rect5))
        self.forward(3)
        self.play(
            table.get_cell(2, 0).anim.fill.set(RED),
            table.get_cell(2, 1).anim.fill.set(PURPLE),
            table.get_cell(2, 2).anim.fill.set(RED),
            table.get_cell(1, 0).anim.fill.set(BLACK),
            table.get_cell(1, 1).anim.fill.set(BLUE),
            table.get_cell(1, 2).anim.fill.set(BLACK),
            Transform(rect5, rect6),
        )
        self.play(
            table.get_cell(2, 0).anim.fill.set(BLACK),
            table.get_cell(2, 1).anim.fill.set(BLUE),
            table.get_cell(2, 2).anim.fill.set(BLACK),
            table.get_cell(1, 0).anim.fill.set(RED),
            table.get_cell(1, 1).anim.fill.set(PURPLE),
            table.get_cell(1, 2).anim.fill.set(RED),
            Transform(rect6, rect5),
        )
        self.play(
            table.get_cell(2, 0).anim.fill.set(RED),
            table.get_cell(2, 1).anim.fill.set(PURPLE),
            table.get_cell(2, 2).anim.fill.set(RED),
            table.get_cell(1, 0).anim.fill.set(BLACK),
            table.get_cell(1, 1).anim.fill.set(BLUE),
            table.get_cell(1, 2).anim.fill.set(BLACK),
            Transform(rect5, rect6),
        )
        self.play(
            table.get_cell(2, 0).anim.fill.set(BLACK),
            table.get_cell(2, 1).anim.fill.set(BLUE),
            table.get_cell(2, 2).anim.fill.set(BLACK),
            table.get_cell(1, 0).anim.fill.set(RED),
            table.get_cell(1, 1).anim.fill.set(PURPLE),
            table.get_cell(1, 2).anim.fill.set(RED),
            Transform(rect6, rect5),
        )
        self.forward(1)
        self.play(FadeOut(rect5))
        self.forward(1)
        death1 = SVGItem(r"images\death.svg")
        death2 = SVGItem(r"images\death.svg")
        death1.points.move_to(devil1).scale(3)
        death2.points.move_to(devil2).scale(3)
        self.play(FadeTransform(devil1, death1), FadeTransform(devil2, death2))
        self.forward(5)
