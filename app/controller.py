from app import app 
from flask import render_template, request, redirect
from app.models.add_event import *
from app.models.event import *

@app.route('/')
def index():
    return render_template("index.html", title="Home", events=events)
    


