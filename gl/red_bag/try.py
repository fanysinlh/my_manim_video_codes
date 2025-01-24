from manimlib import *
from random import random, seed
from time import time

class RedBagRain(Scene):
    def construct(self):
        seed(time())
        print(time())
        PMNUM = 10
        RBNUM = 200
        pm = ImageMobject("./assets/paimeng.png").scale(0.5)
        red_bag = Rectangle(color=RED, fill_opacity=1, stroke_color=WHITE).scale(0.3).rotate(70*DEGREES)
        width, height = FRAME_WIDTH, FRAME_HEIGHT
        pmrd = [((random() - 0.5)*(width - pm.get_width()), (random() - 0.5)*(height - pm.get_height()), 0) for _ in range(PMNUM)]
        pms = Group(*[pm.copy().move_to(pmrd[i]) for i in range(PMNUM)])
        self.add(pms)
        k1 = SurroundingRectangle(pms[0], color=YELLOW)
        k2 = SurroundingRectangle(pms[9], color=RED)
        self.add(k1, k2)
