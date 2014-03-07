'''
Created on Mar 6, 2014

@author: oliver
'''

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
        self.service.events().insert(calendarId='primary', body=event).execute()
        
    def removeAllEvents(self):
        '''Removes all the events from the calendar'''
        self.service.calendars().clear(calendarId='primary').execute()

    def removeEventFromCalendar(self,eventID):
        '''Removes a specific event from the calendar. Requires the eventID'''
        print self.service.events().delete(calendarId='primary', eventId=eventID, sendNotifications=True).execute()

    def selectAllEvents(self):
        '''Selects all events in the calendar '''
        page_token = None
        while True:
            events = self.service.events().list(calendarId='primary', pageToken=page_token).execute()
            for event in events['items']:
                print event['id'],"--",event['summary']
            page_token = events.get('nextPageToken')
            if not page_token:
                break
            
    def rescheduleEvent(self, oldEventId, newEvent):
        '''Used to update or modify an old event. Requires old event id and new Event object that will replace the old event'''
        self.service.events().update(calendarId='primary', eventId = oldEventId, body = newEvent).execute()