from tkinter import LEFT
from MotorModule import Motor
import KeyPressModule as kp

motor= Motor(2,3,4,17,22,27)

kp.init()
 
def main():
    if(kp.getKey("UP")):
        motor.move(0.6,0 ,0.1)
        print("Tiến\n")
    elif(kp.getKey("DOWN")):
        motor.move(-0.6, 0, 0.1)
        print("Lùi\n")
    elif(kp.getKey("LEFT")):
        motor.move(0.5,0.2,0.1)
        print("Trái\n")
    elif(kp.getKey("RIGNT")):
         motor.move(0.5, -0.2, 0.1)
         print("Phải\n")
    else:    
        motor.stop(2)
        print("Dừng\n")
 
if __name__ == '__main__':
    while True:
        main()