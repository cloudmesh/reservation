#! /usr/bin/env python


from flask import Flask, request
from flask import render_template
from reservation.model import reservation_connect
from reservation.model import Reservation
from reservation.plot import timeline_plot
from reservation import model
import datetime
import csv

app = Flask(__name__)    
app.debug = True


def main():
    db = reservation_connect()
    app.run()


@app.route('/')
def route_table():
    reservations = Reservation.objects()
    for reservation in reservations:
        print reservation
    return render_template('table.html',
                           order=Reservation._order,
                           reservations=reservations)

    
@app.route('/time')
def timeline():
    """printing the timeline from mongodb"""
    filename="static/time-plot"
    
    print "TIMELINE", filename
    timeline_plot(filename)
    return render_template('plot.html')

@app.route("/find_user/<user>")
def find_user(user):        
    """list the reservations"""
    rsv = Reservation()    
    return render_template('list.html', order=rsv.find_user(user))

@app.route("/find_user/<cm_id>")
def find_id(cm_id):        
    """list the reservations"""
    rsv = Reservation()    
    return render_template('list.html', order=rsv.find_id(cm_id))

@app.route("/duration/<cm_id>")
def duration(cm_id):        
    """list the reservations"""
    rsv = Reservation()    
    return render_template('list.html', order=rsv.duration(cm_id))

@app.route("/find_label/<label>")
def find_label(label):        
    """list the reservations"""
    rsv = Reservation()    
    return render_template('list.html', order=rsv.find_label(label))

@app.route("/findall")
def find_all():        
    """list the reservations"""
    reservations = Reservation.objects()
    for reservation in reservations:
        return render_template('list.html', order=Reservation.objects(list()))
    
@app.route("/delete_all")
def delete_all():        
    """list the reservations"""
    rsv = Reservation()
    return render_template('list.html', order=rsv.delete_all())

@app.route("/list/", methods=['GET', 'POST'])
def list():
    """list the reservations

    :param label: the label of the reservation
    """
    #label = "exp-1-9"
    #reservations = Reservation.objects()
    rsv = Reservation()
    reservations = {}
    start_time ="1901-01-01"
    end_time = "2100-12-31"
    #print 70 * "="
    if request.method=='GET':
        if(request.args.get("start") is not None):
            start_time = request.args.get("start")
        if(request.args.get("end") is not None):
            end_time = request.args.get("end") 
        reservations = rsv.list(cm_id=request.args.get("cm_id"), user=request.args.get("user"), project=request.args.get("project"), label= request.args.get("label"), start_time= start_time, end_time=end_time, host=request.args.get("host"), summary=request.args.get("summary"))
        #print reservations
    #for reservation in reservations:
    return render_template('list.html', order=reservations)

@app.route("/delete/", methods=['GET', 'POST'])
def delete_selection():
    """list the reservations

    :param label: the label of the reservation
    """
    #label = "exp-1-9"
    #reservations = Reservation.objects()
    rsv = Reservation()
    start_time ="1901-01-01"
    end_time = "2100-12-31"
    #print 70 * "="
    if request.method=='GET':
        if(request.args.get("start") is not None):
            start_time = request.args.get("start")
        if(request.args.get("end") is not None):
            end_time = request.args.get("end") 
        rsv.delete_selection(cm_id=request.args.get("cm_id"), user=request.args.get("user"), project=request.args.get("project"), label= request.args.get("label"), start_time= start_time, end_time=end_time, host=request.args.get("host"), summary=request.args.get("summary"))
        #print reservations
    #for reservation in reservations:
    reservations = rsv.find_all()
    return render_template('list.html', order=reservations)
   
@app.route("/add/addFile", methods=['POST'])
def add_submitFile():
    if request.method=='POST':
        file = request.files["file"]
        reader = csv.reader(file)
        for row in reader:
            reservations = Reservation(cm_id=row[0], label=row[1], user=row[2], project=row[3], start_time=row[4], end_time=row[5], host=row[6], summary=row[7])
            reservations.add()
    rsv = Reservation()
    reservations = rsv.find_all()
    for reservation in reservations:
        return render_template('list.html', order=reservations)

@app.route("/add/addSubmit", methods=['POST'])
def add_submit():
    if request.method=='POST':
        reservations = Reservation(project=request.form["project"], cm_id=request.form["cm_id"], host=request.form["host"], end_time=request.form["end_time"], user=request.form["user"], start_time= request.form["start_time"], summary=request.form["summary"], label= request.form["label"])
        reservations.add()
    """list the reservations"""
    rsv = Reservation()
    reservations = rsv.find_all()
    for reservation in reservations:
        return render_template('list.html', order=reservations)

@app.route("/add/")
def route_reservation_add():
    """add a reservation

    :param label: the label of the reservation
    :param resource: the resource
    :param time_from: the start time
    :param time_to: the end time    
    """
    print "in add"
    return render_template('add.html', order={})

if __name__ == "__main__":
    main()

