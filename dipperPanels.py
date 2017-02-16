#~/usr/bin/python

# dipperPanels.py

import wx
import os, sys

def AddSpacer( boxsizer, reqArg, optArg=None ) :
    """ 
        AddSpacer

        An intelligent function to add a variety of spacers.  
        Interger values of zero or greater are valid.

        Syntax:
            AddSpacer( sizerName, reqArg, rectYarg )

            A) reqArg is a single integer. Inserts a one-demensional spacer
                along the sizer's major axis. This is a safe alternative 
                to the sizer.AddSpacer( n ) method which inserts a square 
                shaped spacer which can unintentionally interfere with 
                adjacent controls stacked along one or both of the 
                sizer's minor axis.

            B) reqArg is a 2-tuple of integers. Inserts a rectanguler spacer.
                E.g.:   (20, 30)
                Inserts a rectanguler spacer.
   
            C) reqArg and optArg are integer arguments.
                 E.g.:   20, 30
                Inserts a rectanguler spacer.
   

        Ray Pasco
        2010-09-25-Sat__PM-03-14-19__September
    """
    
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


#------------------------------------------------------------------------------

class MiddleButtonPanel(wx.Panel):
    """
    A horizontal panel with a single button in the middle
    """

    def __init__(self, parent, buttonLabel):

        wx.Panel.__init__(self, 
                          parent=parent, 
                          id=-1)

        #----

        middleButton = wx.Button(self, 
                                 -1, 
                                 buttonLabel)

        #----

        panelHorizontalSizer = wx.BoxSizer(wx.HORIZONTAL)

        AddSpacer(panelHorizontalSizer, 10)

        alignFlag = wx.ALIGN_CENTER
        padFlag = wx.LEFT|wx.RIGHT

        panelHorizontalSizer.Add(middleButton, 
                                 flag=alignFlag|padFlag, 
                                 border=10)

        AddSpacer(panelHorizontalSizer, 10)

        #----

        self.SetSizer(panelHorizontalSizer)
        self.LayOut()

#----

class MiddleSpaceButtonPanel(wx.Panel):
    """
    A horizontal panel with two buttons separated by an empty space
    """

    def __init__(self, parent, buttonLabels):

        wx.Panel.__init__(self,
                          parent=parent,
                          id=-1)

        #----
        
        leftButton = wx.Button(self,
                              -1,
                              buttonLabels[0])

        rightButton = wx.Button(self,
                                -1,
                                buttonLabels[1])

        #----

        panelHorizontalSizer = wx.BoxSizer(wx.HORIZONTAL)

        padFlag = wx.LEFT|wx.RIGHT

        panelHorizontalSizer.Add(leftButton,
                                 flag=wx.ALIGN_LEFT|padFlag,
                                 border=10)
        
        AddSpacer(panelHorizontalSizer, 10)

        panelHorizontalSizer.Add(rightButton,
                                 flag=wx.ALIGN_RIGHT|padFlag,
                                 border=10)

        #----

        self.SetSizer(panelHorizontalSizer)
        self.Layout()


class ButtonPanel(wx.Panel):
    """
    A vertical panel with three rows of buttons
    """

    def __init__(self, parent):

        wx.Panel.__init__(self, 
                          parent=parent,
                          id=-1)

        #----
        topRowPanel = MiddleButtonPanel()

        #----

        panelVerticalSizer = wx.BoxSizer(wx.VERTICAL)

        panelVerticalSizer.Add()
