from manimlib import *

class Try(Scene):
    def construct(self):
        t = Tex("niumo")
        self.play(FadeIn(t))
        self.embed()
