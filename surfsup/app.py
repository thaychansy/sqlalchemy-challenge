# Import the dependencies.
import numpy as np
import pandas as pd
from datetime import date
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

################################################
# Uncomment to deploy Flask in VS CODE
# engine = create_engine("sqlite:///Surfsup/Resources/hawaii.sqlite")

################################################
# Uncomment to deploy Flask in Terminal
engine = create_engine("sqlite:///../SurfsUp/Resources/hawaii.sqlite")
################################################

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
# Define functions
#################################################

# Define function for passing most recent date 
def get_most_recent_date(session):

    # Retrieve latest date
    most_recent_date = session.query(func.max(Measurement.date)).first()

    return most_recent_date

# Define function for passing oldest date 
def get_oldest_date(session):

    # Retrieve oldest date
    oldest_date = session.query(func.min(Measurement.date)).first()

    return oldest_date

    # Retrieve latest date
    most_recent_date = session.query(func.max(Measurement.date)).first()

    return most_recent_date

# Define function for passing latest date and past 12 months from the latest date
def get_one_year_from_latest(session):

    # Retrieve latest date
    latest_date = session.query(func.max(Measurement.date)).scalar()

    # Retrieve past 12 months of data from latest date
    one_year_ago =  dt.datetime.strptime(latest_date, '%Y-%m-%d') - dt.timedelta(days=365)
    
    return one_year_ago

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# Define the root route
@app.route("/")
def home():  # sourcery skip: remove-redundant-fstring
    return (f"""
        <html>
            <head>
                <title>Welcome to The Hawaii Weather API & Climate APP</title>
            </head>
            <body>
                <h1>Welcome to The Hawaii Weather API & Climate APP!</h1>
                <h2>Available Routes:</h2>
                <ul>
                    <li><a href="/">home</a></li>
                    <li><a href="/api/v1.0/precipitation">precipitation</a></li>
                    <li><a href="/api/v1.0/stations">stations</a></li>
                    <li><a href="/api/v1.0/tobs">tobs</a></li>
                    <li><a href="/api/v1.0/start/<start>">start</a></li>
                    <li><a href="/api/v1.0/start_end/<start>/<end>">start/end</a></li>
                </ul>
            </body>
        </html>
    """)

# Define the precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():  # sourcery skip: merge-dict-assign
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Invoke function to retrieve a date one year prior to the most recent date from a custom function
    one_year_ago = get_one_year_from_latest(session)

    # Save the query results 
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_ago).all()
    
    session.close()
    
     # Convert query results to dictionary with the date as the key and the value as the precipitation
    precipitation_data = {date[0]: date[1] for date in results}
   
    return jsonify(precipitation_data) 

# Define the stations route
@app.route("/api/v1.0/stations")
def stations():  # sourcery skip: merge-dict-assign
    
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Save the query results 
    station_results = session.query(Station.id,
                            Station.station,
                            Station.name,
                            Station.latitude,
                            Station.longitude,
                            Station.elevation).all()
    
    session.close()

    # Create a dictionary from the row data and append to a list
    all_station=[]
    for id,station,name,latitude,longitude,elevation in station_results:
        station_dict={}
        station_dict['id']=id
        station_dict['station']=station
        station_dict['name']=name
        station_dict['latitude']=latitude
        station_dict['longitude']=longitude
        station_dict['elevation']=elevation
        all_station.append(station_dict)
        
    return jsonify(all_station)

# Define the stations route
@app.route("/api/v1.0/tobs")
def tobs():  # sourcery skip: merge-dict-assign

    # Create our session (link) from Python to the DB
    session = Session(engine) 
    
    one_year_ago = get_one_year_from_latest(session)
    
    # Using the most active station id
    # Query the last 12 months of temperature observation data for most active station
    active_station_results = session.query(Measurement.station,
                                    Measurement.date,
                                    Measurement.tobs)\
                                .filter(Measurement.date >= one_year_ago)\
                                .filter(Measurement.station == 'USC00519281').all()
        
    # Create a list of dictionaries from the query results
    most_active_list = []
    for row in active_station_results:
        # Create a dictionary for each row
        tobs_dict = {
            'station': row.station,
            'date': row.date,
            'tobs': row.tobs
        }
        most_active_list.append(tobs_dict)

    session.close()
        
    return jsonify(most_active_list)

# Define the start route
@app.route("/api/v1.0/start/<start>")
def get_start(start):

  # Create session
  session = Session(engine)
  
  # Invoke function to retrieve most recent date
  most_recent = get_most_recent_date(session)
 
  # Convert start date to datetime object with proper format validation
  try:
      start = dt.datetime.strptime(most_recent[0], "%Y-%m-%d").date()
  except ValueError:
      return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400

  # Build query
  temp_query_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
              filter(Measurement.date >= start).all()

  # Convert results to list of dictionaries
  tobs_data = []
  for min_temp, avg_temp, max_temp in temp_query_results:
      tobs_dict = {"Min_Temp": min_temp, 
                   "Avg_Temp": avg_temp, 
                   "Max_Temp": max_temp}
      tobs_data.append(tobs_dict)

  session.close()

  return jsonify(tobs_data)

# Define the start route
@app.route("/api/v1.0/start_end/<start>/<end>")
def get_start_end(start, end):

  # Create session
  session = Session(engine)

  # Invoke function to retrieve most recent date
  most_recent = get_most_recent_date(session)

  # Invoke function to retrieve oldest date
  oldest_date = get_oldest_date(session)
  
  # Convert start date to datetime object with proper format validation
  try:
      end = dt.datetime.strptime(most_recent[0], "%Y-%m-%d").date()
      start = dt.datetime.strptime(oldest_date[0], "%Y-%m-%d").date()
  except ValueError:
      return jsonify({"error": "Invalid date format. Use YYYY-MM-DD."}), 400
  
  # Build query
  temp_query_result = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).filter(Measurement.date <= end).all()

  # Convert results to list of dictionaries
  tobs_data = []
  for min_temp, avg_temp, max_temp in temp_query_result:
      tobs_dict = {"Min_Temp": min_temp, 
                   "Avg_Temp": avg_temp, 
                   "Max_Temp": max_temp}
      tobs_data.append(tobs_dict)

  session.close()

  return jsonify(tobs_data)

# Run the Flask app in debug mode
if __name__ == '__main__':
    app.run(debug=True)