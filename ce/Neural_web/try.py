from manim import *
from utils import *
from manim_ml.neural_network import NeuralNetwork, FeedForwardLayer

class Try(Scene):
    def construct(self):
        rec1 = Rectangle(width=4, height=4, color=YELLOW)
        rec2 = rec1.copy()
        VGroup(rec1, rec2).arrange(RIGHT, buff=2)
        self.add(rec1, rec2)
        nnn1 = NeuralNetwork([
            FeedForwardLayer(num_nodes=1, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
            FeedForwardLayer(num_nodes=5, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
            FeedForwardLayer(num_nodes=5, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
            FeedForwardLayer(num_nodes=1, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
        ], layer_spacing=0.7).rotate(PI/2).scale_to_fit_height(3.5).move_to(rec1)
        nnn2 = NeuralNetwork([
            FeedForwardLayer(num_nodes=4, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
            FeedForwardLayer(num_nodes=5, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
            FeedForwardLayer(num_nodes=5, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
            FeedForwardLayer(num_nodes=1, node_radius=0.42, node_color=YELLOW, node_spacing=1, node_stroke_width=4, animation_dot_color=PINK),
        ], layer_spacing=0.7).rotate(PI/2).scale_to_fit_height(3.5).move_to(rec2)
        self.add(nnn1, nnn2)
