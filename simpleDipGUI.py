#!/usr/bin/python

#simpleDipGUI.py

import wx

class SimpleDipper(wx.Frame):

    def __init__(self, parent, title):

        super(SimpleDipper, self).__init__(parent, title=title, size=(350, 400))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):

        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(5, 5)


        #### set up the buttons to control motor motion

        button_up = wx.Button(panel, 
                              label='Up')
        button_left = wx.Button(panel, 
                                label='Left')
        button_right = wx.Button(panel, 
                                 label='Right')
        button_down = wx.Button(panel, 
                                label='Down')

        sizer.Add(button_up,
                  pos=(1,1),
                  border=5,
                  flag=wx.ALL|wx.ALIGN_CENTER_HORIZONTAL)
        sizer.Add(button_left,
                  pos=(2,0),
                  border=5,
                  flag=wx.ALL|wx.ALIGN_CENTER_HORIZONTAL)
        sizer.Add(button_right,
                  pos=(2,2),
                  border=5,
                  flag=wx.ALL|wx.ALIGN_CENTER_HORIZONTAL)
        sizer.Add(button_down,
                  pos=(3,1),
                  border=5,
                  flag=wx.ALL|wx.ALIGN_CENTER_HORIZONTAL)


        #### set up the labels and input fields for dipper speed

        horizontal_speed_label = wx.StaticText(panel,
                                               label='Horizontal\nSpeed (mm/s)')
        vertical_speed_label = wx.StaticText(panel,
                                             label='Vertical\nSpeed (mm/s)')
        sizer.Add(horizontal_speed_label,
                  pos=(5,0),
                  border=5)
        sizer.Add(vertical_speed_label,
                  pos=(6,0),
                  border=5)

        horizontal_speed_input = wx.SpinCtrl(panel,
                                             value='1.0')
        vertical_speed_input = wx.SpinCtrl(panel,
                                           value='1.0')
        sizer.Add(horizontal_speed_input,
                  pos=(5,1),
                  border=5,
                  flag=wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM)
        sizer.Add(vertical_speed_input,
                  pos=(6,1),
                  border=5,
                  flag=wx.LEFT|wx.RIGHT|wx.TOP|wx.BOTTOM)




        # sizer.SetEmptyCellSize((10, 10))
        panel.SetSizerAndFit(sizer)


if __name__ == '__main__':
    app = wx.App()
    SimpleDipper(None, title='Simple Dipper Controls')
    app.MainLoop()