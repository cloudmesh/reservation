Python API
----------------------------------------------------------------------

The Python API contains the following functions to work with the Google Calendar:
Our current version uses only JSON objects to pass to the calendar.

  * The addEventToCalendar():
      Arguments: event object
      return value: -
  
  * removeEventFromCalendar():
      Argument: EventId (Integer)
  
  * removeAllEvents():
      This removes all the events from the primary calendar.
  
  * selectAllEvents():
      This lists all the events from the primary calendar.
  
  * rescheduleEvent(oldEventId, newEvent):
      Used to update or modify an old event.
          Args: oldEventId (Integer)
          newEvent (JSON object)
        
  * Specification of the entire JSON Calendar object: Referenced from the google documentation.
      The Json Object must adhere to the following standard.
  
  {
      "creator": { # The creator of the event. Read-only.
        "self": false, # Whether the creator corresponds to the calendar on which this copy of the event appears. Read-only. The default is False.
        "displayName": "A String", # The creator's name, if available.
        "email": "A String", # The creator's email address, if available.
        "id": "A String", # The creator's Profile ID, if available.
      },
      "originalStartTime": { # For an instance of a recurring event, this is the time at which this event would start according to the recurrence data in the recurring event identified by recurringEventId. Immutable.
        "date": "A String", # The date, in the format "yyyy-mm-dd", if this is an all-day event.
        "timeZone": "A String", # The name of the time zone in which the time is specified (e.g. "Europe/Zurich"). Optional. The default is the time zone of the calendar.
        "dateTime": "A String", # The time, as a combined date-time value (formatted according to RFC 3339). A time zone offset is required unless a time zone is explicitly specified in 'timeZone'.
      },
      "organizer": { # The organizer of the event. If the organizer is also an attendee, this is indicated with a separate entry in 'attendees' with the 'organizer' field set to True. To change the organizer, use the "move" operation. Read-only, except when importing an event.
        "self": false, # Whether the organizer corresponds to the calendar on which this copy of the event appears. Read-only. The default is False.
        "displayName": "A String", # The organizer's name, if available.
        "email": "A String", # The organizer's email address, if available.
        "id": "A String", # The organizer's Profile ID, if available.
      },
      "id": "A String", # Identifier of the event.
      "hangoutLink": "A String", # An absolute link to the Google+ hangout associated with this event. Read-only.
      "attendees": [ # The attendees of the event.
        {
          "comment": "A String", # The attendee's response comment. Optional.
          "displayName": "A String", # The attendee's name, if available. Optional.
          "self": True or False, # Whether this entry represents the calendar on which this copy of the event appears. Read-only. The default is False.
          "id": "A String", # The attendee's Profile ID, if available.
          "email": "A String", # The attendee's email address, if available. This field must be present when adding an attendee.
          "additionalGuests": 42, # Number of additional guests. Optional. The default is 0.
          "resource": True or False, # Whether the attendee is a resource. Read-only. The default is False.
          "organizer": True or False, # Whether the attendee is the organizer of the event. Read-only. The default is False.
          "optional": True or False, # Whether this is an optional attendee. Optional. The default is False.
          "responseStatus": "A String", # The attendee's response status. Possible values are:
              # - "needsAction" - The attendee has not responded to the invitation.
              # - "declined" - The attendee has declined the invitation.
              # - "tentative" - The attendee has tentatively accepted the invitation.
              # - "accepted" - The attendee has accepted the invitation.
        },
      ],
      "source": { # Source of an event from which it was created; for example a web page, an email message or any document identifiable by an URL using HTTP/HTTPS protocol. Accessible only by the creator of the event.
        "url": "A String", # URL of the source pointing to a resource. URL's protocol must be HTTP or HTTPS.
        "title": "A String", # Title of the source; for example a title of a web page or an email subject.
      },
      "htmlLink": "A String", # An absolute link to this event in the Google Calendar Web UI. Read-only.
      "recurrence": [ # List of RRULE, EXRULE, RDATE and EXDATE lines for a recurring event. This field is omitted for single events or instances of recurring events.
        "A String",
      ],
      "start": { # The (inclusive) start time of the event. For a recurring event, this is the start time of the first instance.
        "date": "A String", # The date, in the format "yyyy-mm-dd", if this is an all-day event.
        "timeZone": "A String", # The name of the time zone in which the time is specified (e.g. "Europe/Zurich"). Optional. The default is the time zone of the calendar.
        "dateTime": "A String", # The time, as a combined date-time value (formatted according to RFC 3339). A time zone offset is required unless a time zone is explicitly specified in 'timeZone'.
      },
      "etag": "A String", # ETag of the resource.
      "location": "A String", # Geographic location of the event as free-form text. Optional.
      "recurringEventId": "A String", # For an instance of a recurring event, this is the event ID of the recurring event itself. Immutable.
      "extendedProperties": { # Extended properties of the event.
        "shared": { # Properties that are shared between copies of the event on other attendees' calendars.
          "a_key": "A String", # The name of the shared property and the corresponding value.
        },
        "private": { # Properties that are private to the copy of the event that appears on this calendar.
          "a_key": "A String", # The name of the private property and the corresponding value.
        },
      },
      "status": "A String", # Status of the event. Optional. Possible values are:
          # - "confirmed" - The event is confirmed. This is the default status.
          # - "tentative" - The event is tentatively confirmed.
          # - "cancelled" - The event is cancelled.
      "updated": "A String", # Last modification time of the event (as a RFC 3339 timestamp). Read-only.
      "description": "A String", # Description of the event. Optional.
      "iCalUID": "A String", # Event ID in the iCalendar format.
      "gadget": { # A gadget that extends this event.
        "preferences": { # Preferences.
          "a_key": "A String", # The preference name and corresponding value.
        },
        "title": "A String", # The gadget's title.
        "height": 42, # The gadget's height in pixels. Optional.
        "width": 42, # The gadget's width in pixels. Optional.
        "link": "A String", # The gadget's URL.
        "type": "A String", # The gadget's type.
        "display": "A String", # The gadget's display mode. Optional. Possible values are:
            # - "icon" - The gadget displays next to the event's title in the calendar view.
            # - "chip" - The gadget displays when the event is clicked.
        "iconLink": "A String", # The gadget's icon URL.
      },
      "endTimeUnspecified": false, # Whether the end time is actually unspecified. An end time is still provided for compatibility reasons, even if this attribute is set to True. The default is False.
      "sequence": 42, # Sequence number as per iCalendar.
      "visibility": "default", # Visibility of the event. Optional. Possible values are:
          # - "default" - Uses the default visibility for events on the calendar. This is the default value.
          # - "public" - The event is public and event details are visible to all readers of the calendar.
          # - "private" - The event is private and only event attendees may view event details.
          # - "confidential" - The event is private. This value is provided for compatibility reasons.
      "guestsCanModify": false, # Whether attendees other than the organizer can modify the event. Optional. The default is False.
      "end": { # The (exclusive) end time of the event. For a recurring event, this is the end time of the first instance.
        "date": "A String", # The date, in the format "yyyy-mm-dd", if this is an all-day event.
        "timeZone": "A String", # The name of the time zone in which the time is specified (e.g. "Europe/Zurich"). Optional. The default is the time zone of the calendar.
        "dateTime": "A String", # The time, as a combined date-time value (formatted according to RFC 3339). A time zone offset is required unless a time zone is explicitly specified in 'timeZone'.
      },
      "attendeesOmitted": false, # Whether attendees may have been omitted from the event's representation. When retrieving an event, this may be due to a restriction specified by the 'maxAttendee' query parameter. When updating an event, this can be used to only update the participant's response. Optional. The default is False.
      "kind": "calendar#event", # Type of the resource ("calendar#event").
      "locked": false, # Whether this is a locked event copy where no changes can be made to the main event fields "summary", "description", "location", "start", "end" or "recurrence". The default is False. Read-Only.
      "created": "A String", # Creation time of the event (as a RFC 3339 timestamp). Read-only.
      "colorId": "A String", # The color of the event. This is an ID referring to an entry in the "event" section of the colors definition (see the "colors" endpoint). Optional.
      "anyoneCanAddSelf": false, # Whether anyone can invite themselves to the event. Optional. The default is False.
      "reminders": { # Information about the event's reminders for the authenticated user.
        "overrides": [ # If the event doesn't use the default reminders, this lists the reminders specific to the event, or, if not set, indicates that no reminders are set for this event.
          {
            "minutes": 42, # Number of minutes before the start of the event when the reminder should trigger.
            "method": "A String", # The method used by this reminder. Possible values are:
                # - "email" - Reminders are sent via email.
                # - "sms" - Reminders are sent via SMS.
                # - "popup" - Reminders are sent via a UI popup.
          },
        ],
        "useDefault": True or False, # Whether the default reminders of the calendar apply to the event.
      },
      "guestsCanSeeOtherGuests": true, # Whether attendees other than the organizer can see who the event's attendees are. Optional. The default is True.
      "summary": "A String", # Title of the event.
      "guestsCanInviteOthers": true, # Whether attendees other than the organizer can invite others to the event. Optional. The default is True.
      "transparency": "opaque", # Whether the event blocks time on the calendar. Optional. Possible values are:
          # - "opaque" - The event blocks time on the calendar. This is the default value.
          # - "transparent" - The event does not block time on the calendar.
      "privateCopy": false, # Whether this is a private event copy where changes are not shared with other copies on other calendars. Optional. Immutable. The default is False.
    }
  
