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
## Class PanelThemSanPham
###########################################################################

class PanelThemSanPham ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 547,253 ), style = wx.TAB_TRAVERSAL )
        
        gbSizer3 = wx.GridBagSizer( 0, 0 )
        gbSizer3.SetFlexibleDirection( wx.BOTH )
        gbSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText29 = wx.StaticText( self, wx.ID_ANY, u"Thông Tin Sản Phẩm", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_staticText29.Wrap( -1 )
        self.m_staticText29.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), 70, 94, 90, False, wx.EmptyString ) )
        
        gbSizer3.Add( self.m_staticText29, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText30 = wx.StaticText( self, wx.ID_ANY, u"Mã số", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText30.Wrap( -1 )
        gbSizer3.Add( self.m_staticText30, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.edtMaSo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        gbSizer3.Add( self.edtMaSo, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_staticText31 = wx.StaticText( self, wx.ID_ANY, u"Tên", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText31.Wrap( -1 )
        gbSizer3.Add( self.m_staticText31, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.edtTen = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3.Add( self.edtTen, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText32 = wx.StaticText( self, wx.ID_ANY, u"Ký hiệu", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText32.Wrap( -1 )
        gbSizer3.Add( self.m_staticText32, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.edtKyHieu = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3.Add( self.edtKyHieu, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText33 = wx.StaticText( self, wx.ID_ANY, u"Đơn giá nhập", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText33.Wrap( -1 )
        gbSizer3.Add( self.m_staticText33, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.edtDonGiaNhap = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3.Add( self.edtDonGiaNhap, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Đơn giá bán", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText34.Wrap( -1 )
        gbSizer3.Add( self.m_staticText34, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.edtDonGiaBan = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3.Add( self.edtDonGiaBan, wx.GBPosition( 4, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText35 = wx.StaticText( self, wx.ID_ANY, u"Số lượng tồn", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText35.Wrap( -1 )
        gbSizer3.Add( self.m_staticText35, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.edtSoLuongTon = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3.Add( self.edtSoLuongTon, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText36 = wx.StaticText( self, wx.ID_ANY, u"Nhóm sản phẩm", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText36.Wrap( -1 )
        gbSizer3.Add( self.m_staticText36, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        choiceNhomSanPhamChoices = []
        self.choiceNhomSanPham = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, choiceNhomSanPhamChoices, 0 )
        self.choiceNhomSanPham.SetSelection( 0 )
        gbSizer3.Add( self.choiceNhomSanPham, wx.GBPosition( 5, 3 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.btnThem = wx.Button( self, wx.ID_ANY, u"Thêm", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer3.Add( self.btnThem, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 4 ), wx.ALL|wx.EXPAND, 5 )
        
        
        self.SetSizer( gbSizer3 )
        self.Layout()
        
        # Connect Events
        self.btnThem.Bind( wx.EVT_BUTTON, self.btnThem_click )
    
    def __del__( self ):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def btnThem_click( self, event ):
        Ma_so = self.edtMaSo.GetValue()
        Ten = self.edtTen.GetValue()
        Ky_hieu = self.edtKyHieu.GetValue()
        Don_gia_nhap = self.edtDonGiaNhap.GetValue()
        So_luong_ton = self.edtSoLuongTon.GetValue()
        Don_gia_ban = self.edtDonGiaBan.GetValue()
        Nhom_san_pham = self.choiceNhomSanPham.GetString(self.choiceNhomSanPham.GetSelection())

        sp = SanPham('Du_lieu/quan_ly_ban_hang.db')
        try:
            n = sp.ThemSanPham(Ten, Ma_so, Ky_hieu, Don_gia_ban, Don_gia_nhap, So_luong_ton, Nhom_san_pham)
            if n > 0:
                dlg = wx.MessageDialog(None, "Thêm sản phẩm thành công", "Thông báo", wx.OK)
            else:
                dlg = wx.MessageDialog(None, "Thêm sản phẩm không thành công", "Thông báo", wx.OK)
        except:
            dlg = wx.MessageDialog(None, "Thêm sản phẩm không thành công", "Thông báo", wx.OK)
        finally:
            sp.deConnect()
            dlg.ShowModal()
            self.Close()