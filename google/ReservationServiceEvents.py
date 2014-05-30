'''
Created on Mar 6, 2014

@author: oliver
'''
from datetime import datetime

class ReservationClient(object):
    '''
    This class contains all the events that the calendar supports
    New events can be appended at the bottom
    '''

    def __init__(self, serviceArg):
        '''The init method takes in the service object an initializes it'''
        self.service = serviceArg
    
    def addEventToCalendar(self,event):
        '''An event is a JSON object that is passes to his method to be added to the calendar'''
        if(checkEventOverlap(self.service,event)==True):
            return "Event overlaps: cannot schedule at this time"
        else:
            completedEvent = self.service.events().insert(calendarId='primary', body=event).execute()
            return completedEvent['id']
        
    def removeAllEvents(self):
        '''Removes all the events from the calendar'''
        self.service.calendars().clear(calendarId='primary').execute()

    def removeEventFromCalendar(self,eventID):
        '''Removes a specific event from the calendar. Requires the eventID'''
        print self.service.events().delete(calendarId='primary', eventId=eventID, sendNotifications=True).execute()

        
    def selectAllEvents(self):
        '''Selects all events in the calendar '''
        eventsDict = dict()
        page_token = None
        i=0
        while True:
            events = self.service.events().list(calendarId='primary', pageToken=page_token).execute()
            for event in events['items']:
                innerDict = dict()
                innerDict['id'] = event['id']
                innerDict['label'] = event['summary']
                eventsDict['event' + str(i)] = innerDict
                i = i+1
            page_token = events.get('nextPageToken')
            if not page_token:
                break
        return eventsDict    
    
    def selectEventIdFromLabel(self, labelStr):
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
            
    def rescheduleEvent(self, oldEventId, newEvent):
        '''Used to update or modify an old event. Requires old event id and new Event object that will replace the old event'''
        self.service.events().update(calendarId='primary', eventId = oldEventId, body = newEvent).execute()
        
      
def checkEventOverlap(service, newEvent):
    page_token = None
    flag = False
    while True:
        events = service.events().list(calendarId='primary', pageToken=page_token).execute()
        for event in events['items']:
            if((event['start']['dateTime'] < newEvent['start']['dateTime'] and event['end']['dateTime'] > newEvent['start']['dateTime']) or (newEvent['end']['dateTime'] < event['end']['dateTime'] and event['start']['dateTime'] < newEvent['end']['dateTime'])):
                flag = True
        page_token = events.get('nextPageToken')
        if not page_token:
            break 
    return flag
        