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
    
    def add(self,reservation):
        '''A reservation is a JSON object that is passes to his method to be added to the calendar'''
        completedReservation = self.service.events().insert(calendarId='primary', body=reservation).execute()
        return completedReservation['id']
        
    def removeAll(self):
        '''Removes all the reservations from the calendar'''
        self.service.calendars().clear(calendarId='primary').execute()

    def removeReservation(self,reservationID):
        '''Removes a specific reservation from the calendar. Requires the reservationID'''
        print self.service.events().delete(calendarId='primary', eventId=reservationID, sendNotifications=True).execute()

    def getAll(self):
        '''Selects all reservations in the calendar '''
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
    
    def selectReservationIdFromLabel(self, labelStr):
        '''Assuming this label will return only one reservationID'''
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
            
    def reschedule(self, oldReservationId, newReservation):
        '''Used to update or modify an old reservation. Requires old reservation id and new reservation object that will replace the old event'''
        self.service.events().update(calendarId='primary', eventId = oldReservationId, body = newReservation).execute()
        
