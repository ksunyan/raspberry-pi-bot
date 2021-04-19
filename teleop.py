from advanced_robot import AdvRobot
from picamera import PiCamera
from time import sleep, time
from os import mkdir
import curses

# Create instance AdvRobot
rbt = AdvRobot(left=(10,9),right=(8,7),pwr_coeffs=(1,0.95))

# Create instance PiCamera
camera = PiCamera()

# Launch curses window and change terminal settings
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

# Set default drive settings
power_setting = 0.7
power_increment = 0.05
turn_pwr_scalar = 0.7
accel_time = 1
accel_time_increment = 0.05
turn_accel_scalar = 0

# Set default camera settings
camera.resolution = (2592, 1944)
camera.framerate = 15

# Make a new directory (name based on current time) for photos
new_photo_directory = str(int(time()))
mkdir(new_photo_directory)

# Display default settings in window
stdscr.addstr("POWER: " + str(power_setting) + '\n')
stdscr.addstr("RAMP TIME (s): " + str(accel_time) + '\n')

# Loop to detect keypresses and control robot
while True:
	ch = stdscr.getch()

	if(ch == curses.KEY_BACKSPACE):
		break

	elif(ch == curses.KEY_UP):
		if(power_setting < (1-power_increment)):
			power_setting += power_increment
		else:
			power_setting = 1
		stdscr.erase()
		stdscr.addstr("POWER: " + str(power_setting) + '\n')
		stdscr.addstr("RAMP TIME (s): " + str(accel_time) + '\n')

	elif(ch == curses.KEY_DOWN):
		if(power_setting > (0+power_increment)):
			power_setting -= power_increment
		else:
			power_setting = 0
		stdscr.erase()
		stdscr.addstr("POWER: " + str(power_setting) + '\n')
		stdscr.addstr("RAMP TIME (s): " + str(accel_time) + '\n')

	elif(ch == curses.KEY_LEFT):
		if(accel_time > (0+accel_time_increment)):
			accel_time -= accel_time_increment
		else:
			accel_time = 0
		stdscr.erase()
		stdscr.addstr("POWER: " + str(power_setting) + '\n')
		stdscr.addstr("RAMP TIME (s): " + str(accel_time) + '\n')

	elif(ch == curses.KEY_RIGHT):
		if(accel_time < (1-accel_time_increment)):
			accel_time += accel_time_increment
		else:
			accel_time = 1
		stdscr.erase()
		stdscr.addstr("POWER: " + str(power_setting) + '\n')
		stdscr.addstr("RAMP TIME (s): " + str(accel_time) + '\n')

	elif(ch == ord('w')):
		rbt.forward(power_setting,accel_time)

	elif(ch == ord('s')):
		rbt.backward(power_setting,accel_time)

	elif(ch == ord('a')):
		rbt.leftTank((turn_pwr_scalar * power_setting),(turn_accel_scalar * accel_time))

	elif(ch == ord('d')):
		rbt.rightTank((turn_pwr_scalar * power_setting),(turn_accel_scalar * accel_time))

	elif(ch == ord('k')):
		rbt.leftPivot((turn_pwr_scalar * power_setting),(turn_accel_scalar * accel_time))

	elif(ch == ord('l')):
		rbt.rightPivot((turn_pwr_scalar * power_setting),(turn_accel_scalar * accel_time))

	elif(ch == ord(' ')):
		rbt.brake(accel_time)

	elif(ch == ord('p')):
		current_time = str(int(time()))
		camera.capture(new_photo_directory + '/' + current_time + '.jpg')
		stdscr.addstr("PHOTO CAPTURED at " + current_time + '\n')

	else:
		rbt.halt()

# Reset terminal settings to default and quit
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
quit()
