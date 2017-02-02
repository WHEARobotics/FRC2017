#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on.
"""

import wpilib
import ctre

class MyRobot(wpilib.IterativeRobot):
    
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.l_motor = ctre.CANTalon(2)
        self.l_motor.setInverted(True)
        self.r_motor = ctre.CANTalon(3)
        self.r_motor.setInverted(True)
        self.stick = wpilib.Joystick(0)
        self.drive = wpilib.RobotDrive(self.l_motor, self.r_motor)
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
        #self.drive.arcadeDrive(self.stick)
        self.drive.tankDrive(self.stick.getRawAxis(1),self.stick.getRawAxis(5))
        self.counter += 1
        if self.counter % 90 == 0:
            print(self.counter)


    def testPeriodic(self):
        """This function is called periodically during test mode."""
        wpilib.LiveWindow.run()


if __name__ == "__main__":
    wpilib.run(MyRobot)
