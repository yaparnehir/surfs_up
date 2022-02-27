import datetime as dt
import tempfile
#from lib2to3.pytree import _Results
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask
from flask import jsonify

#access and query database
engine = create_engine("sqlite:///hawaii.sqlite")
#reflect to class
Base = automap_base()
Base.prepare(engine, reflect=True)
#create references for each class
Measurement = Base.classes.measurement
Station = Base.classes.station
#create a session
session = Session(engine)



#create Flask app name app
app = Flask(__name__)
#to import app in another file 
#import app
#print("example __name__ = %s", __name__)
#if __name__ == "__main__":
#print("example is being run directly.")
#else:
#print("example is being imported")



@app.route('/')
def welcome():
    return(
    
    f"Welcome to the Climate Analysis API!<br/>"
    f"Available Routes:<br/>"
    f"/api/v1.0/precipitation<br/>"
    f"/api/v1.0/stations<br/>"
    f"/api/v1.0/tobs<br/>"
   f"/api/v1.0/temp/start/end<br/>"
    )
    
@app.route("/api/v1.0/precipitation")
def precipitaion():
    # .\ helps us to continue to writing a query on a next line
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).\
      filter(Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}
    return jsonify(precip)
    
@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station.station).all()
    stations = list(np.ravel(results))
    # = format to list to json similar to {"data": data}
    return jsonify(stations=stations)

@app.route("/api/v1.0/tobs")
def temp_monthly():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results= session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()
    temps = list(np.ravel(results))
    
    return jsonify(temp=temps)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def stats(start = None, end = None):
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)

    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))
    
    return jsonify(temps=temps)