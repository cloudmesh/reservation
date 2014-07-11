"""
Examples:

  nosetests -v --nocapture

  nosetests -v

"""

from cloudmesh_common.util import banner
from reservation.cli import shell_command_reservation, reservation_connect
from docopt import docopt
import inspect

def HEADING(txt=None,c="#"):
    """
    Prints a message to stdout with #### surrounding it. This is useful for
    nosetests to better distinguish them.

    :param txt: a text message to be printed
    :type txt: string
    """
    if txt is None:
        txt = inspect.getouterframes(inspect.currentframe())[1][3]

    banner(txt,c)

    
class Test_reservation_cli:

    def setup(self):
        HEADING(c="-")
        self.connect()
        assert self.db is not None
                    
    def teardown(self):
        pass

    def connect(self):
        self.db = reservation_connect()
        assert self.db is not None
        
    def test_connect_to_mongo(self):
        HEADING()
        if self.db is None:       
            assert False
        else:
            assert True


    def test_reading_docopt_from_shell_command_reservation(self):
        HEADING()
        try:
            arguments = docopt(shell_command_reservation.__doc__)
            assert True
        except:
            assert False
