#! /usr/bin/env python


from flask import Flask
from flask import render_template
from reservation.model import reservation_connect
from reservation.model import Reservation



app = Flask(__name__)    
app.debug = True

def main():
    db = reservation_connect()
    app.run()

@app.route('/')
def swimlane():
    reservations = Reservation.objects()
    data = []
    for reservation in reservations:
        data.append({"id": reservation.label,
                     "start": reservation.start_time,
                     "end": reservation.end_time,
                     'desc': "abc",
                     'class': 'past',
                     'lane': reservation.host,
                     })                   
    print data
    return render_template('timeline.html',
                           order=Reservation._order,
                           reservations=reservations,
                           data=data)
    
@app.route('/home')
def home_page():
    reservations = Reservation.objects()
    for reservation in reservations:
        print reservation
    return render_template('index.html',
                           order=Reservation._order,
                           reservations=reservations)

@app.route("/cm/v1.0/reservation/list")
def route_reservation():
    """list the reservations"""
    return "not implemented"

@app.route("/cm/v1.0/reservation/list/<label>")
def route_reservation_by_label(label):
    """list the reservations

    :param label: the label of the reservation
    """
    return "not implemented"

@app.route("/cm/v1.0/reservation/delete/<label>")
def route_reservation_delete(label):
    """delet the reservation

    :param label: the label of the reservation
    """
    return "not implemented"

@app.route("/cm/v1.0/reservation/delete/<resource>/<time_from>/<time_to>")
def route_reservation_delete_time(label,resource,time_from,time_to):
    """delete reservations

    :param resource: the resource
    :param time_from: the start time
    :param time_to: the end time    
    """
    return "not implemented"



@app.route("/cm/v1.0/reservation/add/<label>/<resource>/<time_from>/<time_to>")
def route_reservation_add(label,resource,time_from,time_to):
    """add a reservation

    :param label: the label of the reservation
    :param resource: the resource
    :param time_from: the start time
    :param time_to: the end time    
    """
    return "not implemented"

if __name__ == "__main__":
    main()

