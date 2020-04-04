from dswebapp import app

from flask import render_template
import time

import plotly.graph_objs as go 
import plotly, json

data = [('United States', [1990,2015],[24.7,18.383])]
country = data[0][0]

graph_one= [go.Scatter(
    x = data[0][1],
    y = data[0][2],
    mode = 'lines',
    name = country
)]

layout_one = dict(title="Change in Hectares Arable Land <br> per Person 1990 to 2015",
    xaxis = dict(title="Year",
    autotick=False, tick0=1990, dtick=25),
    yaxis = dict(title='Hectacres')    
)

figures = []
figures.append(dict(data=graph_one, layout=layout_one))

ids = ['figure-{}'.format(i) for i,_ in enumerate(figures)]

figuresJSON = json.dumps(figures,cls=plotly.utils.PlotlyJSONEncoder)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', ids=ids, figuresJSON=figuresJSON)

@app.route('/project-one')
def project_one():
    return render_template('project_one.html')