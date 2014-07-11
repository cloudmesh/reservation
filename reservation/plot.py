#! /usr/bin/env python
"""
Usage:
    plot.py   
"""
import sys
import os
from model import Reservation
import datetime
from mongoengine import *
from cli import reservation_connect


    
def timeline_plot(out_filename):
    format = "svg"
    db = reservation_connect()


    reservations = Reservation.objects()

    hosts = set()
    times = set()

    if reservations.count() == 0:
        return False
    
    data = []
    for reservation in reservations:
        hosts.add(reservation["host"])
        times.add(reservation["start_time"])
        times.add(reservation["start_time"])
        #print reservation
        data.append("{0} {1} {2} {3}".format(reservation.host,
                                            reservation.start_time.strftime("%Y/%m/%d.%H:%M"),
                                            reservation.end_time.strftime("%Y/%m/%d.%H:%M"),
                                            reservation.label)
            )

    # print hosts
    # print min(times)
    # print max(times)

    delta = max(times) - min(times)

    height = len(hosts) - 1
    if height <=1:
        height = 2

    script = \
    """
    #proc getdata
    data: {data}

    #proc areadef
       title: Cloudmesh Reservation
       rectangle: 1 1 10 {no_hosts}
       xscaletype: datetime YYYY/mm/dd.hh:mm
       #xrange: {tmin} {tmax}
       xautorange: datafield=2,3
       yscaletype: categories
       ycategories: {labels} 

    #proc xaxis
       stubs: datematic

    #proc yaxis
       stubs: categories

    #proc bars
       clickmapurl: @CGI?channel=@@1&starttime=@@2&endtime=@@3&title=@@4
       color: powderblue2
       axis: x
       locfield: 1
       segmentfields: 2 3
       labelfield: 4
       longwayslabel: yes
       labeldetails: size=6
    """.format(tmin=min(times).strftime("%Y/%m/%d.%H:%M"),
               tmax=max(times).strftime("%Y/%m/%d.%H:%M"),
               labels="\n\t" + "\n\t".join(hosts),
               data="\n\t" + "\n\t".join(data),
               no_hosts=height
               )


    #print script

    filename ="/tmp/ploticus.txt"    

    with open(filename, "w") as file:
        file.write(script)

    
    if sys.platform in ["darwin"]:
        ploticus = "/usr/local/bin/pl"
    else:
        ploticus = "/usr/bin/ploticus"
    
    command = "{ploticus} {filename} -{format} -o {out}.{format}".format(out=out_filename,
                                                                         filename=filename,
                                                                         format=format,
                                                                         ploticus=ploticus)

    os.system(command)
    return True


if __name__ == "__main__":
    filename = "out"
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    timeline_plot(filename)
