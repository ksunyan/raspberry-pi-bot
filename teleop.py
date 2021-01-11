from advanced_robot import AdvRobot
from time import sleep

rbt = AdvRobot(left=(10,9),right=(8,7),pwr_coeffs=(1,0.95))

# Testing code
rbt.forward(1)
sleep(2)
rbt.halt()