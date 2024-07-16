# Import the dependencies.
import numpy as np
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

# Uncomment to deploy Flask on VS CODE
engine = create_engine("sqlite:///Surfsup/Resources/hawaii.sqlite")

# Uncomment deploy Flask on Terminal
# engine = create_engine("sqlite:///../SurfsUp/Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# View all of the classes that automap found
Base.classes.keys()#

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
                <title>Welcome to The Hawaii Weather Climate API</title>
            </head>
            <body>
                <h1>Welcome to The Hawaii Weather Climate API!</h1>
                <h2>Available Routes:</h2>
                <ul>
                    <li><a href="/">home</a></li>
                    <li><a href="/api/v1.0/precipitation">precipitation</a></li>
                    <li><a href="/api/v1.0/station">stations</a></li>
                    <li><a href="/api/v1.0/tobs">tobs</a></li>
                    <li><a href="/api/v1.0/start">start</a></li>
                    <li><a href="/api/v1.0/start_end">start/end</a></li>
                </ul>
            </body>
        </html>
    """)

# Define the precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Find the most recent date in the dataset
    latest_date = session.query(func.max(Measurement.date)).scalar()

    # Calculate the date one year from the last date in data set.
    one_year_ago = dt.datetime.strptime(latest_date, '%Y-%m-%d') - dt.timedelta(days=365)

    # Save the query results. 
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_ago).all()
    
    session.close()
    
    # Create a dictionary from the row data and append to a list
    precipitation_data = []
    for date, precip in results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["precipitation"] = precip
        precipitation_data.append(precipitation_dict)
    
    return jsonify(precipitation_data)  

# Run the Flask app in debug mode
if __name__ == '__main__':
    app.run(debug=True)