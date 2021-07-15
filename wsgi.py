from flask import Flask, render_template
from services import azure
from collections import Counter
app = Flask(__name__)

@app.route("/")
def hello_world():
    columns, data = azure.request()
    return render_template('hello.html', columns=columns, data=data)

@app.route('/pie')
def pie_chart():
    _, data = azure.request()
    
    workitems = [ d['fields']['System.WorkItemType'] for d in data['value'] ]
    count = Counter(workitems)
    return render_template('pie.html', columns=list(set(workitems)), count=list(count.values()))