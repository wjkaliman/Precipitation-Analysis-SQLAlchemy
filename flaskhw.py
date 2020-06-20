# 1. import all dependendies
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify

# create engine to connect to database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
measurement = Base.classes.measurement
station = Base.classes.station

# We will Create our session (link) from Python to the DB farther down in the code.

# Create an app, being sure to pass __name__
app = Flask(__name__)

# List all routes that are available.
# use div to help with mirroring css code

@app.route ("/")
def Welcome():
    #print('Welcome page')
    return (
        f"<div>available routes for the moment<br/>" 
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/station<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end<br/>"
        f"/api/v1.0/greater_temp/start</div>"
    )
        
# convert the query results to a dictionary using 'date' as the key and prcp as the value.
# return the json representation of your dictionary.   
@app.route('/api/v1.0/precipitation')
def precip():     
    print('Precipitation Page…')
    session = Session(engine)
    results = session.query(measurement.date, measurement.prcp).all()
    session.close()
    precip = {date:prcp for date, prcp in results}
    return jsonify(precip)

# Return a JSON list of stations from the dataset.
@app.route("/api/v1.0/station")
def station_route():
    session = Session(engine)      
    results = session.query(station.station).all()
    session.close()
    station_list = list(np.ravel(results))
    return jsonify(station_list)


# Return a JSON list of temperature observations (TOBS) for the previous year.
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine) 
    results = session.query(measurement.tobs).\
        filter(measurement.date >= "2016-02-01").\
        filter(measurement.date <= "2017-02-02").all()
    session.close()
    tobs_list = list(np.ravel(results))
    return jsonify(tobs_list)

# Return a JSON list of the minimum temperature, the average temperature,
# and the max temperature for a given start or start-end range.
@app.route("/api/v1.0/temp/<start>/<end>")
def start(start,end): 
    session = Session(engine)
    calc_results = session.query(func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)).filter(measurement.date >= start).filter(measurement.date <= end).all()                   
    session.close()
    calc_results = list(np.ravel(calc_results))
    return jsonify(calc_results)

#When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates
#greater than and equal to the start date.

@app.route("/api/v1.0/greater_temp/<start>")
def greater_temp(start):
    session = Session(engine)
    #putting parameters in a list
    sel = [func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)]
    g_results = session.query(*sel).\
        filter(measurement.date >= start).all()
    session.close()
    g_results = list(np.ravel(g_results))
    return jsonify(g_results)


if __name__ == "__main__":
    app.run(debug=False)
