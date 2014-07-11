from cmd3.shell import function_command
from reservation.cli import shell_command_reservation

class cm_shell_reservation:
    
    def activate_cm_shell_reservation(self):
        self.register_command_topic('cloud','reservation')
        pass

    @function_command(shell_command_reservation)
    def do_reservation(self, args, arguments):
        shell_command_reservation(arguments)
        pass

#    def __reservation__(self):
#        pass
#
#if __name__ == '__main__':
#    command = cm_reservation()
#    command.do_reservation("")
