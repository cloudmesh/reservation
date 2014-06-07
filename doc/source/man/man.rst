************************************************************
Manual Pages
************************************************************

reservation
======================================================================

::

   
   Usage:
       reservation -h | --help | --rst
       reservation --version
       reservation login
       reservation admin add [--start=TIME_START]
                             [--end=TIME_END]
                             [--user=ID]
                             LABEL
                             HOSTS
       reservation admin remove --user=USER_ID --reservation=RESERVATION_IDS
       reservation admin add --file=FILE
       reservation add [--start=TIME_START]
                       [--end=TIME_END]
                       LABEL
                       HOSTS
       reservation add --file=FILE [--start=TIME_START]
                                   [--end=TIME_END]
       reservation remove --reservation=IDS [--start=TIME_START]
                                            [--end=TIME_END]
       reservation remove --all [--start=TIME_START]
                                [--end=TIME_END]
       reservation list [--reservation=RESERVATION_IDS]   
                        [--project=PROJECT_IDS]
                        [--label=LABELS]
                        [--user=USER_IDS]
                        [--format=FORMAT]
                        [--start=TIME_START]
                        [--end=TIME_END]
                        [--fileds=FIELDS]
       reservation reschedule --reservation=ID --file=FILE
       reservation find -n RESOURCES -d DURATION
       		         [--start=TIME_START]
                        [--end=TIME_END]     
       reservation find -s SERVERS -d DURATION
       		         [--start=TIME_START]
                        [--end=TIME_END]     
       
   Arguments:
       ID        the unique ID of the reservation
       
   Options:
       LABEL  the label pf the reservation
       -f FILE, --file=FILE  file to be specified
       --reservation=RESERVATION_ID                RESERVATION_ID
       HOSTS        SERVER NUMBERS
       --user=USER_ID                USER_ID
       --proj_id=PROJ_ID                PROJ_ID
       -i           interactive mode adds a yes/no 
                    question for each host specified
       --start=TIME_START     Start time of the reservation, in 
                              YYYY/MM/DD HH:MM:SS format. [default: current_time]
       --end=TIME_END         End time of the reservation, in 
                              YYYY/MM/DD HH:MM:SS format. In addition a duration
                              can be specified if the + sign is the first sign.
                              The duration will than be added to
                              the start time. [default: +1d]
       --format=FORMAT        Format of the output table, json, cfg. [default: table]
   
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
   
   
