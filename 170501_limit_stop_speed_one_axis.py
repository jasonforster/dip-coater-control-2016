import wx
import ArcusDeviceModified as ADM

class TheFrame(wx.Frame):
	def __init__(self, parent, id=wx.ID_ANY, title='',
	             pos=wx.DefaultPosition, size=(300,300),
	             style=wx.DEFAULT_FRAME_STYLE, name='TheFrame'):
		super(TheFrame, self).__init__(parent, id, title,
		                               pos, size, style, name)

		# Attributes
		self.CreateStatusBar()

		# Layout the buttons
		sizer = wx.BoxSizer(wx.VERTICAL)

		self.active_motor_checkbox = wx.CheckBox(self, wx.ID_ANY,
		                                    label='Enable Motor?')

		self.speed_label = wx.StaticText(self, wx.ID_ANY,
		                                 label='Motor Speed (mm/s)')
		self.speed_input = wx.TextCtrl(self, wx.ID_ANY)

		self.limit_button = wx.Button(self, wx.ID_ANY,
		                         label='Go To Minus Limit')
		self.stop_button = wx.Button(self, wx.ID_ANY,
		                        label='STOP!')

		sizer.Add(self.active_motor_checkbox, 0, wx.ALL, 5)
		sizer.Add(self.speed_label, 0, wx.ALL, 5)
		sizer.Add(self.speed_input, 0, wx.ALL, 5)
		sizer.Add(self.limit_button, 0, wx.ALL, 5)
		sizer.Add(self.stop_button, 0, wx.ALL, 5)

		self.SetSizer(sizer)

		# Bind events to the buttons
		self.Bind(wx.EVT_CHECKBOX, self.OnCheckActivate, self.active_motor_checkbox)
		self.Bind(wx.EVT_TEXT_ENTER, self.OnSpeedInput, self.speed_input)
		self.Bind(wx.EVT_BUTTON, self.OnLimitButton, self.limit_button)
		self.Bind(wx.EVT_BUTTON, self.OnStopButton, self.stop_button)


	def OnCheckActivate(self, event):
		"""
		Checking this button should initialize one of the motors on the dip coater with 
		some default settings for speed, etc.
		"""
		checked = self.active_motor_checkbox.GetValue()
		if checked:
			self.device, self.motor = self.ActivateMotor(active_axis='Y')
			# self.PushStatusText('Motor Enabled.')
		else:
			self.DeactivateMotor(self.motor, self.device)
			del self.motor
			del self.device

	def OnSpeedInput(self, event):
		"""
		This function deals with the motor speed text control
		1. When the user inputs a value, this function changes the motor 
			settings to update the speed.
		Should implement some kind of check on the type of input.
		Also need to think about how to handle the impending separation
		of axes.
		"""
		new_speed = float(self.speed_input.GetValue())
		#convert new speed to steps/s
		new_speed_steps = new_speed*800

		self.motor.device.Write('HSPDY=' + str(new_speed_steps))
		print('New speed is ' + self.motor.device.Write('HSPDY') + ' steps/s')
		


	def OnLimitButton(self, event):
		"""
		There are a number of things that should occur when this function
		is called.
		1. There should be a check that there is an active stepper channel.
		2. If the check in step one is passed, the method to move the motor to 
			its minus limit should be called.
		"""
		motor_active = self.active_motor_checkbox.GetValue()
		if motor_active:
			self.PushStatusText('Limit sequence activated.')
			self.motor.GoToLimit(polarity='-', wait=False)
		else:
			self.PushStatusText('No active motor. No sequence activated.')

	def OnStopButton(self, event):
		"""

		"""
		motor_active = self.active_motor_checkbox.GetValue()
		if motor_active:
			self.PushStatusText('Stop sequence requested!')
			# do something to interrupt the motor and stop it immediately!
			self.motor.Abort()
		else:
			self.PushStatusText('No active motor to stop.')


	def ActivateMotor(self, active_axis='Y'):
		"""
		This method is called when the enable motor checkbox is checked.
		This is where the code interfaces with the ADM and arcus modules.
		One thing I am presently confused about is how to give the rest
		of this code access to the motor object
		"""

		arc = ADM.ArcusDevice()
		motor = ADM.ArcusStepperChannel(arc, axis=active_axis, min=0, max=200000,
		                                acceleration=250, lca=8000, hspd=2400, lspd=240)
		abort_success = motor.Abort()
		if abort_success:
			print('axis %s is successfully stopped' % motor.axis)
		else:
			print('axis %s did not listen to you' % motor.axis)
		activate_success = motor.TurnMotorOn()
		if activate_success:
			print('axis %s is active' % motor.axis)
			self.PushStatusText('motor activated on %s axis' % motor.axis)
			print('current motor high speed is %s steps/s' % motor.hspd)
			self.speed_input.ChangeValue(str(motor.hspd/800))
		else:
			print('axis %s did not turn on' % motor.axis)

		
		return arc, motor

	def DeactivateMotor(self, motor, device): # call should be like DeactivateMotor(self, motor)g
		deactivate_success = motor.TurnMotorOff()
		close_success = device.Close()
		if deactivate_success & close_success:
			print('motor deactivated and device closed')
			self.PushStatusText('motor deactivated')
			return 1
		else:
			print('deactivation and closing not successful')
			return 0


class TheApp(wx.App):
	def OnInit(self):
		self.frame = TheFrame(None, title='Limit finder, speed setter.')
		self.SetTopWindow(self.frame)
		self.frame.Show()

		return True

if __name__ == '__main__':
	app = TheApp(False)
	app.MainLoop()