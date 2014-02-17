from fabric.api import task, local
import sys

@task
def start():
    """start the reservation service"""
    local("echo 'start the service'")

@task
def stop():
    """stop the reservation service"""
    local("echo 'stop the service somehow, see in cloudmesh fab mongo.stop where we use killallx'")



