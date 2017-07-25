from bokeh.io import curdoc
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

from random import randrange

#create figure
f=figure(x_range=(0,11), y_range=(0,11))

source = ColumnDataSource(dict(x=[],y=[]))

f.circle(x='x',y='y',color='olive',line_color='brown',source=source)
f.line(x='x',y='y', color='green', source=source)

#create periodic function
def update():
    new_data=dict(x=[randrange(1,10)], y=[randrange(1,10)])
    source.stream(new_data, rollover=15)
    print(source.data)

#add figure to curdoc and configure callback
curdoc().add_root(f)
curdoc().add_periodic_callback(update,1000)