import wpilib
from wpilib import drive, SmartDashboard
import magicbot
from commands2 import CommandScheduler, InstantCommand
from commands2.button import CommandXboxController


class MyRobot(magicbot.MagicRobot):
    robotController: CommandXboxController

    def createObjects(self):
        # Create motors and stuff here
        self.robotController = CommandXboxController(0)
        self.robotController.a().onTrue(InstantCommand(lambda: SmartDashboard.putBoolean("A button", 1)))
        self.robotController.a().onFalse(InstantCommand(lambda: SmartDashboard.putBoolean("A button", 0)))

    def autonomousInit(self):
        # Runs when auton starts
        pass

    def teleopInit(self):
        # Called when teleop starts; optional
        pass

    def teleopPeriodic(self):
        # Called every 20ms when teleop runs
        pass

    def robotPeriodic(self):
        # Called every 20ms in each run mode.
        super().robotPeriodic()
        CommandScheduler.getInstance().run()
