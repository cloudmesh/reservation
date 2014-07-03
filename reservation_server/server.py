#! /usr/bin/env python


from flask import Flask, request
from flask import render_template
from reservation.model import reservation_connect
from reservation.model import Reservation
from reservation.plot import timeline_plot
from reservation import model
import datetime
import csv
from flask_bootstrap import Bootstrap

app = Flask(__name__)    
Bootstrap(app)
app.debug = True


def main():
    db = reservation_connect()
    app.run()

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/boot')
def boot():
    return render_template('boot.html')
    
@app.route('/table')
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

@app.route("/find_user")
def find_users():        
    """find the reservations by user
    *can be used in production mode
    """
    rsv = Reservation()    
    return render_template('finduser.html', order=rsv.find_user(user))

@app.route("/find_cm_id/<cm_id>")
def find_id(cm_id):        
    """find the reservations by cm_id"""
    rsv = Reservation()    
    return render_template('list.html', order=rsv.find_id(cm_id))

@app.route("/duration/<cm_id>")
def duration(cm_id):
    """list the reservations by duration"""
    rsv = Reservation()
    return render_template('list.html', order=rsv.duration(cm_id))

@app.route("/find_label/<label>")
def find_label(label):        
    """list the reservations by label"""
    rsv = Reservation()    
    return render_template('list.html', order=rsv.find_label(label))

@app.route("/findall")
def find_all():        
    """list all the reservations"""
    rsv = Reservation()
    return render_template('list.html', order=rsv.find_all())
    
@app.route("/delete_all")
def delete_all():        
    """delete all the reservations"""
    rsv = Reservation()
    rsv.delete_all()
    return render_template('list.html', order=rsv.find_all())

@app.route("/update/", methods=['GET', 'POST'])
def update_selection():        
    """delete all the reservations"""
    if request.method=='GET':
        fromObj = [request.args.keys()[0], request.args.values()[0]]
        toObj = [request.args.keys()[1], request.args.values()[1]]
    rsv = Reservation()
    rsv.update_selection(fromObj, toObj)
    return render_template('list.html', order=rsv.find_all())

@app.route("/list/", methods=['GET', 'POST'])
def list():
    """list the reservations

    as param it can get any of the arguments
    """
    rsv = Reservation()
    reservations = {}
    start_time ="1901-01-01"
    end_time = "2100-12-31"
    if request.method=='GET':
        if(request.args.get("start") is not None):
            start_time = request.args.get("start")
        if(request.args.get("end") is not None):
            end_time = request.args.get("end") 
        reservations = rsv.list(cm_id=request.args.get("cm_id"), user=request.args.get("user"), project=request.args.get("project"), label= request.args.get("label"), start_time= start_time, end_time=end_time, host=request.args.get("host"), summary=request.args.get("summary"))
        
    return render_template('list.html', 
                           order=Reservation._order,
                           reservations=reservations)


@app.route("/delete/", methods=['GET', 'POST'])
def delete_selection():
    """delete a reservation

    :param label: the label of the reservation
    """
    rsv = Reservation()
    start_time ="1901-01-01"
    end_time = "2100-12-31"
    if request.method=='GET':
        if(request.args.get("start") is not None):
            start_time = request.args.get("start")
        if(request.args.get("end") is not None):
            end_time = request.args.get("end") 
        rsv.delete_selection(cm_id=request.args.get("cm_id"), user=request.args.get("user"), project=request.args.get("project"), label= request.args.get("label"), start_time= start_time, end_time=end_time, host=request.args.get("host"), summary=request.args.get("summary"))
    reservations = rsv.find_all()
    return render_template('delete.html', order=reservations)
       
@app.route("/add/addFile", methods=['POST'])
def add_submitFile():
    """add a reservation uploading a csv file

    :use a form to upload
    """
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
    """submit a new a reservation
    """
    if request.method=='POST':
        reservations = Reservation(project=request.form["project"], cm_id=request.form["cm_id"], host=request.form["host"], end_time=request.form["end_time"], user=request.form["user"], start_time= request.form["start_time"], summary=request.form["summary"], label= request.form["label"])
        str = reservations.add()
        if str is not None:
            return render_template('list.html', order=str)
    """list the reservations"""
    rsv = Reservation()
    reservations = rsv.find_all()
    for reservation in reservations:
        return render_template('list.html', order=reservations)

@app.route("/add/")
def route_reservation_add():
    """add a reservation: use a form to get info from the user

    """
    return render_template('add.html', order={})

if __name__ == "__main__":
    main()

