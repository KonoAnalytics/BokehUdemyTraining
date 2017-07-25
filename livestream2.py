from bokeh.io import curdoc
from bokeh.models import ColumnDataSource, DatetimeTickFormatter
from bokeh.plotting import figure

import requests
from bs4 import BeautifulSoup
from datetime import datetime
from math import radians

#create webscraping function
def extract_value():
    r = requests.get("https://bitcoincharts.com/markets/coincheckJPY.html",headers={'User-Agent':'Mozilla/5.0'})
    soup = BeautifulSoup(r.content,'html.parser')
    value_raw = soup.find_all("p")
    value_net = float(value_raw[0].span.text)
    return value_net

#create figure
f=figure()

source = ColumnDataSource(dict(x=[],y=[]))

f.circle(x='x',y='y',color='olive',line_color='brown',source=source)
f.line(x='x',y='y', color='green', source=source)


#create periodic function
def update():
    new_data=dict(x=[datetime.now()], y=[extract_value()])
    source.stream(new_data, rollover=200)
    #print(source.data)

f.xaxis.formatter = DatetimeTickFormatter(
    seconds=["%Y-%m-%d %H:%M:%S %Z"],
    minsec=["%Y-%m-%d %H:%M:%S %Z"],
    minutes=["%Y-%m-%d %H:%M:%S %Z"],
    hourmin=["%Y-%m-%d %H:%M:%S %Z"],
    hours=["%Y-%m-%d %H:%M:%S %Z"],
    days=["%Y-%m-%d %H:%M:%S %Z"],
    months=["%Y-%m-%d %H:%M:%S %Z"],
    years=["%Y-%m-%d %H:%M:%S %Z"]
)


f.xaxis.major_label_orientation=radians(90)

#add figure to curdoc and configure callback
curdoc().add_root(f)
curdoc().add_periodic_callback(update,500)