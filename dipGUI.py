#!usr/bin/python

#dipGUI.py

import wx

class Dipper(wx.Frame):

    def __init__(self, parent, title):
        super(Dipper, self).__init__(parent, title=title, size=(980, 700))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(4, 4)


        #### set up the manual motor control box
        text1 = wx.StaticText(panel, 
                              label='Manual Motor\nControls')
        sizer.Add(text1, 
                  pos=(0, 0), 
                  flag=wx.TOP|wx.LEFT|wx.BOTTOM, 
                  border=5)

        mmc = wx.TextCtrl(panel)
        sizer.Add(mmc, 
                  pos=(1, 0), 
                  span=(8, 4), 
                  flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.BOTTOM, 
                  border=10)

        
        #### set up the position indicators
        horizontal_position_text = wx.StaticText(panel, 
                                                 label='Current\nHorizontal\nPosition (mm)')
        sizer.Add(horizontal_position_text, 
                  pos=(1, 4))

        horizontal_position_indicator = wx.TextCtrl(panel)
        sizer.Add(horizontal_position_indicator, 
                  pos=(2,4), 
                  span=(1,2))

        vertical_position_text = wx.StaticText(panel, 
                                               label='Current\nVertical\nPosition (mm)')
        sizer.Add(vertical_position_text, 
                  pos=(3, 4))

        vertical_position_indicator = wx.TextCtrl(panel)
        sizer.Add(vertical_position_indicator, 
                  pos=(4,4), 
                  span=(1,2))


        #### set up the dipper position display box
        text2 = wx.StaticText(panel, 
                              label='Dipper\nPosition')
        sizer.Add(text2, 
                  pos=(0, 7),
                  flag=wx.TOP|wx.LEFT|wx.BOTTOM, 
                  border=5)

        dpd = wx.TextCtrl(panel)
        sizer.Add(dpd, 
                  pos=(1, 7), 
                  span=(8,4),
                  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.BOTTOM, 
                  border=5)


        #### set up the reset button
        reset_button = wx.Button(panel, 
                                 label='reset')
        sizer.Add(reset_button, 
                  pos=(10, 0), 
                  flag=wx.LEFT, 
                  border=10)


        #### set up the emergency stop button
        stop_button = wx.Button(panel, 
                                label='EMERGENCY STOP')
        sizer.Add(stop_button, 
                  pos=(12, 0), 
                  flag=wx.LEFT, 
                  border=10)
        

        #### set up four check boxes to select which dip positions are active
        check1 = wx.CheckBox(panel, 
                             label='Pos. 1')
        sizer.Add(check1, 
                  pos=(9, 7), 
                  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT|wx.BOTTOM, 
                  border=5)

        check2 = wx.CheckBox(panel, 
                             label='Pos. 2')
        sizer.Add(check2, 
                  pos=(9, 8), 
                  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT|wx.BOTTOM, 
                  border=5)

        check3 = wx.CheckBox(panel, 
                             label='Pos. 3')
        sizer.Add(check3, 
                  pos=(9, 9), 
                  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT|wx.BOTTOM, 
                  border=5)

        check4 = wx.CheckBox(panel, 
                             label='Pos. 4')
        sizer.Add(check4, 
                  pos=(9, 10), 
                  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT|wx.BOTTOM, 
                  border=5)


        #### set up the four buttons to record the dip depth for each position
        dipStop1 = wx.Button(panel, 
                             label='Record\nDepth')
        sizer.Add(dipStop1, 
                  pos=(10, 7), 
                  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT|wx.BOTTOM, 
                  border =5)

        dipStop2 = wx.Button(panel, 
                             label='Record\nDepth')
        sizer.Add(dipStop2, 
                  pos=(10, 8), 
                  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT|wx.BOTTOM, 
                  border =5)

        dipStop3 = wx.Button(panel, 
                             label='Record\nDepth')
        sizer.Add(dipStop3, 
                  pos=(10, 9), 
                  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT|wx.BOTTOM, 
                  border =5)

        dipStop4 = wx.Button(panel, 
                             label='Record\nDepth')
        sizer.Add(dipStop4, 
                  pos=(10, 10), 
                  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT|wx.BOTTOM, 
                  border=5)


        #### set up the labels for speed and time delay entry fields
        insert_speed_label = wx.StaticText(panel, 
                                           label='insertion\nspeed (mm/s)')
        sizer.Add(insert_speed_label, 
                  pos=(11, 4), 
                  flag=wx.EXPAND|wx.BOTTOM|wx.TOP, 
                  border=5)

        withdrawal_speed_label = wx.StaticText(panel, 
                                               label='withdrawal\nspeed (mm/s)')
        sizer.Add(withdrawal_speed_label, 
                  pos=(12, 4), 
                  flag=wx.EXPAND|wx.BOTTOM|wx.TOP, 
                  border=5)

        time_delay_label = wx.StaticText(panel, 
                                         label='time delay (s)')
        sizer.Add(time_delay_label, 
                  pos=(13, 4), 
                  flag=wx.EXPAND|wx.BOTTOM|wx.TOP, 
                  border=5)


        #### set up entry fields for dip speed, withdrawal speed and time delay
        insert_speed_1 = wx.SpinCtrl(panel, value='0.00')
        sizer.Add(insert_speed_1, 
                  pos=(11, 7), 
                  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT|wx.BOTTOM, 
                  border=5)

        insert_speed_2 = wx.SpinCtrl(panel, value='0.00')
        sizer.Add(insert_speed_2, 
                  pos=(11, 8), 
                  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT|wx.BOTTOM, 
                  border=5)

        insert_speed_3 = wx.SpinCtrl(panel, value='0.00')
        sizer.Add(insert_speed_3, 
                  pos=(11, 9), 
                  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT|wx.BOTTOM, 
                  border=5)

        insert_speed_4 = wx.SpinCtrl(panel, value='0.00')
        sizer.Add(insert_speed_4,
                  pos=(11, 10), 
                  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT|wx.BOTTOM, 
                  border=5)

        withdrawal_speed_1 = wx.SpinCtrl(panel, value='0.00')
        sizer.Add(withdrawal_speed_1, 
                  pos=(12, 7), 
                  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT|wx.BOTTOM, 
                  border=5)

        withdrawal_speed_2 = wx.SpinCtrl(panel, value='0.00')
        sizer.Add(withdrawal_speed_2, 
                  pos=(12, 8), 
                  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT|wx.BOTTOM, 
                  border=5)

        withdrawal_speed_3 = wx.SpinCtrl(panel, value='0.00')
        sizer.Add(withdrawal_speed_3, 
                  pos=(12, 9), 
                  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT|wx.BOTTOM, 
                  border=5)

        withdrawal_speed_4 = wx.SpinCtrl(panel, value='0.00')
        sizer.Add(withdrawal_speed_4, 
                  pos=(12, 10), 
                  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT|wx.BOTTOM, 
                  border=5)

        time_delay_1 = wx.SpinCtrl(panel, value='0.00')
        sizer.Add(time_delay_1, 
                  pos=(13, 7), 
                  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT|wx.BOTTOM, 
                  border=5)

        time_delay_2 = wx.SpinCtrl(panel, value='0.00')
        sizer.Add(time_delay_2, 
                  pos=(13, 8), 
                  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT|wx.BOTTOM, 
                  border=5)

        time_delay_3 = wx.SpinCtrl(panel, value='0.00')
        sizer.Add(time_delay_3, 
                  pos=(13, 9), 
                  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT|wx.BOTTOM, 
                  border=5)

        time_delay_4 = wx.SpinCtrl(panel, value='0.00')
        sizer.Add(time_delay_4, 
                  pos=(13, 10), 
                  flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT|wx.BOTTOM, 
                  border=5)


        #### set up field to set number of repitions
        rep_number_label = wx.StaticText(panel, 
                                         label='number of cycles')
        sizer.Add(rep_number_label, 
                  pos=(14, 7), 
                  flag=wx.EXPAND|wx.BOTTOM|wx.TOP, 
                  border=5)

        rep_number = wx.SpinCtrl(panel, value='1')
        sizer.Add(rep_number, 
                  pos=(14,8), 
                  flag=wx.EXPAND|wx.BOTTOM|wx.TOP, 
                  border=5)


        #### add "go" button
        go_button = wx.Button(panel, 
                              label='GO')
        sizer.Add(go_button, 
                  pos=(15, 10), 
                  span=(1,2),
                  flag=wx.EXPAND|wx.BOTTOM|wx.TOP, 
                  border=5)



        sizer.SetEmptyCellSize((30, 40))
        panel.SetSizerAndFit(sizer)




if __name__ == '__main__':
    app = wx.App()
    Dipper(None, title='Dipper')
    app.MainLoop()