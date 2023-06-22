import time
from ev3dev2.motor import MediumMotor
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.motor import MoveTank, SpeedPercent, SpeedRPS
from ev3dev2.sensor.lego import UltrasonicSensor

class RobotControl:
    def __init__(self):
        self.tank = MoveTank(OUTPUT_D, OUTPUT_A)
        self.frontClaw = MediumMotor(OUTPUT_C)
        self.backClaw = MediumMotor(OUTPUT_B)
    
    def execute(self, command, duration):
        if (command == "forward"):
            self.tank.on_for_seconds(SpeedPercent(25), SpeedPercent(25), duration)
        elif (command == "reverse"):
            self.tank.on_for_seconds(SpeedPercent(-25), SpeedPercent(-25), duration)
        elif (command == "left"):
            self.tank.on_for_seconds(SpeedPercent(-25), SpeedPercent(25), duration)
        elif (command == "right"):
            self.tank.on_for_seconds(SpeedPercent(25), SpeedPercent(-25), duration)
        elif (command == "grab"):
            self.frontClaw.on_for_seconds(SpeedRPS(-1000/360), duration)
            time.sleep(2)
            self.frontClaw.on_for_seconds(SpeedRPS(1000/360), duration)
        elif (command == "release"):
            self.backClaw.on_for_seconds(SpeedRPS(700/360), duration)
            time.sleep(8)
            self.backClaw.on_for_seconds(SpeedRPS(-700/360), duration)
        else:
            print("Unknown command")
        
    def stop(self):
        self.tank.stop()