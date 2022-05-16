import tkinter as tk
import Utility as ut
from Presentation import Presentation
from Rectangle import Rectangle
from Text import Text
from Image import Image

class Flow:
    def start(self, canvas: Presentation):
        self.canvas = canvas
        self.canvas.configure(bg='#000011')
        self.main_image = Image(canvas, 0, 0, 1280, 720, "images/start.jpeg", hide=False)
        self.climate_change_text = Text(canvas, 0, 0, "Climate Change Informer", size=-50, color="white", bold=True)
        self.climate_change_text = Rectangle(canvas, -200, 150, 600, 80, text=self.climate_change_text, transparency=0.6)
        self.climate_change_text.move_easeinout_to(self.climate_change_text.get_h_centre(), show=True)
        self.start_button = Text(canvas, 0, 0, "Start!", size=-30, bold=True)
        self.start_button = Rectangle(canvas, 0, 720, 125, 75, text=self.start_button, fill="white", transparency=0.6, onclick=self.s1)
        self.start_button.move(*self.start_button.get_h_centre())
        self.start_button.move_easeinout_to(self.start_button.get_vh_centre(), show=True)

    def s1(self, _):
        self.main_image.unload()
        self.climate_change_text.unload()
        self.start_button.unload()

        self.s1_title = Text(self.canvas, -400, 50, "What Is Climate Change?", size=-50, color="white", bold=True)
        self.s1_title.move_easeinout_to(self.s1_title.get_h_centre(), show=True)
        self.s1_text = Text(self.canvas, -400, 0,
"""Climate change is the long-term
change of temperature and weather
patterns worldwide"""
        , color="white", size=-30)
        self.s1_text.move(*self.s1_text.get_v_centre())
        self.s1_text.move_easeinout_to((40, self.s1_text.get_h_centre()[1]), show=True)
        self.s1_image = Image(self.canvas, 1280, 0, 750, 400, "images/s1_img.jpg")
        self.s1_image.move(*self.s1_image.get_v_centre())
        self.s1_image.move_easeinout_to((600, self.s1_image.get_h_centre()[1]), show=True)
        self.s1_next_button = Text(self.canvas, 0, 0, "Continue", bold=True)
        self.s1_next_button = Rectangle(self.canvas, 1280, 720, 100, 40, text=self.s1_next_button, fill="white", onclick=self.s2)
        self.s1_next_button.move_easeinout_to((1180, 680), show=True)

    def s2(self, _):
        self.s1_title.unload()
        self.s1_text.unload()
        self.s1_image.unload()
        self.s1_next_button.unload()
        
        self.s2_title = Text(self.canvas, -400, 50, "What Causes Climate Change?", size=-50, color="white", bold=True)
        self.s2_title.move_easeinout_to(self.s2_title.get_h_centre(), show=True)
        self.s2_text = Text(self.canvas, -400, 0,
"""There is a multitude of things
that cause climate change, here
are some:
- Burning fossil fuels
  - Transport
  - Factories
  - Power plants
- Farming livestock
- Volcanic Activity
- Cutting down forests"""
        , color="white", size=-30)
        self.s2_text.move(*self.s2_text.get_v_centre())
        self.s2_text.move_easeinout_to((40, self.s2_text.get_h_centre()[1]), show=True)
        self.s2_image = Image(self.canvas, 1280, 0, 750, 400, "images/s2_img.jpg")
        self.s2_image.move(*self.s2_image.get_v_centre())
        self.s2_image.move_easeinout_to((600, self.s2_image.get_h_centre()[1]), show=True)
        self.s2_next_button = Text(self.canvas, 0, 0, "Continue", bold=True)
        self.s2_next_button = Rectangle(self.canvas, 1280, 720, 100, 40, text=self.s2_next_button, fill="white", onclick=self.s3)
        self.s2_next_button.move_easeinout_to((1180, 680), show=True)

    def s3(self, _):
        self.s2_title.unload()
        self.s2_text.unload()
        self.s2_image.unload()
        self.s2_next_button.unload()
        
        self.s3_title = Text(self.canvas, -400, 50, "What Are The Results Of Climate Change?", size=-50, color="white", bold=True)
        self.s3_title.move_easeinout_to(self.s3_title.get_h_centre(), show=True)
        self.s3_text = Text(self.canvas, -400, 0,
"""Climate change causes way to
much damage for what it's worth,
here's some of what the results
are:
- Glaciers melt
  - Rising sea levels
    - Flooding
- Heat waves
- Drought
- Warming oceans
- Animals harmed
- More common extreme weather"""
        , color="white", size=-30)
        self.s3_text.move(*self.s3_text.get_v_centre())
        self.s3_text.move_easeinout_to((40, self.s3_text.get_h_centre()[1]), show=True)
        self.s3_image = Image(self.canvas, 1280, 0, 600, 450, "images/s3_img.jpg")
        self.s3_image.move(*self.s3_image.get_v_centre())
        self.s3_image.move_easeinout_to((600, self.s3_image.get_h_centre()[1]), show=True)
        self.s3_next_button = Text(self.canvas, 0, 0, "Continue", bold=True)
        self.s3_next_button = Rectangle(self.canvas, 1280, 720, 100, 40, text=self.s3_next_button, fill="white", onclick=self.s4)
        self.s3_next_button.move_easeinout_to((1180, 680), show=True)

    def s4(self, _):
        exit()