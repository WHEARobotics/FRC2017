#!/usr/bin/env python3
"""
    WHEA Robotics 3881 code for FRC 2017.
#test
"""

import wpilib
import ctre

class MyRobot(wpilib.IterativeRobot):
    
    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        # Configure shooter motor controller.
        self.shooter = ctre.CANTalon(1) # Create a CANTalon object.
        self.shooter.setFeedbackDevice(ctre.CANTalon.FeedbackDevice.QuadEncoder) # Choose an encoder as a feedback device.  The default should be QuadEncoder already, but might as well make sure.
        # I thought the encoder was 20 pulses per revolution per phase, which would require "80" as an argument below, but after trying it, it looks like there are 12.
        # Setting this parameter changes things so getPosition() returns decimal revolutions, and getSpeed() returns RPM.
        self.shooter.configEncoderCodesPerRev(48)
        # resets shooter position on startup
        self.shooter.setPosition(0)
        self.shooter.enableBrakeMode(False) # This should change between brake and coast modes.
        
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
        """
        Programmer: Jun Hyung Lee
        Date: 2/9/17
        Description: The code below is unfinished, and purely experimental. Right now, it's set so that the robot drives forward and shoots
        balls into the goal. I'm unsure whether we'll have to rotate the robot before making a shot. :\
        """
        self.auto_loop_counter = 0
        #50 loops is equal to one second
        if self.auto_loop_counter < 100:
            self.robot_drive.drive(1, 0) #Drives forward at full speed 
            self.auto_loop_counter += 1
        else:
            self.robot_drive.drive(0, 0) #Stops the robot from moving forward
            auto_loop_counter_ = 0 
        if self.auto_loop_counter <50:
            self.shooter.setPosition(x) #I'm unsure about what value I should put in place of "x". Could I get some clarification on the parameters of the function?
            Shoot() #Shoot() would be a pre-defined function which would fire a ball from the shooter.
            self.auto_loop_counter += 1
        else:
            self.auto_loop_counter = 0
        #break
            #this isn't working, error says break is out of loop. Just fyi. -Hunter
        pass


    def teleopInit(self):
        #resets printed shooter position on enable
        self.shooter.setPosition(0)

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
       # self.drive.arcadeDrive(self.stick)
        # XBox controller: axis 1 = left Y, axis 5 = right Y
        self.drive.tankDrive(self.stick.getRawAxis(1),self.stick.getRawAxis(5))
        
        # Section to run the shooter at 0% to +10% full voltage, shooter axis(2), left trigger
        self.shooter.set(self.stick.getRawAxis(2)*0.1)
        
        self.counter += 1
        if self.counter % 90 == 0:
            # Uncomment whichever line you want to use.  Need to have a shooter to use the second one.
         #   print(self.counter)
            print(self.counter, 'axis: ', self.stick.getRawAxis(2), ' pos: ', self.shooter.getPosition(), ' rpm: ', self.shooter.getSpeed())


    def testPeriodic(self):
        """This function is called periodically during test mode."""
        wpilib.LiveWindow.run()


if __name__ == "__main__":
    wpilib.run(MyRobot)
