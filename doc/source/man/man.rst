['../reservation/reservation.py', '--rst']
**********************************************************************
Manual Pages
**********************************************************************

reservation
======================================================================

::

   
   Usage:
       reservation -h | --help | --rst
       reservation --version
       reservation login
       reservation add [--start=TIME_START]
                       [--end=TIME_END]
                       LABEL
                       HOSTS
       reservation add --file=FILE
       reservation remove --reservation=ID
       reservation remove --user=ID    
       reservation remove --all
       reservation get [--all]
       reservation get --label=LABEL
       reservation get --user=ID
       reservation get --reservation=ID    
       reservation reschedule --reservation=ID --file=FILE
       reservation duration --reservation=ID
       reservation list --project=PROJECT_ID
       reservation list [--user_id=USER_ID]
                        [--project_id=PROJ_ID]
                        [--start=TIME_START]
                        [--end=TIME_END]
                        [--format=FORMAT]
       reservation id (LABELS|IDS)
       reservation [-i] rm (LABELS|IDS)
       reservation [-i] delete (LABELS|IDS)     
       
   Arguments:
       ID        the unique ID of the reservation
       
   Options:
       --label=LABEL  the label pf the reservation
       -f FILE, --file=FILE  file to be specified
       --reservation_id=RESERVATION_ID                RESERVATION_ID
       --hosts=HOSTS        SERVER NUMBERS
       --user_id=USER_ID                USER_ID
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
       --format=FORMAT        Format of the output json, cfg. [default:json]
   
