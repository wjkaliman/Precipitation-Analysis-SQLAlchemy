# ## Hints

# You will need to join the station and measurement tables for some of the queries.

# Use Flask `jsonify` to convert your API data into a valid JSON response object.

# 1. import all dependendies
from flask import Flask, jsonify

import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# create engine to connect to database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# Create an app, being sure to pass __name__
app = Flask(__name__)

# List all routes that are available.

@app.route("/")
def Welcome():
    return(
    f"test"    
    f"/api/v1.0/precipitation<br/>"
    f"/api/v1.0/stations<br/>"
    f"/api/v1.0/tobs<br/>"
    f"/api/v1.0/&lt;start<br/>"
    f"/api/v1.0/&lt;start/end")


@app.route("/api/v1.0/precipitation")
def precipitation():
    session_prec = Session(engine)
    x = "name"
    return jsonify(x) 
####################################################
@app.route("/api/v1.0/stations")
def stations():
    session_station = Session(engine)
#Return a JSON list of stations from the dataset.
    results = Session.query(station.station).all()
    session.close
    station_list = list(np.ravel(results))
    return jsonify(station_list)
####################################################

@app.route("/api/v1.0/tobs")
def tobs():
    session_tobs = Session(engine)
# Return a JSON list of temperature observations (TOBS) for the previous year.
    results = Session.query(measurement.tobs).\
        filter(measurement.date >= "2016-02-01").\
        filter(measurement.date <= "2017-02-01").all()
    Session.close
    tobs_list = list(np.ravel(results))
    return jsonify(tobs_list)
####################################################
@app.route("/api/v1.0/<start>/<end>")
def start():
    Session_date = Session(engine)
    

    return jsonify()
####################################################



# Return a JSON list of stations from the dataset.
# Query the dates and temperature observations of the most active station
# for the last year of data.

# Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.
# session = session(engine)

# calc_results = session.query(func.min(measurement.tobs),
#                              func.avg(measurement.tobs),
#                              func.max(measurement.tobs)
#                .join(station, station == measurement.station)
#                .filter(measurement.date >= start)
#                .filetr(measurement.date<= end)
#                .all())
# session.close()               

# # When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.
# session = session(engine)

# calc_results = session.query(func.min(measurement.tobs),
#                              func.avg(measurement.tobs),
#                              func.max(measurement.tobs)
#                .join(station, station == measurement.station)
#                .filter(measurement.date >= start)
#                .filetr(measurement.date<= end)
#                .all())
# session.close()    


# ## Hints

# You will need to join the station and measurement tables for some of the queries.

# Use Flask `jsonify` to convert your API data into a valid JSON response object.





# boiler plate stuff?
if __name__ == "__main__":
    app.run(debug=False)