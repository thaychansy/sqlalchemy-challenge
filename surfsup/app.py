# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
# Create an engine that connects to the SQLite database
#################################################
#################################################
engine = create_engine("sqlite:///surfsup/resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# View all of the classes that automap found
Base.classes.keys()

# Save references to each table
Measurement = Base.classes.measurement

Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Define the root route
@app.route("/")
def home():
    return (f"""
        <html>
            <head>
                <title>Welcome to Hawaii Weather Climate API</title>
            </head>
            <body>
                <h1>Welcome to Hawaii Weather Climate API!</h1>
                <h2>Available Routes:</h2>
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/api/v1.0/precipitation">Precipitation</a></li>
                    <li><a href="/api/v1.0/station">Station</a></li>
                    <li><a href="/api/v1.0/tobs">TOBS</a></li>
                </ul>
            </body>
        </html>
    """)

# Run the Flask app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
