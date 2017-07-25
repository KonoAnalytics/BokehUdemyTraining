from bokeh.plotting import figure
from bokeh.io import curdoc
from bokeh.models.annotations import LabelSet
from bokeh.models import ColumnDataSource, Range1d
from bokeh.models.widgets import Select, Slider, RadioButtonGroup
from bokeh.layouts import layout

# Source Data

source_original = ColumnDataSource(dict(average_grades=[7,8,10],
                             exam_grades=[6,9,8],
                             student_names=["Stephan","Helder","Riazudidn"]))

source = ColumnDataSource(dict(average_grades=[7,8,10],
                             exam_grades=[6,9,8],
                             student_names=["Stephan","Helder","Riazudidn"]))

# create a figure
f = figure(x_range=Range1d(start=0, end=12),
            y_range=Range1d(start=0, end=12))


# add labels for glyphs (need column datasource)
labels=LabelSet(x="average_grades", y = "exam_grades", text="student_names", x_offset=5, y_offset = 5, source=source)
f.add_layout(labels)

#create glyphs
f.circle(x="average_grades", y="exam_grades", source = source, size=4)

#create filtering function
def filter_grades(attr,old,new):
    source.data = {key:[value for i, value in enumerate(source_original.data[key]) if source_original.data["exam_grades"][i]>=slider.value] for key in
                   source_original.data}
    print(slider.value)

#create label function
def update_labels(attr,old,new):
    labels.text = options[radio_button_group.active]


#create select widget
options = ["average_grades","exam_grades","student_names"]
radio_button_group = RadioButtonGroup(labels=options)
radio_button_group.on_change("active",update_labels)

slider = Slider(start=min(source_original.data["exam_grades"])-1,
                end=max(source_original.data["exam_grades"])+1,
                step=0.1,
                title="Exam Grade: ")

slider.on_change("value",filter_grades)


#create layout and add to curdoc
lay_out = layout([[radio_button_group],[slider]])
curdoc().add_root(f)
curdoc().add_root(lay_out)
