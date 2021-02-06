
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
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
        )

#########################################################################################################################
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    #Parse through to turn string into datetime object
    recent_date = session.query(func.max(Measurement.date)).all() [0][0]

    recent_year = int(recent_date[0:4])
    recent_month = int(recent_date[5:7])
    recent_day = int(recent_date[8:])

    recent_date = dt.date(recent_year,recent_month, recent_day)

    """Return a dictionary of dates and precipitation for a year"""
    one_year_ago = recent_date - dt.timedelta(days = 365) 

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

        #Parse through to turn string into datetime object
        recent_date = session.query(func.max(Measurement.date)).all() [0][0]

        recent_year = int(recent_date[0:4])
        recent_month = int(recent_date[5:7])
        recent_day = int(recent_date[8:])

        recent_date = dt.date(recent_year,recent_month, recent_day)

        """Return a dictionary of dates and precipitation for a year"""
        one_year_ago = recent_date - dt.timedelta(days = 365) 

        most_active_station = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281', Measurement.date >= one_year_ago).all()

        Most_active_station = list(np.ravel(most_active_station))
        return jsonify(Most_active_station)
        
        session.close()

#########################################################################################################################
@app.route("/api/v1.0/<start>")
def start_date_lookup(start):

    #Create our session (link) from Python to the DB
    session = Session(engine)

    years = session.query(Measurement.date).all()[0]
    if start[0:4] not in 
        return (
            f'ERROR: Date not found, use yyyymmdd format<br/>'
            f'Years available: {years_available}'
        )


# ##LOOK AT JUSTICE LEAGUE -- START And START END SHOULD ACT LIKE A VARIABLE 
# ##SIMILAR TO PART 1 OF TOBS FOR YEAR -- if you put any date in the browser then returns tobs 

# justice_league_members = [
#     {"date": "min", "avg", "max"}

#     def justice_league_character(date):
#     """Fetch the Justice League character whose real_name matches
#        the path variable supplied by the user, or a 404 if not."""

#     canonicalized = date.replace(" ", "").lower()
#     for character in justice_league_members:
#         search_term = character["date"].replace(" ", "").lower() #turn into a datetime object

#         if search_term == canonicalized:
#             return jsonify(character)

#     return jsonify({"error": f"Character with real_name {real_name} not found."}), 404



# # @app.route("/api/v1.0/<start>/<end>")
# # def 

if __name__ == "__main__":
    app.run(debug=True)
