import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

measurements = Base.classes.measurements
station = Base.classes.Station

session = Session(engine)

app = Flask(__name__)

@app.route("/api/v1.0/precipitation")
def precipitation():
    
    sel = [measurements.date,
    measurements.prcp]

    date = datetime.datetime.now()

    last_twelve = session.query(*sel).\
    filter(measurements.date > date).filter(measurements.prcp > 0).\
    group_by(measurements.date).\
    order_by(easurements.date).all()
    
    return jsonify(last_twelve)


@app.route("/api/v1.0/stations")
def names():
    results = session.query(station.name).all()

    # Convert list of tuples into normal list
    all_names = list(np.ravel(results))

    return jsonify(all_names)


@app.route("/api/v1.0/tobs")
def passengers():
    start_year = int(int(input('Enter the year of your visit ')) - 1)
    start_month = int(input('Enter the month of your visit, as a number '))
    start_day = int(input('Enter the day '))
    start_date = datetime.date(start_year, start_month, start_day)
    end_year = int(int(input('Enter the year of your visit ')) - 1)
    end_month = int(input('Enter the month of your visit, as a number '))
    end_day = int(input('Enter the day '))
    end_date = datetime.date(end_year, end_month, end_day)
    
    sel = [Measurements.tobs,
           func.max(Measurements.tobs),
           func.avg(Measurements.tobs),
           func.min(Measurements.tobs)]

    if start_date > 0 and end_date = null:
        data = session.query(*sel).\
        filter(Measurements.date = start_date).all()
  
    elif start_date > 0 and end_date > 0:
        data = session.query(*sel).\
        filter(Measurements.date > start_date).\
        filter(Measurements.date < end_date).all()

    plots = list(np.ravel(data))

    fig, ax = plt.subplots()

    x = range(len(plots))
    ax.boxplot(plots, patch_artist=True)
    ax.set_title('Temps')
    fig.tight_layout()
    fig.show()

if __name__ == '__main__':
    app.run(debug=True)
