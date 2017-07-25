from bokeh.io import output_file, show
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool
)

from random import random

map_options = GMapOptions(lat=29.7604, lng=-95.3698, map_type="roadmap", zoom=11)

plot = GMapPlot(
    x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options
)
plot.title.text = "Houston"

# For GMaps to function, Google requires you obtain and enable an API key:
#
#     https://developers.google.com/maps/documentation/javascript/get-api-key
#
# Replace the value below with your personal API key:
plot.api_key = "AIzaSyCQDqp4C_sUJ3avHizALfpoVIQtgDJuh6E"

latitude1 = []
longitude1 = []
latitude2 = []
longitude2 = []

for i in range(100):
    latitude1.append((random()-.55)/2 + 29.7604)
    longitude1.append((random()-.45)/2 - 95.369)
    latitude2.append((random()-.5)/2 + 29.7604)
    longitude2.append((random()-.5)/2 - 95.369)

source1 = ColumnDataSource(
    data=dict(
        lat=latitude1,
        lon=longitude1,
    )
)
circle1 = Circle(x="lon", y="lat", size=10, fill_color="blue", fill_alpha=0.8, line_color=None)

source2 = ColumnDataSource(
    data=dict(
        lat=latitude2,
        lon=longitude2,
    )
)

circle2 = Circle(x="lon", y="lat", size=10, fill_color="red", fill_alpha=0.8, line_color=None)

plot.add_glyph(source1, circle1)
plot.add_glyph(source2, circle2)

plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
output_file("gmap_plot.html")
show(plot)