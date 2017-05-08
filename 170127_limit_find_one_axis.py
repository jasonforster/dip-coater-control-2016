import wx
import ArcusDeviceModified as ADM

#### this whole thing is screwed up. need to go eat lunch and try again. 27Jan201712:45
### here is where we create the functions that the GUI buttons will call
def connect_to_device():
	device = ADM.ArcusDevice()
	return device

def close_device_connection(device):
	device.Close()

def create_motor(device):
	motor_id = ADM.ArcusStepperChannel(device,
									 axis='Y',
									 min = 0,
									 max = 100000,
									 acceleration = 1000,
									 lca = 8000,
									 hspd = 4000,
									 lspd = 400)
	return motor_id

def enable_motor(motor_id):
	_ = motor_id.TurnMotorOn()

def disable_motor(motor_id):
	_ = motor_id.TurnMotorOff()

def go_to_minus_limit(motor_id):
	_ = motor_id.GoToLimit(polarity='-')

def go_to_plus_limit(motor_id):
	_ = motor_id.GoToLimit(polarity='+')



#### here is where we setup the gui
class LimitSeeker(wx.Frame):

    def __init__(self, parent, title):

        super(LimitSeeker, self).__init__(parent, title=title, size=(350, 350))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):

    	device = connect_to_device()
        motor = create_motor(device)

        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(5, 5)


        #### set up the buttons to control motor motion

        minus_limit_button = wx.Button(panel, 
                              		   label='Go To Minus Limit')
        plus_limit_button = wx.Button(panel,
        							  label='Go To Plus Limit')

        y_axis_enable_box = wx.CheckBox(panel,
        								label='Enable Motor?')


        sizer.Add(minus_limit_button,
                  pos=(1,1),
                  border=5)
        sizer.Add(plus_limit_button,
        		  pos=(1,2),
        		  border=5)
        sizer.Add(y_axis_enable_box,
        		  pos=(3,1),
        		  border=5)
        # sizer.SetEmptyCellSize((10, 10))
        panel.SetSizerAndFit(sizer)

        ### bind some functions to the widgets?
        self.Bind(wx.EVT_CHECKBOX, self.EvtCheckBox, y_axis_enable_box)
        self.Bind(wx.EVT_CLOSE, self.OnClose(device))


    def OnClose(self, device):
    	close_device_connection(device)

    def EvtCheckBox(self, event):
		cb = event.GetEventObject()
		if cb:
			enable_motor(self.motor)
		else:
			disable_motor(self.motor)


if __name__ == '__main__':
    app = wx.App()
    LimitSeeker(None, title='single Axis Limit Seeker')
    app.MainLoop()