'''
Created on May 5, 2014

@author: oliver
'''
import datetime
import json

class ReservationClient(object):
    '''
    This class contains all the events that the calendar supports
    New events can be appended at the bottom
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
        
    def removeAll(self):
        '''Removes all the reservations from the calendar'''
        '''rename to remove_all'''
        self.service.calendars().clear(calendarId='primary').execute()

    def removeReservation(self,rsvId):
        '''Removes a specific reservation from the calendar. Requires the reservationID'''
        '''rename to remove'''
        print self.service.events().delete(calendarId='primary', eventId=rsvId, sendNotifications=True).execute()


    def viewReservationFromId(self,rsvId):
        '''displays the reservation object'''
        '''rename to get_from_id'''
        print self.service.events().get(calendarId='primary', eventId=rsvId).execute()
        
    def selectRsvIdsFromUser(self,userId):
        '''Selects all the reservations made by a user'''
        '''rename to get_by_user'''
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
        
    def getAll(self):
        '''Selects all reservations in the calendar '''
        '''rename to get_all'''
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
    
    def selectRsvIdFromLabel(self, labelStr):
        '''Assuming this label will return only one eventId'''
        '''rename get_from_label'''
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
        
    def lstUsrProjRsvSTimeETime(self, userId, projId, sTime,eTime):
        '''Lists all the users reservations made in a project from a start-time to a end time'''
        '''reanme list_by_user_and_project'''
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
    
    def lstRsvProj(self, projId):
        '''Lists all the reservations made in a particular project'''
        '''rename list_by_project'''
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
    
    def durationOfRsv(self, rsvId):
        '''Shows the duration of the reservation'''
        '''rename duration'''
        rsvEvent = self.service.events().get(calendarId='primary', eventId=rsvId).execute()
        duration = rsvEvent['start']['dateTime']- rsvEvent['end']['dateTime']
        return duration
        
      
def checkRsvOverlap(service, newRsv):
    '''rename check_overlap'''
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
        
