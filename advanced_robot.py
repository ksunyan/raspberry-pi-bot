from gpiozero import Motor

class AdvRobot:

	def __init__(self, left, right, pwr_coeffs):
		self.left = Motor(left[0],left[1])
		self.right = Motor(right[0],right[1])
		self.pwr_coeffs = pwr_coeffs

	def halt(self):
		self.left.stop()
		self.right.stop()

	def forward(self, power):
		self.left.forward(self.pwr_coeffs[0] * power)
		self.right.forward(self.pwr_coeffs[1] * power)
