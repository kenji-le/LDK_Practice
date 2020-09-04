# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug 23 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from Xu_ly.Xu_ly_NhanVien import *

###########################################################################
## Class PanelDanhSachNhanVien
###########################################################################

class PanelDanhSachNhanVien ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.TAB_TRAVERSAL )
        
        gbSizer4 = wx.GridBagSizer( 0, 0 )
        gbSizer4.SetFlexibleDirection( wx.BOTH )
        gbSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_listCtrl_danh_sach_nhan_vien = wx.ListCtrl( self, -1, wx.DefaultPosition, size=(600,400), style=wx.LC_REPORT )
        gbSizer4.Add( self.m_listCtrl_danh_sach_nhan_vien, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        self.m_listCtrl_danh_sach_nhan_vien.InsertColumn(0, 'Mã số', width = 100)
        self.m_listCtrl_danh_sach_nhan_vien.InsertColumn(1, 'Họ tên', wx.LIST_FORMAT_LEFT, 200)
        self.m_listCtrl_danh_sach_nhan_vien.InsertColumn(2, 'Tên đăng nhập', wx.LIST_FORMAT_LEFT, 100)

        nhanVien = NhanVien('Du_lieu/quan_ly_ban_hang.db')
        lstNhanVien = nhanVien.DanhSachNhanVien()

        index = 0
        for nv in lstNhanVien:
            self.m_listCtrl_danh_sach_nhan_vien.InsertItem(index, nv['Ma_so'])
            self.m_listCtrl_danh_sach_nhan_vien.SetItem(index, 1, nv['Ho_ten'])
            self.m_listCtrl_danh_sach_nhan_vien.SetItem(index, 2, nv['Ten_dang_nhap'])
        
        self.SetSizer( gbSizer4 )
        self.Layout()
    
    def __del__( self ):
        pass