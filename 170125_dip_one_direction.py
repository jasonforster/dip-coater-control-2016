#!/usr/bin/python

#170125_dip_one_direction.py

import wx
import ArcusDeviceModified as ADM

### initialize the Y-axis motor
arc = ADM.ArcusDevice()

dy = ADM.ArcusStepperChannel(arc,
							 axis = 'Y',
							 min = 0,
							 max = 0,
							 acceleration = 30,
							 lca = 8000,
							 hspd = 4000,
							 lspd = 80)

dy.TurnMotorOn()

dy.GoToLimit(polarity = '-')
### set up the GUI and assign functions to buttons
class SimpleDipper(wx.Frame):

    def __init__(self, parent, title):

        super(SimpleDipper, self).__init__(parent, 
        								   title=title, 
        								   size=(350, 400))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):

        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(5, 5)


        #### set up the buttons to control motor motion

        button_up = wx.Button(panel, 
                              label='Up')
        button_down = wx.Button(panel, 
                                label='Down')

        sizer.Add(button_up,
                  pos=(1,1),
                  border=5,
                  flag=wx.ALL|wx.ALIGN_CENTER_HORIZONTAL)

        sizer.Add(button_down,
                  pos=(3,1),
                  border=5,
                  flag=wx.ALL|wx.ALIGN_CENTER_HORIZONTAL)


        #### set up the labels and input fields for dipper speed

        vertical_speed_label = wx.StaticText(panel,
                                             label='Vertical\nSpeed (mm/s)')

        sizer.Add(vertical_speed_label,
                  pos=(6,0),
                  border=5)


        vertical_speed_input = wx.SpinCtrl(panel,
                                           value='1.0')

        sizer.Add(vertical_speed_input,
                  pos=(6,1),
                  border=5,
                  flag=wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM)

		# sizer.SetEmptyCellSize((10, 10))
        panel.SetSizerAndFit(sizer)


if __name__ == '__main__':
    app = wx.App()
    SimpleDipper(None, title='Simple Dipper Control - 170125')
    app.MainLoop()