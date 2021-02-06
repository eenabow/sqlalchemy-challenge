## sqlalchemy_challenge ##
To begin, I used Python and SQLAlchemy to do basic climate analysis and data exploration of the climate database. All of the following analysis was completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.  Once I completed the initial analysis, I designed a Flask API based on the queries so users may interact with the information. 

Includes: 
* Output bargraph of precipitation data over the course of a year 
* Output histogram of temperature observations at Hawaii's most active station
* Flask API that allows users to interact and photos in "Routes" folder:
    * / - Homepage listing all routes available 
    * /api/v1.0/precipitation - Retrieves the last 12 months of precipitation data 
    * /api/v1.0/stations - Lists all stations from the dataset
    * /api/v1.0/tobs - Query the dates and temperature observations of the most active station for the last year of data
    * /api/v1.0/<start> & /api/v1.0/<start>/<end> - Returns a list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range (user's input yyyymmdd).


Assignment: 

**Precipitation Analysis**
    * Finding the most recent date in the data set.
    * Using this date, retrieve the last 12 months of precipitation data by querying the 12 preceding months of data. 
    * Selecting only the date and prcp values.
    * Load the query results into a Pandas DataFrame and set the index to the date column and sorting values by date.
    * Plot the results as a bargraph
    * Print the summary statistics for the precipitation data.

**Station Analysis**
    * Design a query to calculate the total number of stations in the dataset.
    * Design a query to find the most active stations (i.e. which stations have the most rows).
    * Using the most active station id, calculate the lowest, highest, and average temperature.
    * Design a query to retrieve the last 12 months of temperature observation data (TOBS), filtering by the station with the highest number of observations.
    * Query the last 12 months of temperature observation data for this station.
    * Plot the results as a histogram with bins=12.


Challenges: 
  * Readjusting xticks on bargraph 
  * Using datetime objects to reformat users entry
