#!/usr/bin/env python

from flask import Flask, jsonify

from cloudmesh.rack.rack_data import RackData
from cloudmesh.temperature.cm_temperature import cm_temperature as RackTemperature

app = Flask(__name__)


nop = [
    {
        'id': 1,
        'label' : "abc",
        'description': 'not yet implemented',
        'status' : 4,
        'unit' : 'temperature',
        'ttl' : 'time to live in data to be implemented'
    }
]

@app.route('/cm/v1.0/researvation/', methods = ['GET'])
def get_list():
    """returns the temperatures of all registered servers"""
    return jsonify( {"reservation": nop} )
    
@app.route('/cm/v1.0/reservation/<label>', methods = ['GET'])
def get_researvation_by_label(cluster):
    """returns all the resrevations with a given label, there could be multiple."""
    return jsonify( {"reservation": nop} )
    

if __name__ == '__main__':
    print "start"
    app.run(debug = True)
