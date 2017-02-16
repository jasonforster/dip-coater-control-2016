import wx
import wx.lib.agw.genericmessagedialog as GMD
import sys
try:
   import sqlalchemy
except:
   pass

def main():
   app = wx.PySimpleApp()
   try:
      version = "{}.{}".format(*list(sys.version_info[:2]))
      message = "Congratulations \nthis program uses\npython {}\nwxpython {}\nsqlalchemy {}".format(version , wx.__version__, sqlalchemy.__version__)
   except:
      message = "Sorry but you forgot to set the PYTHONPATH variable using source dothis"
   dlg = GMD.GenericMessageDialog(None, message , "A message for you", wx.OK |  ( wx.ICON_INFORMATION + GMD.GMD_USE_GRADIENTBUTTONS )  )
   dlg.ShowModal()
   dlg.Destroy()
   app.MainLoop()

if __name__ == "__main__":
   main()