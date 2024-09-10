from manim import *

class HXJBrace(Brace):
    def get_tex(self, *text, **kwargs):
        text_mob = MathTex(*text, **kwargs)
        self.put_at_tip(text_mob)
        return text_mob

class Try(Scene):
    def construct(self):
        mvtpoint = Text("move_to([1, 1, 0])", font="Courier New", font_size=24, t2c={
            "move_to": YELLOW,
            "(": YELLOW,
            "[1, 1, 0]": GREEN,
            ")": YELLOW,
        })
        self.add(mvtpoint, index_labels(mvtpoint))

class TryWrite(Scene):
    def construct(self):
        tx = Text("niumo", font_size=144)
        self.play(Write(tx))