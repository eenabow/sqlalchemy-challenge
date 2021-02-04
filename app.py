
#Import dependencies
import numpy as pd 
import sqlalchemy 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement

Station= Base.classes.station

#################################################
# Flask Setup
#################################################

#Create an app
app = Flask(__name__)

#################################################################
# FLASK ROUTES
################################################################

@app.route("/")
def welcome(): 
        print("Server received request for 'Home' page...")
        return ( 
        f"Available api routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
        )

# @app.route("/api/v1.0/precipitation")
# def precipitation():
#         return jsonify(prcp_df)

# @app.route("/api/v1.0/stations<br/>")
# def stations():
        # Create our session (link) from Python to the DB
        # session = Session(engine)

        # """Return a list of all station names"""
        # Query all stations
        # results = session.query(station.station).all()

        # session.close()

        # # Convert list of tuples into normal list
        # all_stations = list(np.ravel(results))

        # return jsonify(all_stations)


