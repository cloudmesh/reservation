'''
Created on May 5, 2014

@author: oliver
'''
import datetime
import json

class ReservationClient(object):
    '''
    This class contains all the reservations that the calendar supports
    New reservation related functions can be appended at the bottom
    
    New template of the Json object to support multi-user reservations
    
    {
                  'summary': 'oliver1',
                   'description':'{
                       'hosts': '100-103',
                       'kind':'vm-server',
                       'project':'xyz',
                       'userid':'1002',
                       'displayName':'oliverlewis',
                       'email':'lewiso@indiana.edu'
                   },

                   'start': {
                       'dateTime': '2014-05-05T22:50:00.000',
                       'timeZone': 'America/New_York'
                   },

                   'end': {
                       'dateTime': '2014-05-05T23:51:00.000',
                       'timeZone': 'America/New_York'
                   }
    }
    
    
    '''

    def __init__(self, serviceArg):
        '''The init method takes in the service object an initializes it'''
        self.service = serviceArg
    
    def add(self,rsv):
        '''A reservation is a JSON object that is passes to his method to be added to the calendar'''
        if(checkRsvOverlap(self.service,rsv)==True):
            return "Reservations overlap: cannot schedule at this time"
        else:
            completedRsv = self.service.events().insert(calendarId='primary', body=rsv).execute()
            return completedRsv['id']
        
    def remove_all(self):
        '''Removes all the reservations from the calendar'''
        self.service.calendars().clear(calendarId='primary').execute()

    def remove(self,rsvId):
        '''Removes a specific reservation from the calendar. Requires the reservationID'''
        print self.service.events().delete(calendarId='primary', eventId=rsvId, sendNotifications=True).execute()


    def get_from_id(self,rsvId):
        '''displays the reservation object'''
        print self.service.events().get(calendarId='primary', eventId=rsvId).execute()
        
    def get_by_user(self,userId):
        '''Selects all the reservations made by a user'''
        page_token = None
        listIds = []
        while True:
            events = self.service.events().list(calendarId='primary', pageToken=page_token).execute()
            for event in events['items']:
                desc = event['description'].replace("'", "\"")
                d = json.loads(desc)
                if(d['userid']==str(userId)):
                    listIds.append(event['id'])
                    
            page_token = events.get('nextPageToken')
            if not page_token:
                break 
        return listIds
        
    def get_all(self):
        '''Selects all reservations in the calendar '''
        page_token = None
        event_list = []
        while True:
            events = self.service.events().list(calendarId='primary', pageToken=page_token).execute()
            for event in events['items']:
                event_list.append(self.service.events().get(calendarId='primary', eventId=event['id']).execute())
            page_token = events.get('nextPageToken')
            if not page_token:
                break
        return event_list    
    
    def get_from_label(self, labelStr):
        '''Assuming this label will return only one eventId'''
        page_token = None
        while True:
            events = self.service.events().list(calendarId='primary', pageToken=page_token).execute()
            for event in events['items']:
                if(event['summary'] == labelStr):
                    return event['id']
            page_token = events.get('nextPageToken')
            if not page_token:
                break
        return 0
            
    def reschedule(self, oldRsvId, newRsv):
        '''Used to update or modify an old reservation. Requires old reservation id and new reservation object that will replace the old reservation'''
        self.service.events().update(calendarId='primary', eventId = oldRsvId, body = newRsv).execute()
        
    def list_by_user_and_project(self, userId, projId, sTime,eTime):
        '''Lists all the users reservations made in a project from a start-time to a end time'''
        page_token = None
        evt_list = []
        while True:
            events = self.service.events().list(calendarId='primary', pageToken=page_token).execute()
            for event in events['items']:
                desc = event['description'].replace("'", "\"")
                d = json.loads(desc)
                '''The start time is checked at both the places to know if the event was started between the stime and etime'''
                if(d['userId'] == str(userId) and d['projId'] == str(projId) and event['start']['dateTime'] > sTime and event['start']['dateTime'] < eTime):
                    evt_list.append(event['id'])
            page_token = events.get('nextPageToken')
            if not page_token:
                break
        return evt_list
    
    def list_by_project(self, projId):
        '''Lists all the reservations made in a particular project'''
        page_token = None
        evt_list = []
        while True:
            events = self.service.events().list(calendarId='primary', pageToken=page_token).execute()
            for event in events['items']:
                desc = event['description'].replace("'", "\"")
                d = json.loads(desc)
                '''The start time is checked at both the places to know if the event was started between the stime and etime'''
                if(d['projId'] == str(projId)):
                    evt_list.append(event['id'])
            page_token = events.get('nextPageToken')
            if not page_token:
                break
        return evt_list
    
    def duration(self, rsvId):
        '''Shows the duration of the reservation'''
        rsvEvent = self.service.events().get(calendarId='primary', eventId=rsvId).execute()
        duration = rsvEvent['start']['dateTime']- rsvEvent['end']['dateTime']
        return duration
        
      
def check_overlap(service, newRsv):
    page_token = None
    flag = False
    while True:
        events = service.events().list(calendarId='primary', pageToken=page_token).execute()
        for event in events['items']:
            if((event['start']['dateTime'] < newRsv['start']['dateTime'] and event['end']['dateTime'] > newRsv['start']['dateTime']) or (newRsv['end']['dateTime'] < event['end']['dateTime'] and event['start']['dateTime'] < newRsv['end']['dateTime'])):
                flag = True
        page_token = events.get('nextPageToken')
        if not page_token:
            break 
    return flag
        
