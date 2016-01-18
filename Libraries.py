# Simple example of using a library to generate a graph

import plotly as py
import plotly.graph_objs as go

data1 = go.Bar(
        x=['python','javascript','ruby'],
        y=[160,250,190],
        name='US'
)

data2 = go.Bar(
        x=['python','javascript','ruby'],
        y=[350,50,220],
        name='EU'
)

data = [ data1, data2 ]
layout = go.Layout(
    barmode = 'group'
)

fig = go.Figure(data = data, layout=layout)

py.offline.plot(data)
