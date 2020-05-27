import os
from gerber import PCB
from gerber.render.theme import *
from gerber.render.cairo_backend import GerberCairoContext


GERBER_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'gerbers'))


# Create a new drawing context
ctx = GerberCairoContext()

# Create a new PCB instance
pcb = PCB.from_directory(GERBER_FOLDER)

# Render PCB top view
ctx.render_layers(
					pcb.top_layers,
                	os.path.join(os.path.dirname(__file__), 'Redpcb_top.png',),
                	Theme(name='Red',
                	topmask=RenderSettings(COLORS['red'], alpha=0.8, invert=True),
                	bottommask=RenderSettings(COLORS['red'], alpha=0.8, invert=True)),
                	max_width=800, max_height=600)

# Render PCB bottom view
ctx.render_layers(pcb.bottom_layers,
                  os.path.join(os.path.dirname(__file__), 'Redpcb_bottom.png'),
                  Theme(name='Red',
                  topmask=RenderSettings(COLORS['red'], alpha=0.8, invert=True),
                  bottommask=RenderSettings(COLORS['red'], alpha=0.8, invert=True)
                  ), max_width=800, max_height=600)

# Render copper layers only
ctx.render_layers(pcb.copper_layers + pcb.drill_layers,
                  os.path.join(os.path.dirname(__file__),
                               'pcb.png'),
                  THEMES['Transparent Copper'], max_width=800, max_height=600)