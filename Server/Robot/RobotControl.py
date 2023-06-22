import random
import time
from ev3dev2.motor import MediumMotor
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.sensor import INPUT_1, INPUT_3, INPUT_4
from ev3dev2.motor import MoveTank, SpeedPercent
from ev3dev2.sensor.lego import UltrasonicSensor

class RobotControl:
    def __init__(self):
        self.tank = MoveTank(OUTPUT_D, OUTPUT_A)
        self.frontClaw = MediumMotor(OUTPUT_C)
        self.backClaw = MediumMotor(OUTPUT_B)
        self.ballSensor = UltrasonicSensor(INPUT_4)
        self.wallSensor = UltrasonicSensor(INPUT_3)
        self.begin = False
    
    def execute(self, command):
        if (command == "start"):
            self.begin = True
            picking_up = False
            while self.begin:
                if not picking_up and self.ballSensor.distance_centimeters <= 15:
                    picking_up = True
                    self.tank.stop()
                    self.pick_up()
                    picking_up = False
                    self.tank.on(SpeedPercent(25), SpeedPercent(25))
                elif not picking_up and self.wallSensor.distance_centimeters <= 20:
                    self.tank.stop()
                    turn = random.choice(["left", "right"])
                    if (turn == "left"):
                        self.tank.on_for_seconds(SpeedPercent(-25), SpeedPercent(-25))
                        self.tank.on_for_seconds(SpeedPercent(-25), SpeedPercent(25), 1)
                    else:
                        self.tank.on_for_seconds(SpeedPercent(-25), SpeedPercent(-25))
                        self.tank.on_for_seconds(SpeedPercent(25), SpeedPercent(-25), 1)
                elif not picking_up:
                    self.tank.on_for_seconds(SpeedPercent(25), SpeedPercent(25))
        elif (command == "stop"):
            self.begin = False
            self.tank.stop()
    
    def pick_up(self):
        self.frontClaw.on_for_seconds(SpeedPercent(-35), 3.5)
        time.sleep(2)
        self.frontClaw.on_for_seconds(SpeedPercent(35), 3.5)
    
    def release(self):
        self.backClaw.on_for_seconds(SpeedPercent(35), 3)
        time.sleep(8)
        self.backClaw.on_for_seconds(SpeedPercent(-35), 3)
    
    def stop(self):
        self.tank.stop()




