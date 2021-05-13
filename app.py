from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

# route 
@app.route("/")
def index()
