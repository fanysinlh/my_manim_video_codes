from manim import *

class Try(Scene):
    def construct(self):
        ax = NumberPlane()
        c = Circle(radius=1).move_to(LEFT)
        self.add(ax)
        self.play(Create(c))
        line = Line(ORIGIN, ORIGIN, color=YELLOW)
        self.add(line)
        now_t = self.renderer.time
        def line_up(mob: Line):
            t = self.renderer.time
            mob.put_start_and_end_on(ORIGIN, (np.cos(t - now_t) - 1)*RIGHT + np.sin(t - now_t)*UP)
        line.add_updater(line_up)
        line2 = line.copy().set_color(GREEN)
        self.add(line2)
        def line2_up(mob: Line):
            length = line.get_length()**0.5
            e = line.get_end()
            if not e.any():
                theta = 0
            elif np.arctan(e[1]/e[0]) < PI/2:
                theta = (np.arctan(e[1]/e[0]) + PI)/2
            elif np.arctan(e[1]/e[0]) > 3*PI/2:
                theta = (np.arctan(e[1]/e[0]) - PI)/2
            else:
                theta = np.arctan(e[1]/e[0])/2
            dot = np.array([length*np.cos(theta), length*np.sin(theta), 0])
            mob.put_start_and_end_on(-dot, dot)
            self.add(Dot(mob.get_end(), radius=0.02), Dot(mob.get_start(), radius=0.02))
        line2.add_updater(line2_up)
        self.wait(10, frozen_frame=False)
