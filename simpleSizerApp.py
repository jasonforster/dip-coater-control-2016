#!/usr/bin/python

""" SIMPLE_SINGLE_SIZER_2_A.PY """

import wx

#------------------------------------------------------------------------------

class MainFrame( wx.Frame ) :
    """ A very basic single BoxSizer demo """
        
    def __init__( self, parent ) :
        
        #----  Configure the Frame.
        
        wx.Frame.__init__ ( self, parent, -1, title='SIMPLE_SINGLE_SIZER_2_A.PY', 
                            size=(400, 300), pos=(100, 100), 
                            style=wx.DEFAULT_FRAME_STYLE )
        
        # A panel is needed for tab-traversal and platform background color consistancy.
        frm_pnl = wx.Panel( self )
        frm_pnl.BackgroundColour = (255, 250, 240)
        
        #-----  Create the controls.
        
        # A "pos=" positioning parameter is allowed to be given, 
        #   but would be ignored and overridden by the sizer.
        caption_stTxt = wx.StaticText( frm_pnl, label='Caption Text' )
        
        # The given vertical dimension will be automatically overridden by the sizer.
        frm_pnl.listing_txtCtrl = wx.TextCtrl( frm_pnl, -1, style=wx.TE_MULTILINE, 
                                               size=(200, 150) )
        
        #-----  Create the sizer and add the controls to it.
        
        allCtrls_vertSizer = wx.BoxSizer( wx.VERTICAL )
        
        allCtrls_vertSizer.AddStretchSpacer( prop=1 )
        
        allCtrls_vertSizer.Add( caption_stTxt,           flag=wx.ALIGN_CENTER )
        allCtrls_vertSizer.Add( frm_pnl.listing_txtCtrl, flag=wx.ALIGN_CENTER )
        
        allCtrls_vertSizer.AddStretchSpacer( prop=1 )
        
        # Apply to the sizer's container :
        frm_pnl.SetSizer( allCtrls_vertSizer )
        frm_pnl.Layout()                 # frm_pnl.Fit()  # always use one or the other
        
    #end __init__

#end MainFrame class

#==============================================================================

if __name__ == '__main__' :

    app = wx.App( redirect=False )
    appFrame = MainFrame( None ).Show()
    app.MainLoop()

#end if