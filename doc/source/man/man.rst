**********************************************************************
Manual Pages
**********************************************************************

reservation
======================================================================

::

   
   Usage:
       reservation -h | --help
       reservation --rst
       reservation --version
       reservation add [--start=TIME_START]
                       [--end=TIME_END]
                       LABEL
                       HOSTS
       reservation add --file=FILE
       reservation list [--start=TIME_START]
                        [--end=TIME_END]
                        [--format=FORMAT]
       reservation id (LABELS|IDS)
       reservation [-i] rm (LABELS|IDS)
       reservation [-i] delete (LABELS|IDS)     
       
   Arguments:
       ID        the unique ID of the reservation
       LABEL     the label of a host
       
   Options:
       --label=LABEL  the label pf the reservation
       -f FILE, --file=FILE  file to be specified
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
   
