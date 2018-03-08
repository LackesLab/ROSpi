import Adafruit_PCA9685

class Servos:
    pwm = None
    
    LEFT_SERVO = 0
    RIGHT_SERVO = 1
    FRONT_SERVO = 3
    
    LEFT_DOWN = 780
    LEFT_FORWARD = 480
    RIGHT_DOWN = 780
    RIGHT_FORWARD = 1090
    FRONT_FORWARD = 1400
    
    def __init__(self):
        # Initialization at address 0x40
        self.pwm = Adafruit_PCA9685.PCA9685()
    
    def set_servo(servo, value):
        self.pwm.set_pwm(servo, 0, value)
    
    def left_servo_down():
        self.set_servo(LEFT_SERVO, LEFT_DOWN)
    
    def right_servo_down():
        self.set_servo(RIGHT_SERVO, RIGHT_DOWN)
    
    def left_servo_forward():
        self.set_servo(LEFT_SERVO, LEFT_FORWARD)
    
    def right_servo_forward():
        self.set_servo(RIGHT_SERVO, RIGHT_FORWARD)
    
    def font_servo_forward():
        self.set_servo(FRONT_SERVO, FRONT_FORWARD)
    