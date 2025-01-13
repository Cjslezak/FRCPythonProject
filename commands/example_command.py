from commands2 import Command


class ExampleCommand(Command):
    def __init__(self):
        super().__init__()
        self.started = False

    def initialize(self):
        """Insert code to be run when command is initially called"""
        pass

    def execute(self):
        """Insert code to run while command is scheduled"""
        self.started = True

    def end(self, interrupted):
        """Insert code to be run when the command is completed."""
        pass

    def isFinished(self):
        """Insert code that decides if the command is finished running"""
        if self.started:
            return True
        else:
            return False
