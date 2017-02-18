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
        self.shooter.enableBrakeMode(False)# This should change between brake and coast modes.
        
        
        self.l_motor = ctre.CANTalon(3)
        self.l_motor.setInverted(True)
        self.r_motor = ctre.CANTalon(2)
        self.r_motor.setInverted(True)
        #self.stick = wpilib.Joystick(0)
        self.l_joy = wpilib.Joystick(0)
        self.r_joy = wpilib.Joystick(1)
        #self.gatherer = wpilib.Spark(0)
        #print (self.stick.getName())
        self.drive = wpilib.RobotDrive(self.l_motor , self.r_motor)
        self.counter = 0

        #Section for Init Mode Function
        self.mode = 0
        

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.auto_loop_counter = 0
        self.shooter.setPosition(0)
    

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""
        
        if self.auto_loop_counter <50:
            self.robot_drive.drive(0,1)

        elif self.auto_loop_counter >=50 and self.auto_loop_counter <100:
            self.robot_drive.drive(1,1)

        elif self.auto_loop_counter >=100 and self.auto_loop_counter <150:
            self.shooter.set(x)

        elif self.auto_loop_counter >=200 and self.auto_loop_counter <250:
            self.robot_drive.drive(-1,-1)

        #This stops the robot at 14.5 seconds
        #elif self.auto_loop_counter >=(725):
            #self.robot_drive.drive(0,0)

        else:
            self.robot_drive.drive(0,0)

        self.auto_loop_counter +=1
        #This counter runs 50 times a second      
            
            
            
            


    def teleopInit(self):
        #resets printed shooter position on enable
        self.shooter.setPosition(0)
        

    def teleopPeriodic(self):
    """This function is called periodically during operator control."""
        #self.drive.arcadeDrive(self.stick)
       #  XBox controller: axis 1 = left Y, axis 5 = right Y
       # self.drive.tankDrive(self.stick.getRawAxis(1),self.stick.getRawAxis(5))
        
        # Section to run the shooter at 0% to +10% full voltage, shooter axis(2), left trigger
        #self.shooter.set(self.stick.getRawAxis(2)*0.2)
        #self.shooter.set(self.stick.getRawButton(1)*0.2)
        #Here is the code Rod wanted to have us test -Hunter
        #self.shooter.set(self.stick.getRawAxis(3)*0.2)
        #(1)The above code works perfectly
        #self.shooter.set((self.stick.getRawButton(1)*0.2) , (self.stick.getRawButton(2)*0.1))
        #(2)The above code does not work
        #self.shooter.set(self.stick.getRawButton(1)*0.2)
        #self.shooter.set(self.stick.getRawButton(2)*-0.1)
        #(2)For the above code, button 2 works, but not button 1
        
        #self.stick = wpilib.Joystick(0)
        #self.stick = wpilib.Joystick(1)
        #Section for Mode Control
        #Select=Drive mode, Start=Shoot mode
        #if self.mode ==0:
            #self.mode
        if self.l_joy.getRawButton(4) or self.r_joy.getRawButton(4):
            self.mode = 1

        if self.l_joy.getRawButton(5) or self.r_joy.getRawButton(5):
            self.mode = 2

        if self.mode == 1:
            #self.drive.tankDrive(wpilib.Joystick(0).getRawAxis(1),wpilib.Joystick(1).getRawAxis(1))
            self.drive.tankDrive(self.l_joy.getRawAxis(1) , self.r_joy.getRawAxis(1))
        #else: self.mode ==0

        if self.mode == 2:
            if self.l_joy.getRawButton(1) or self.r_joy.getRawButton(1):
                self.shooter.set(1)
            else:
                self.shooter.set(0)
            #self.shooter.set(self.l_joy.getRawButton(1) or self.r_joy(1).getRawButton(1))
       # else: self.mode ==0
        
        #self.gatherer.set(self.l_joy and self.r_joy.getRawButton(3)*1)
        if self.l_joy.getRawButton(3) or self.r_joy.getRawButton(3):
            self.shooter.set(1)
        else:
            self.shooter.set(0)
        
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
