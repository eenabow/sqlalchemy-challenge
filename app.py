
#Import dependencies
import numpy as np 
import sqlalchemy 
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
import datetime as dt
#########################################################################################################################
# Database Setup
#########################################################################################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement

Station= Base.classes.station

#########################################################################################################################
# Flask Setup
#########################################################################################################################

#Create an app
app = Flask(__name__)

#########################################################################################################################
# Setting variables
#########################################################################################################################
session = Session(engine)

#Parse through to turn string into datetime object
recent_date = session.query(func.max(Measurement.date)).all() [0][0]

recent_year = int(recent_date[0:4])
recent_month = int(recent_date[5:7])
recent_day = int(recent_date[8:])

recent_date = dt.date(recent_year,recent_month, recent_day)

"""Return a dictionary of dates and precipitation for a year"""
one_year_ago = recent_date - dt.timedelta(days = 365) 

#Find most active station
total_stations_query = session.query(Measurement.station, func.count(Measurement.station))

most_active_stations = total_stations_query.group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()

# Station= Base.classes.station

# most_active = session.query(Measurement.station, Measurement.tobs, Measurement.date).filter(Measurement.station == Station, Measurement.date >= one_year_ago).order_by(Measurement.date)[0][0]

# # Most_active_station = pd.DataFrame(most_active)

# # Most_active_station

session.close()







#########################################################################################################################
# FLASK ROUTES
#########################################################################################################################

@app.route("/")
def welcome(): 
        print("Server received request for 'Home' page...")
        return ( 
        f"Available api routes:<br/>" 
        f"/api/v1.0/precipitation : Precipitation percentages for the past year<br/>"
        f"/api/v1.0/stations : Unique stations<br/>"
        f"/api/v1.0/tobs : Temperatures for the most active station over the past year<br/>"
        f"/api/v1.0/<start> : User inputs given start date (yyyymmdd) to search for minimum, maximum, and average temperature <br/>"
        f"/api/v1.0/<start>/<end> : User inputs given start date (yyyymmdd) and end date (yyyymmdd) to search for minimum, maximum, and average temperature<br/>"
        )

#########################################################################################################################
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Perform a query to retrieve the data and precipitation scores and sort the dataframe by date
    precipitation_year = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).order_by(Measurement.date).all()
    
    prcp_list = list(np.ravel(precipitation_year))
    return jsonify(prcp_list)

    session.close()
    
#########################################################################################################################
@app.route("/api/v1.0/stations")
def stations():
        #Create our session (link) from Python to the DB
        session = Session(engine)

        """Return a list of all station names"""
        #Query all stations
        results = session.query(Station.station).all()


        # Convert list of tuples into normal list
        all_stations = list(np.ravel(results))

        return jsonify(all_stations)

        session.close()

#########################################################################################################################
@app.route("/api/v1.0/tobs")
def tobs():
        
        #Create our session (link) from Python to the DB
        session = Session(engine)

        most_active_station = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == most_active_stations[0][0], Measurement.date >= one_year_ago).all()

        Most_active_station = list(np.ravel(most_active_station))
        return jsonify(Most_active_station)
        
        session.close()

#########################################################################################################################
@app.route("/api/v1.0/<start>")
def start_date_lookup(start):

    #Create our session (link) from Python to the DB
    session = Session(engine)

    #Reformat user's input 
    start_year = (start[0:4])
    start_month = (start[4:6])
    start_date = (start[6:])
    start_input = dt.date(int(start_year), int(start_month), int(start_date)).strftime('%Y-%m-%d')


    #Query Min, Max, & Avg temps for user's input
    results = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start_input).all() 

    session.close()

    start_date_tobs = []
    for min, avg, max in results:
        start_date_tobs_dict = {}
        start_date_tobs_dict["min_temp"] = min
        start_date_tobs_dict["avg_temp"] = avg
        start_date_tobs_dict["max_temp"] = max
        start_date_tobs.append(start_date_tobs_dict) 
    print("Years available: 2010-2017, please use yyyymmdd format.<br/>")
    return jsonify(start_date_tobs)


@app.route("/api/v1.0/<start>/<end>")
def start_end_lookup(start, end):
#Create our session (link) from Python to the DB
    session = Session(engine)

    #Reformat user's input 
    start_year = (start[0:4])
    start_month = (start[4:6])
    start_date = (start[6:])
    start_input = dt.date(int(start_year), int(start_month), int(start_date)).strftime('%Y-%m-%d')


    #Reformat user's input 
    end_year = (end[0:4])
    end_month = (end[4:6])
    end_date = (end[6:])
    end_input = dt.date(int(end_year), int(end_month), int(end_date)).strftime('%Y-%m-%d')

    #Query Min, Max, & Avg temps for user's input
    results2= session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start_input).filter (Measurement.date <= end_input).all()
    # results2= session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= stop).all()
    session.close()

    end_date_tobs = []
    for min, avg, max in results2:
        end_date_tobs_dict = {}
        end_date_tobs_dict["min_temp"] = min
        end_date_tobs_dict["avg_temp"] = avg
        end_date_tobs_dict["max_temp"] = max
        end_date_tobs.append(end_date_tobs_dict) 
    print("Years available: 2010-2017, please use yyyymmdd format.<br/>")
    return jsonify(end_date_tobs)

   
if __name__ == "__main__":
    app.run(debug=True)
