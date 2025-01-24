from typing import Sequence
from manim import *
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


class Try(Scene):
    def construct(self):
        s = Square()
        self.wait()
        self.play(Create(s))
        self.wait()
        self.play(RotateWithMove(s, 90*DEGREES, RIGHT*3+ UP*2))
        self.wait()