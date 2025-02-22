import vex

# Initialize Brain and Controller
brain = vex.Brain()
controller = vex.Controller(vex.ControllerType.PRIMARY)

# Initialize motors (two per side for drivetrain, one for conveyor belt)
left_motor_1 = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO18_1, False)
left_motor_2 = vex.Motor(vex.Ports.PORT18, vex.GearSetting.RATIO18_1, False)
right_motor_1 = vex.Motor(vex.Ports.PORT8, vex.GearSetting.RATIO18_1, True)
right_motor_2 = vex.Motor(vex.Ports.PORT20, vex.GearSetting.RATIO18_1, True)
conveyor_motor = vex.Motor(vex.Ports.PORT15, vex.GearSetting.RATIO18_1, False)

# Group motors for easier drivetrain control
left_drive = vex.MotorGroup(left_motor_1, left_motor_2)
right_drive = vex.MotorGroup(right_motor_1, right_motor_2)

# Create Competition instance
competition = vex.Competition()

def autonomous():
    """Autonomous Routine"""
    brain.screen.print("Autonomous Running")
    
    # Example autonomous movement
    left_drive.set_velocity(50, vex.VelocityUnits.PCT)
    right_drive.set_velocity(50, vex.VelocityUnits.PCT)
    left_drive.spin(vex.DirectionType.FWD)
    right_drive.spin(vex.DirectionType.FWD)
    vex.wait(2000, vex.TimeUnits.MSEC)
    left_drive.stop()
    right_drive.stop()

def driver_control():
    """Driver Control Period"""
    brain.screen.print("Driver Control Running")
    
    while True:
        # Get joystick values
        forward = controller.axis3.position()
        turn = controller.axis1.position()
        
        # Calculate motor speeds
        left_speed = forward + turn
        right_speed = forward - turn
        
        # Set motor speeds
        left_drive.set_velocity(left_speed, vex.VelocityUnits.PCT)
        right_drive.set_velocity(right_speed, vex.VelocityUnits.PCT)
        left_drive.spin(vex.DirectionType.FWD)
        right_drive.spin(vex.DirectionType.FWD)
        
        # Conveyor belt control
        if controller.buttonL1.pressing():
            conveyor_motor.set_velocity(100, vex.VelocityUnits.PCT)
            conveyor_motor.spin(vex.DirectionType.FWD)
        elif controller.buttonR1.pressing():
            conveyor_motor.set_velocity(100, vex.VelocityUnits.PCT)
            conveyor_motor.spin(vex.DirectionType.REV)
        else:
            conveyor_motor.stop(vex.BrakeType.HOLD)
        
        # Allow time for other tasks to run
        vex.wait(20, vex.TimeUnits.MSEC)

# Register autonomous and driver control functions
competition.autonomous(autonomous)
competition.drivercontrol(driver_control)
