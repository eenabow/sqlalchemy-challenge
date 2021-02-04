
#Import dependencies
import numpy as np 
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
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
        )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a dictionary of dates and precipitation for a year"""
    # Query all passengers
        # results = session.query(Passenger.name).all()
        one_year_ago = recent_date - dt.timedelta(days = 365) 

        # Perform a query to retrieve the data and precipitation scores and sort the dataframe by date
        precipitation_year = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).order_by(Measurement.date).all()
        ##CREATE A LIST 
        precipitation_year

    return jsonify(precipitation_year)
    session.close()
    

@app.route("/api/v1.0/stations")
def stations():
        #Create our session (link) from Python to the DB
        session = Session(engine)

        """Return a list of all station names"""
        #Query all stations
        results = session.query(Station.station).all()

        session.close()

        # Convert list of tuples into normal list
        all_stations = list(np.ravel(results))

        return jsonify(all_stations)

# @app.route("/api/v1.0/tobs")
# def tobs():
#         return jsonify(Most_active_station)
        

# @app.route("/api/v1.0/<start>")
# def 

##LOOK AT JUSTICE LEAGUE -- START And START END SHOULD ACT LIKE A VARIABLE 
##SIMILAR TO PART 1 OF TOBS FOR YEAR -- if you put any date in the browser then returns tobs 

justice_league_members = [
    {"date": "min", "avg", "max"}

    def justice_league_character(date):
    """Fetch the Justice League character whose real_name matches
       the path variable supplied by the user, or a 404 if not."""

    canonicalized = date.replace(" ", "").lower()
    for character in justice_league_members:
        search_term = character["date"].replace(" ", "").lower() #turn into a datetime object

        if search_term == canonicalized:
            return jsonify(character)

    return jsonify({"error": f"Character with real_name {real_name} not found."}), 404



# @app.route("/api/v1.0/<start>/<end>")
# def 

if __name__ == "__main__":
    app.run(debug=True)
