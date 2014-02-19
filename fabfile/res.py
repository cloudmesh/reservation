from fabric.api import task, local
import sys

@task
def start():
    """start the reservation service"""
    local("python ./reservation/reservation_server.py")

@task
def stop():
    """stop the reservation service"""
    local("killall -9 reservation_server.py")



