import wx
import os
import sys
from Giao_dien.FrmQuanLyBanHang import *

if __name__ == "__main__":
    os.chdir(os.path.abspath(os.path.dirname(sys.executable)))
    app = wx.App()
    frame = FrmQuanLyBanHang()
    frame.Center()
    frame.Show(True)
    app.MainLoop()