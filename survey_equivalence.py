#!/usr/bin/env python
import os
from manimlib.imports import *
from manimlib.constants import *

CURR_DIR = os.path.dirname(os.path.realpath(__file__))

class Urn():
    def __init__(self, scene, num_labels=10, num_blue=5):
        self.scene = scene
        self.blue_squares = [Label(label=True, side_length=1) for _ in range(num_blue)]
        pos = LEFT_SIDE + 0.5*RIGHT
        for sq in self.blue_squares:
            sq.move_to(pos)
            pos = pos + RIGHT
        self.maize_squares = [Label(label=False, side_length=1) for _ in range(num_labels - num_blue)]
        pos = LEFT_SIDE + UP + 0.5*RIGHT
        for sq in self.maize_squares:
            sq.move_to(pos)
            pos = pos + RIGHT + OUT

    def move_random_label(self):
        label_to_move = random.choice(self.all_objects)
        label_to_move.shift(3* RIGHT + 3 * UP)



    @property
    def all_objects(self):
        return self.blue_squares + self.maize_squares

    @property
    def all_manim_objects(self):
        retval = []
        for obj in self.all_objects:
            retval += obj.objects
        return retval

    def show(self):
        self.scene.add(*(self.all_manim_objects))
        for label in self.blue_squares + self.maize_squares:
            label.fade(self.scene)

class Label():
    def __init__(self, label=True, **kwargs):
        if label:
            color = COLOR_MAP['DARK_BLUE']
            txt = 'C'
        else:
            color = COLOR_MAP['GOLD_A']
            txt = 'D'
        self.square = Square(side_length = 1, color=color, fill_opacity=.6)
        self.txt = TextMobject(txt)

    @property
    def objects(self):
        return self.square, self.txt

    def move_to(self, vec):
        self.square.move_to(vec)
        self.txt.move_to(vec)

    def shift(self, vec):
        self.square.move_to(vec)
        self.txt.move_to(vec)

    def fade(self, scene):
        scene.play(FadeOut(self.txt), FadeOut(self.square))
        # self.play(FadeOut(sq))




class Main(Scene):



    def construct(self):
        ## start with full urn or urns
        labels = Urn(scene=self, num_labels=10, num_blue=5)
        labels.show()
        labels.move_random_label()





        ## take one ball out, by making a copy of one, not changing the static urn

        ## put it in the empty slot in the rating matrix W

        ## take another ball out

        ## speed up, taking t
