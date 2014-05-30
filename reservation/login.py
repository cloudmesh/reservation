#! /usr/bin/env python
'''Login '''

from pprint import pprint
from cloudmesh_install import config_file
import argparse
import os
import sys  
import httplib2
import json
from apiclient import discovery
from oauth2client import file
from oauth2client import client
from oauth2client import tools

def login_command(argv):
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        parents=[tools.argparser])
    CLIENT_SECRETS = config_file('/client_secrets.json')
    FLOW = client.flow_from_clientsecrets(CLIENT_SECRETS,
      scope=[
          'https://www.googleapis.com/auth/calendar',
          'https://www.googleapis.com/auth/calendar.readonly',
        ],
        message=tools.message_if_missing(CLIENT_SECRETS))
    # Flags??????

    flags=parser.parse_args(argv[1:])
    pprint(flags)
    storage = file.Storage('Main.dat')
    credentials = storage.get()
    if credentials is None or credentials.invalid:
        credentials = tools.run_flow(FLOW, storage, flags)

if __name__ == '__main__':
    login_command(sys.argv)
    
