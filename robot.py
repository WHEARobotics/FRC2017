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
        self.stick = wpilib.Joystick(1)
        self.drive = wpilib.RobotDrive(self.l_motor, self.r_motor)
        self.counter = 0


    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.auto_loop_counter = 0
        self.shooter.setPosition(0)

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
#WARNING : robotpy             : Robots don't quit! 
#ERROR   : wpilib.ds           : ERROR Unhandled exception 
#ERROR  1  ERROR Unhandled exception  /usr/local/lib/python3.6/site-packages/wpilib/_impl/main.py.134:run 
#ERROR Unhandled exception 
#ERROR   : robotpy             : ---> The startCompetition() method (or methods called by it) should have handled the exception. 
#This is the error I recived when I tried testing it without the shooter code, again just an fyi. -Hunter

        if self.auto_loop_counter <50:
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
        self.drive.arcadeDrive(self.stick)
      #  XBox controller: axis 1 = left Y, axis 5 = right Y
       # self.drive.tankDrive(self.stick.getRawAxis(1),self.stick.getRawAxis(5))
        
        # Section to run the shooter at 0% to +10% full voltage, shooter axis(2), left trigger
        #self.shooter.set(self.stick.getRawAxis(2)*0.2)
         self.shooter.set(self.stick.getRawButton(1)*0.2)
        #Here is the code Rod wanted to have us test -Hunter
        #self.shooter.set(self.stick.getRawAxis(3)*0.2)
        #(1)The above code works perfectly
        #self.shooter.set((self.stick.getRawButton(1)*0.2) , (self.stick.getRawButton(2)*0.1))
        #(2)The above code does not work
        #self.shooter.set(self.stick.getRawButton(1)*0.2)
        #self.shooter.set(self.stick.getRawButton(2)*-0.1)
        #(2)For the above code, button 2 works, but not button 1



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
