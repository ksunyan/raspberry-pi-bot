# A Python module containing the AdvRobot class.
# For more nuanced control over a Raspberry Pi powered robot.
# Copyright 2021, Kenneth S. Yan (ksunyan)

from gpiozero import Motor

class AdvRobot:

	def __init__(self, left, right, pwr_coeffs):
		self.left = Motor(left[0],left[1])
		self.right = Motor(right[0],right[1])
		self.pwr_coeffs = pwr_coeffs

	def halt(self):
		self.left.stop()
		self.right.stop()

	def forward(self, power=1):
		self.left.forward(self.pwr_coeffs[0] * power)
		self.right.forward(self.pwr_coeffs[1] * power)

	def backward(self, power=1):
		self.left.backward(self.pwr_coeffs[0] * power)
		self.right.backward(self.pwr_coeffs[1] * power)

	def leftTank(self, power=1):
		self.left.backward(self.pwr_coeffs[0] * power)
		self.right.forward(self.pwr_coeffs[1] * power)

	def rightTank(self, power=1):
		self.left.forward(self.pwr_coeffs[0] * power)
		self.right.backward(self.pwr_coeffs[1] * power)

	def leftPivot(self, power=1):
		self.right.forward(self.pwr_coeffs[0] * power)
		self.left.stop()

	def rightPivot(self, power=1):
		self.left.forward(self.pwr_coeffs[0] * power)
		self.right.stop()
		
