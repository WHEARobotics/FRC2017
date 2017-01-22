#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on.
"""

import wpilib

class MyRobot(wpilib.IterativeRobot):
    
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        l_motor = wpilib.Spark(1)
        l_motor.setInverted(True)
        r_motor = wpilib.Jaguar(0)
        r_motor.setInverted(True)
        self.stick = wpilib.Joystick(0)
        self.drive = wpilib.RobotDrive(l_motor, r_motor)
        self.counter = 0


    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.auto_loop_counter = 0

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        pass


    def teleopInit(self):
        pass

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.drive.arcadeDrive(self.stick)
        self.counter += 1
        if self.counter % 90 == 0:
            print(self.counter)


    def testPeriodic(self):
        """This function is called periodically during test mode."""
        wpilib.LiveWindow.run()


if __name__ == "__main__":
    wpilib.run(MyRobot)
