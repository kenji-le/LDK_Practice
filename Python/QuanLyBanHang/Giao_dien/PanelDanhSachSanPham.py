# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug 23 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from Xu_ly.Xu_ly_SanPham import *

###########################################################################
## Class PanelDanhSachSanPham
###########################################################################

class PanelDanhSachSanPham ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 600,300 ), style = wx.TAB_TRAVERSAL )
        
        gbSizer6 = wx.GridBagSizer( 0, 0 )
        gbSizer6.SetFlexibleDirection( wx.BOTH )
        gbSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_listCtrl_danh_sach_san_pham = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( 600,400 ), wx.LC_REPORT )
        gbSizer6.Add( self.m_listCtrl_danh_sach_san_pham, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_listCtrl_danh_sach_san_pham.InsertColumn(0, 'Mã số', width = -1)
        self.m_listCtrl_danh_sach_san_pham.InsertColumn(1, 'Tên', wx.LIST_FORMAT_LEFT, -1)
        self.m_listCtrl_danh_sach_san_pham.InsertColumn(2, 'Ký hiệu', wx.LIST_FORMAT_LEFT, -1)
        self.m_listCtrl_danh_sach_san_pham.InsertColumn(3, 'Đơn giá nhập', wx.LIST_FORMAT_LEFT, -1)
        self.m_listCtrl_danh_sach_san_pham.InsertColumn(4, 'Đơn giá bán', wx.LIST_FORMAT_LEFT, -1)
        self.m_listCtrl_danh_sach_san_pham.InsertColumn(5, 'Số lượng tồn', wx.LIST_FORMAT_LEFT, -1)
        self.m_listCtrl_danh_sach_san_pham.InsertColumn(6, 'Nhóm sản phẩm', wx.LIST_FORMAT_LEFT, -1)

        sanPham = SanPham('Du_lieu/quan_ly_ban_hang.db')
        lstSanPham = sanPham.DanhSachSanPham()

        index = 0
        for nv in lstSanPham:
            self.m_listCtrl_danh_sach_san_pham.InsertItem(index, nv['Ma_so'])
            self.m_listCtrl_danh_sach_san_pham.SetItem(index, 1, nv['Ten'])
            self.m_listCtrl_danh_sach_san_pham.SetItem(index, 2, nv['Ky_hieu'])
            self.m_listCtrl_danh_sach_san_pham.SetItem(index, 3, str(nv['Don_gia_nhap']))
            self.m_listCtrl_danh_sach_san_pham.SetItem(index, 4, str(nv['Don_gia_ban']))
            self.m_listCtrl_danh_sach_san_pham.SetItem(index, 5, str(nv['So_luong_ton']))
            self.m_listCtrl_danh_sach_san_pham.SetItem(index, 6, nv['Nhom_san_pham'])

        self.SetSizer( gbSizer6 )
        self.Layout()
    
    def __del__( self ):
        pass
    

