#!/usr/bin/python

# dipGUI_box_sizer_DATESTAMP.py

import os, sys
import wx

def AddSpacer( boxsizer, reqArg, optArg=None ) :
    """ A smart spacer for use with any BoxSizer """
    
    if (type( reqArg ) == type( 123 )) and (optArg == None) :
        
        orientation = boxsizer.GetOrientation()
        if   (orientation == wx.HORIZONTAL) :
            boxsizer.Add( (reqArg, 0) )
            
        elif (orientation == wx.VERTICAL) :
            boxsizer.Add( (0, reqArg) )
        #end if
            
    elif (type( reqArg ) == type( (123, 123) ))  and (optArg == None) and  \
         (type( reqArg[0] ) == type( 123 ))      and (type( reqArg[1] ) == type( 123 )) :
    
        boxsizer.Add( reqArg )
        
    elif (type( reqArg ) == type( 123 )) and (type( optArg ) == type( 123 )) :
    
        boxsizer.Add( (reqArg, optArg) )
        
    else :
        print
        print '####  AddSpacer():    Argument Types are Not Recognized.'
        sys.exit(1)

###############################################################################

class DipFrame(wx.Frame):

    def __init__(self):

        wx.Frame.__init__(self, 
                          parent=None, 
                          title='Dip Coater Control with Box Sizer')
        self.Center()
        self.ClientSize = (980, 700)
        self.BackgroundColour = 'white'

        frm_pnl = wx.Panel(self)
        frm_pnl.BackgroundColour = (255, 255, 230)

        #### create the top and bottom panels

        top_panel = wx.Panel(frm_pnl)
        top_panel.BackgroundColour = "blue"

        bottom_panel = wx.Panel(frm_pnl)
        bottom_panel.BackgroundColour = "green"

        #### create the main frame sizer and add the top and bottom panels

        main_sizer = wx.BoxSizer(wx.VERTICAL)
        main_sizer.Add(top_panel,
                       flag=wx.EXPAND,
                       proportion=1)
        main_sizer.Add(bottom_panel,
                       flag=wx.EXPAND,
                       proportion=1)
        

        frm_pnl.SetSizer(main_sizer)
        frm_pnl.Layout()


dipApp = wx.App()
DipFrame().Show()
dipApp.MainLoop()