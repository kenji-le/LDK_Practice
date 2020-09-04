# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug 23 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import pdb
import wx
import wx.xrc
from Xu_ly.Xu_ly_NhomSanPham import *

###########################################################################
## Class PanelNhomSanPham
###########################################################################

class PanelNhomSanPham ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 767,423 ), style = wx.TAB_TRAVERSAL )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Nhóm sản phẩm" ), wx.VERTICAL )
        
        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
        
        self.mMaSo = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Mã số", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.mMaSo.Wrap( -1 )
        bSizer3.Add( self.mMaSo, 0, wx.ALL, 5 )
        
        self.mMaSo = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        bSizer3.Add( self.mMaSo, 0, wx.ALL, 5 )
        
        self.m_staticText7 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Tên", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )
        bSizer3.Add( self.m_staticText7, 0, wx.ALL, 5 )
        
        self.mTen = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), 0 )
        bSizer3.Add( self.mTen, 0, wx.ALL, 5 )
        
        sbSizer1.Add( bSizer3, 1, wx.EXPAND, 5 )
        
        self.btnThem = wx.Button( sbSizer1.GetStaticBox(), wx.ID_ANY, u"Thêm", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer1.Add( self.btnThem, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        bSizer2.Add( sbSizer1, 0, wx.EXPAND, 5 )
        
        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Danh sách nhóm" ), wx.VERTICAL )
        
        self.mDanhSachNhom = wx.ListBox( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.Size( 600,300 ), [], wx.LB_MULTIPLE|wx.LB_SORT )
        self.CapNhatDanhSachNhomSanPham()
        sbSizer2.Add( self.mDanhSachNhom, 0, wx.ALL|wx.EXPAND, 5 )
        
        bSizer2.Add( sbSizer2, 1, wx.EXPAND, 5 )
        
        self.SetSizer( bSizer2 )
        self.Layout()
        
        # Connect Events
        self.btnThem.Bind( wx.EVT_BUTTON, self.ThemNhom )
    
    def __del__( self ):
        pass
    
    def CapNhatDanhSachNhomSanPham(self):
        nhomSanPham = NhomSanPham('Du_lieu/quan_ly_ban_hang.db')
        lstNhomSanPham  = nhomSanPham.DanhSachNhomSanPham()
        lstTenNhom  = []
        for item in lstNhomSanPham:
            lstTenNhom.append(item['Ten_nhom'])
        nhomSanPham.deConnect()

        self.mDanhSachNhom.SetItems(lstTenNhom)

    # Virtual event handlers, overide them in your derived class
    def ThemNhom( self, event ):
        Ma_nhom = self.mMaSo.GetValue()
        Ten_nhom = self.mTen.GetValue()
        nhomSanPham = NhomSanPham('Du_lieu/quan_ly_ban_hang.db')
        try:
            n = nhomSanPham.ThemNhomSanPham(Ma_nhom, Ten_nhom)
            if n > 0:
                self.CapNhatDanhSachNhomSanPham()
                dlg = wx.MessageDialog(None, "Thêm nhóm thành công", "Thông báo", wx.OK)
            else:
                dlg = wx.MessageDialog(None, "Thêm nhóm không thành công", "Thông báo", wx.OK)
        except:
            dlg = wx.MessageDialog(None, "Thêm nhóm không thành công", "Thông báo", wx.OK)
        finally:
            nhomSanPham.deConnect()
            dlg.ShowModal()