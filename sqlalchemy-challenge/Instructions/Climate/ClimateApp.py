import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
##################################################
#engine = create_engine("sqlite:///C:/pc_dav_hw/sqlalchemy-challenge/Instructions/Resources/hawaii.sqlite")
engine = create_engine("sqlite:///hawaii.sqlite")
print("I an here")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)



# Save reference to the table
Measurement = Base.classes.measurement
Satation  = Base.classes.station
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/dateRange<start><end><br/>"
        f"/api/v1.0/dateRange_start<start><br/>"
    )
@app.route("/api/v1.0/precipitation/<date>")
def precipitation(date):
    session = Session(engine)
    results = session.query(Measurement.station,Measurement.date,Measurement.prcp).filter(Measurement.date==date).all()
    session.close()

    all_dates_prep = []
    for station,date,prcp in results:
        prcp_dict = {}
        prcp_dict["station"] = station
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
       
        all_dates_prep.append(prcp_dict)

    return jsonify(all_dates_prep)


@app.route("/api/v1.0/stations")   
def sattaions():
    session =Session(engine)

    results = session.query(Satation.station).all()
    session.close()

    sataion_list =list(np.ravel(results))
    return jsonify(sataion_list)

@app.route("/api/v1.0/tobs")
def date_temp_obs():
    session = Session(engine)
    results =session.query(Measurement.station,Measurement.date,Measurement.tobs).filter(Measurement.date >='2016-08-23').all()
    session.close()
    #tobs_list =list(np.ravel(results))
    #return jsonify(tobs_list)
    all_dates_tobs = []
    for station,date,tobs in results:
        tobs_dict = {}
        tobs_dict["station"] = station
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
       
        all_dates_tobs.append(tobs_dict)

    return jsonify(all_dates_tobs)



@app.route("/api/v1.0/dateRange/<start>/<end>")
def date_range_temp(start,end=None):
    session = Session(engine)
    
    results = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
        filter(Measurement.date>=start).filter(Measurement.date<=end).all()
    
    session.close()
    tobs_list = list(np.ravel(results))

    return (f"Temprature min = {tobs_list[0]} Temprature avg = {tobs_list[1]} Temprature max = {tobs_list[2]}")
 
    
@app.route("/api/v1.0/dateRange_start/<start>")
def date_start_temp(start):
    session = Session(engine)
    
    results = session.query(func.min(Measurement.tobs),func.avg(Measurement.tobs),func.max(Measurement.tobs)).\
        filter(Measurement.date>=start).all()
    
    session.close()
    tobs_list = list(np.ravel(results))

    return (f"Temprature min = {tobs_list[0]} Temprature avg = {tobs_list[1]} Temprature max = {tobs_list[2]}")
    

if __name__ == '__main__':
    app.run(debug=True)    