
**********************************************************************
Manual Pages
**********************************************************************

reservation
======================================================================

::

   
       Usage:
           reservation --rst
           reservation --version
           reservation find [all]
                            [--user=USER_ID]
                            [--label=ID]
                            [--cm_id=ID]
           reservation list [--cm_id=CM_ID]
                            [--user=USER_ID]
                            [--project=PROJECT_ID]
                            [--label=STRING]
                            [--start=TIME_START]
                            [--end=TIME_END]
                            [--host=HOST]
                            [--summary=SUMMARY]
           reservation duration [--cm_id=CM_ID]
           reservation delete [all]
                              [--cm_id=CM_ID]
                              [--user=USER_ID]
                              [--project=PROJECT_ID]
                              [--label=STRING]
                              [--start=TIME_START]
                              [--end=TIME_END]
                              [--host=HOST]
           reservation update [--cm_id=CM_ID]
                              [--user=USER_ID]
                              [--project=PROJECT_ID]
                              [--label=STRING]
                              [--start=TIME_START]
                              [--end=TIME_END]
                              [--host=HOST]
                              [--summary=SUMMARY]
                              [--cm_id=CM_ID]
           reservation add --cm_id=CM_ID --user=USER_ID --project=PROJECT_ID --label=STRING --start=TIME_START --end=TIME_END --host=HOST --summary=SUMMARY
           reservation add --file=FILE
   
       Options:
           --rst                 print an rst manul page
           --version             print the version
           --label=STRING        label id reservation
           --cm_id=CM_ID         reservation cloudmesh id
           --user=USER_ID        user id
           --project=PROJECT_ID  project id
           --start=TIME_START    Start time of the reservation, in
                                 YYYY/MM/DD HH:MM:SS format. [default: 1901-01-01]
           --end=TIME_END        End time of the reservation, in
                                 YYYY/MM/DD HH:MM:SS format. In addition a duration
                                 can be specified if the + sign is the first sign.
                                 The duration will than be added to
                                 the start time. [default: 2100-12-31]
           --host=HOST           host number 
           --summary=SUMMARY     summary of the reservation
           --file=FILE           Adding multiple reservations from one file
   
   
       
generate
======================================================================

::

   
       Usage:
           generate -h | --help | --rst
           generate clean
           generate SERVERS RESERVATIONS DURATION START
           generate list [--json|--table|--calendar]
   
       Arguments:
           SERVERS       Number of servers for which we generate 
                         reservations
           RESERVATIONS  Number of reservations per server
           DURATION      The maximum duration of a reservation 
                         (determined randomly)
           START         The start date. if now is specified, the current
                         time is used, otherwise an offset is used in the
                         form of 1m, or 1h, or 1w[default: now]
   
       Description:
   
           This program generates a number of reservations so they can be
           used to test the reservation package.
   
           generate clean
               deletes all reservations from the reservation database
   
           generate SERVERS RESERVATIONS DURATION
               generates a number of reservations where the servers are
               specified as hostlist (e.g. i[001-003]. The reservations
               specifies how many reservations there will be for each
               server. The duration is a random number between [0,duration]
               that specified not only a duration, but also the time delta
               between two reservations on the same host.
   
           generate list
               retiurns the list of reservations in the specified
               format. Thoe format can be list, table, or calendar
   
       Bugs:
           Not implemented:
   
           * clean 
           * list
           * the generation function does not yet have a start date
   
       See Also:
           * https://pypi.python.org/pypi/pytimeparse/1.1.0
   
       
