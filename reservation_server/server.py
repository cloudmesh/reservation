#! /usr/bin/env python

from docopt import docopt
from flask import Flask, request, Response
from flask import render_template
from flask.ext.restful import reqparse, abort, Api, Resource
from reservation.cli import reservation_connect
from reservation.model import Reservation
from reservation.generate import generate_from_string
from reservation.plot import timeline_plot
from reservation import model
import datetime
import csv
from flask_bootstrap import Bootstrap
import json
from flask import jsonify
from random import randint
 

#print json.dumps({'4': 5, '6': 7}, sort_keys=False,
# indent=4, separators=(',', ': '))

    
app = Flask(__name__)
api = Api(app)
Bootstrap(app)
app.debug = True


class RestDeleteAll(Resource):
    """Uses REST framework to delete all reservations made. It goes into the function model.py and call the delete_all() function. 
"""
    def get(self):
        Reservation().delete_all()
        resp = Response(list(), status=200, mimetype='text/html')
        return resp
    
class List(Resource):
    """Uses REST framework to list reservations made. It calls the list() function using the list_table() function. 
"""
    def get(self):
        data = Reservation.objects()
        resp = Response(list_table(data), status=200, mimetype='text/html')
        return resp

class ListBySelection(Resource):
    """List the reservations: as param it can get any of the arguments

:param start_time: The time a reservation starts
:type start_time: Datetime
:param end_time: The time a reservation ends
:type end_time: Datetime
:param cm_id: The cloudmesh resource ID
:type cm_id: String
:param user: The name of the user (username)
:type user: String
:param project: The reservation project
:type project: String
:param host: The host machine of the reservation
:type host: String
:param label: The label of the reservation
:type label: String
:param summary: Breaf description of the reason to make this reservation
:type summary: String"""
    def post(self):
        reservations = Reservation()
        data = {}
    
        start_time ="1901-01-01"
        end_time = "2100-12-31"
        if(request.form["start_time"] is not None):
            start_time = request.form["start_time"]
        if(request.form["end_time"] is not None):
            end_time = request.form["end_time"]


        data = reservations.list(project=request.form["project"],
                                   cm_id=request.form["cm_id"],
                                   host=request.form["host"],
                                   end_time=request.form["end_time"],
                                   user=request.form["user"],
                                   start_time= request.form["start_time"],
                                   summary=request.form["summary"],
                                   label= request.form["label"])
        
        resp = Response(list_table(data), status=200, mimetype='text/html')
        return resp
    
class Add(Resource):
    """Uses REST framework to add new reservations. It calls the add template that generates a form to add new reservations. 
"""
    def get(self):
        resp = Response(render_template('add.html', order={}), status=200, mimetype='text/html')
        return resp
    
class Delete(Resource):
    """Uses REST framework to delete reservations. It calls the delete template that generates a form to delete a reservation. 
"""
    def get(self):
    	data = Reservation.objects()
        resp = Response(render_template('delete.html', order={}), status=200, mimetype='text/html')
        return resp

class AddSubmit(Resource):
    """submit a new a reservation: All fields are required    

:param start_time: The time a reservation starts
:type start_time: Datetime
:param end_time: The time a reservation ends
:type end_time: Datetime
:param cm_id: The cloudmesh resource ID
:type cm_id: String
:param user: The name of the user (username)
:type user: String
:param project: The reservation project
:type project: String
:param host: The host machine of the reservation
:type host: String
:param label: The label of the reservation
:type label: String
:param summary: Breaf description of the reason to make this reservation
:type summary: String
"""
    def post(self):
        expanded_list = hostlist.expand_hostlist(request.form["host"])
        print expanded_list
        reservations = Reservation(project=request.form["project"],
                                   cm_id=request.form["cm_id"],
                                   host=request.form["host"],
                                   end_time=request.form["end_time"],
                                   user=request.form["user"],
                                   start_time= request.form["start_time"],
                                   summary=request.form["summary"],
                                   label= request.form["label"])
        str = reservations.add()
        if str is not None:
            print str
            resp = Response(list_table(str), status=200, mimetype='text/html')
            return resp

        """list the reservations"""
        resp = Response(list(), status=200, mimetype='text/html')
        return resp

class DeleteSubmit(Resource):
    """Delete a reservation

:param label: The label of the reservation
:type label: String
:param start_time: The time a reservation starts
:type start_time: Datetime
:param end_time: The time a reservation ends
:type end_time: Datetime
:param cm_id: The cloudmesh resource ID
:type cm_id: String
:param user: The name of the user (username)
:type user: String
:param project: The reservation project
:type project: String
:param host: The host machine of the reservation
:type host: String
:param summary: whay do we search on the summary?????
:type summary: NOT SURE WHY WE ALLO PASSING IN TEH SUMMARY SEEMS A BUG, BUT MAYBE YOU CAN EXPLAIN
"""
    def post(self):
        reservations = Reservation()
        start_time ="1901-01-01"
        end_time = "2100-12-31"
        if request.method=='POST':
            if(request.form["start_time"] is not None):
                start_time = request.form["start_time"]
            if(request.form["end_time"] is not None):
                end_time = request.form["end_time"]
                
            reservations.delete_selection(project=request.form["project"],
                                   cm_id=request.form["cm_id"],
                                   host=request.form["host"],
                                   end_time=request.form["end_time"],
                                   user=request.form["user"],
                                   start_time= request.form["start_time"],
                                   summary=request.form["summary"],
                                   label= request.form["label"])
            
        resp = Response(list(), status=200, mimetype='text/html')
        return resp
    
class AddSubmitFile(Resource):
    """Add a reservation uploading a csv file
    
:param:uses a form to upload the reservations
"""
    def post(self):
        file = request.files["file"]
        reader = csv.reader(file)
        for row in reader:
            reservations = Reservation(cm_id=row[0],
                                       label=row[1],
                                       user=row[2],
                                       project=row[3],
                                       start_time=row[4],
                                       end_time=row[5],
                                       host=row[6],
                                       summary=row[7])
            reservations.add()

        resp = Response(list(), status=200, mimetype='text/html')
        return resp

api.add_resource(RestDeleteAll, '/delete/all')
api.add_resource(List, '/list/')
api.add_resource(ListBySelection, '/list/submit')
api.add_resource(Add, '/add/')
api.add_resource(Delete, '/delete/')
api.add_resource(DeleteSubmit, '/delete/submit')
api.add_resource(AddSubmit, '/add/submit')
api.add_resource(AddSubmitFile, '/add/file')

def main():
    db = reservation_connect()
    app.run()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chart')
def timeline():
    """printing the timeline from mongodb"""
    filename="static/time-plot"
    print "TIMELINE", filename

    random_number = randint(1,100000000)
    
    if timeline_plot(filename):
        return render_template('plot.html',number=random_number)        
    else:
        return error('No Reservation data found.')

def list():
    data = Reservation.objects()
    return list_table(data)

def list_table(data):
    """this method renders the reservation data in a table
:param data: The reservation data
:type data: search result from Reservation
"""
    order = Reservation._order
    return render_template('list.html',
                            order=Reservation._order,
                            reservations=data)
    
def entry_table(data):
    """This method renders the reservation data in a table
    
:param data: The reservation data
:type data: search result from Reservation
"""
    try:
        entry = data[0]
    except:
        return error('can not find the specified object')
        
    order = Reservation._order
    return render_template('table.html',
                            order=Reservation._order,
                            reservation=data)

@app.route('/error/<msg>')
def error(msg):
    return render_template('error.html',
                            msg=msg)

    



@app.route("/list/user/<user>")
def list_user_reservations(user):
    """Find the reservations searching by user
    
:param user: the username
"""
    data = Reservation().find_user(user)
    return list_table(data)

@app.route("/list/id/<id>")
def find_reservation_by_id(id):
    """find the reservations searching by cm_id"""
    data = Reservation().find_id(id)
    return entry_table(data)

@app.route("/list/label/<label>")
def find_reservation_by_label(label):
    """list the reservations searching by label"""
    data = Reservation().find_label(label)
    return entry_table(data)

'''@app.route("/delete/all")
def delete_all():
"""delete all the reservations"""
Reservation().delete_all()
return list()'''

@app.route("/random")
def random_reservations():
    """Randomically create reservations"""
    generate_from_string("m[01-05] 10 10 now")
    return list()


# ######################################################################
# ALL METHODS BELOW THIS ARE POSSIBLY WRONG
# ######################################################################

@app.route("/list/", methods=['GET', 'POST'])
def list_fancy():
    """List the reservations: as param it can get any of the arguments

:param start_time: The time a reservation starts
:type start_time: Datetime
:param end_time: The time a reservation ends
:type end_time: Datetime
:param cm_id: The cloudmesh resource ID
:type cm_id: String
:param user: The name of the user (username)
:type user: String
:param project: The reservation project
:type project: String
:param host: The host machine of the reservation
:type host: String
:param label: The label of the reservation
:type label: String
:param summary: Breaf description of the reason to make this reservation
:type summary: String"""
    reservations = Reservation()
    data = {}

    start_time ="1901-01-01"
    end_time = "2100-12-31"
    
    if request.method=='GET':
        if(request.args.get("start") is not None):
            start_time = request.args.get("start")
        if(request.args.get("end") is not None):
            end_time = request.args.get("end")

        cm_id = request.args.get("cm_id")
        user = request.args.get("user")
        project = request.args.get("project")
        label = request.args.get("label")
        host=request.args.get("host")
        summary=request.args.get("summary")

        data = reservations.list(cm_id=cm_id,
                                user=user,
                                project=project,
                                label=label,
                                start_time=start_time,
                                end_time=end_time,
                                host=host,
                                summary=summary)
        
    return list_table(data)


@app.route("/duration/<id>")
def duration(id):
    """List the reservations by duration
    
:param cm_id: Cloudmesh Resource ID
:type cm_id: String
"""
    data = Reservation().duration(id)
    #print data
    return render_template('list.html', order=str(data))


@app.route("/update/", methods=['GET', 'POST'])
def update_selection():
    """Update a reservation"""
    if request.method=='GET':
        fromObj = [request.args.keys()[0], request.args.values()[0]]
        toObj = [request.args.keys()[1], request.args.values()[1]]
    reservations = Reservation()
    reservations.update_selection(fromObj, toObj)
    data = reservations.all()
    order = reservations._order
    return render_template('list.html', order=order, reservation=data)

'''@app.route("/delete/", methods=['GET'])
def delete_selection():
"""delete a reservation

:param label: the label of the reservation
:type label: String
:param start_time: bla bla
:type start_time: Datetime
:param end_time: bla bla
:type end_time: Datetime
:param cm_id: bla bla
:type cm_id: String
:param user: bla bla
:type user: String
:param project: bla bla
:type project: String
:param label: bla bla
:type label: String
:param host: bla bla
:type host: String
:param summary: whay do we search on the summary?????
:type summary: NOT SURE WHY WE ALLO PASSING IN TEH SUMMARY SEEMS A BUG, BUT MAYBE YOU CAN EXPLAIN
"""
reservations = Reservation()
start_time ="1901-01-01"
end_time = "2100-12-31"
if request.method=='GET':
if(request.args.get("start") is not None):
start_time = request.args.get("start")
if(request.args.get("end") is not None):
end_time = request.args.get("end")
reservations.delete_selection(cm_id=request.args.get("cm_id"),
user=request.args.get("user"),
project=request.args.get("project"),
label= request.args.get("label"),
start_time= start_time,
end_time=end_time,
host=request.args.get("host"),
summary=request.args.get("summary"))
return list()
'''
'''@app.route("/add/file", methods=['POST'])
def add_submitFile():
"""add a reservation uploading a csv file

:use a form to upload
"""
if request.method=='POST':
file = request.files["file"]
reader = csv.reader(file)
for row in reader:
reservations = Reservation(cm_id=row[0],
label=row[1],
user=row[2],
project=row[3],
start_time=row[4],
end_time=row[5],
host=row[6],
summary=row[7])
reservations.add()

return list()'''

'''@app.route("/add/submit", methods=['POST'])
def add_submit():
"""submit a new a reservation
"""
if request.method=='POST':
reservations = Reservation(project=request.form["project"],
cm_id=request.form["cm_id"],
host=request.form["host"],
end_time=request.form["end_time"],
user=request.form["user"],
start_time= request.form["start_time"],
summary=request.form["summary"],
label= request.form["label"])
str = reservations.add()
if str is not None:
return render_template('list.html', order=str)

"""list the reservations"""
return list()'''

'''@app.route("/add/")
def route_reservation_add():
"""add a reservation: use a form to get info from the user

"""
return render_template('add.html', order={})'''

if __name__ == "__main__":
    main()
