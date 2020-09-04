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
## Class PanelCapNhatSanPham
###########################################################################

class PanelCapNhatSanPham ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 519,300 ), style = wx.TAB_TRAVERSAL )
        
        gbSizer7 = wx.GridBagSizer( 0, 0 )
        gbSizer7.SetFlexibleDirection( wx.BOTH )
        gbSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText53 = wx.StaticText( self, wx.ID_ANY, u"Nhập mã số", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText53.Wrap( -1 )
        gbSizer7.Add( self.m_staticText53, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.edtMaSo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
        gbSizer7.Add( self.edtMaSo, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.btnTim = wx.Button( self, wx.ID_ANY, u"Tìm", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer7.Add( self.btnTim, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_staticText54 = wx.StaticText( self, wx.ID_ANY, u"Tên", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText54.Wrap( -1 )
        gbSizer7.Add( self.m_staticText54, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.edtTen = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer7.Add( self.edtTen, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText55 = wx.StaticText( self, wx.ID_ANY, u"Ký hiệu", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText55.Wrap( -1 )
        gbSizer7.Add( self.m_staticText55, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.edtKyHieu = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer7.Add( self.edtKyHieu, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText56 = wx.StaticText( self, wx.ID_ANY, u"Đơn giá nhập", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText56.Wrap( -1 )
        gbSizer7.Add( self.m_staticText56, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.edtDonGiaNhap = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer7.Add( self.edtDonGiaNhap, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText58 = wx.StaticText( self, wx.ID_ANY, u"Đơn giá bán", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText58.Wrap( -1 )
        gbSizer7.Add( self.m_staticText58, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.edtDonGiaBan = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer7.Add( self.edtDonGiaBan, wx.GBPosition( 3, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText57 = wx.StaticText( self, wx.ID_ANY, u"Số lượng tồn", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText57.Wrap( -1 )
        gbSizer7.Add( self.m_staticText57, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.edtSoLuongTon = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer7.Add( self.edtSoLuongTon, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText59 = wx.StaticText( self, wx.ID_ANY, u"Nhóm sản phẩm", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText59.Wrap( -1 )
        gbSizer7.Add( self.m_staticText59, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        m_choice_nhom_san_phamChoices = []
        self.m_choice_nhom_san_pham = wx.Choice( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choice_nhom_san_phamChoices, 0 )
        self.m_choice_nhom_san_pham.SetSelection( 0 )
        gbSizer7.Add( self.m_choice_nhom_san_pham, wx.GBPosition( 4, 3 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.btnCapNhat = wx.Button( self, wx.ID_ANY, u"Cập Nhật", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer7.Add( self.btnCapNhat, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
        
        self.btnXoa = wx.Button( self, wx.ID_ANY, u"Xóa", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer7.Add( self.btnXoa, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
        
        
        self.SetSizer( gbSizer7 )
        self.Layout()
        
        # Connect Events
        self.btnTim.Bind( wx.EVT_BUTTON, self.tim_click )
        self.btnCapNhat.Bind( wx.EVT_BUTTON, self.cap_nhat_click )
        self.btnXoa.Bind( wx.EVT_BUTTON, self.xoa_click )
    
    def __del__( self ):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def tim_click( self, event ):
        Ma_so = self.edtMaSo.GetValue()
        sanPham = SanPham('Du_lieu/quan_ly_ban_hang.db')
        sp = sanPham.SanPhamTheoMaSo(Ma_so)
        self.edtTen.SetValue(sp['Ten'])
        self.edtKyHieu.SetValue(sp['Ky_hieu'])
        self.edtDonGiaNhap.SetValue(str(sp['Don_gia_nhap']))
        self.edtDonGiaBan.SetValue(str(sp['Don_gia_ban']))
        self.edtSoLuongTon.SetValue(str(sp['So_luong_ton']))

        i = self.m_choice_nhom_san_pham.FindString(sp['Nhom_san_pham'])
        self.m_choice_nhom_san_pham.Select(i)
    
    def cap_nhat_click( self, event ):
        Ma_so = self.edtMaSo.GetValue()
        Ten = self.edtTen.GetValue()
        Ky_hieu = self.edtKyHieu.GetValue()
        Don_gia_nhap = self.edtDonGiaNhap.GetValue()
        So_luong_ton = self.edtSoLuongTon.GetValue()
        Don_gia_ban = self.edtDonGiaBan.GetValue()
        Nhom_san_pham = self.m_choice_nhom_san_pham.GetString(self.m_choice_nhom_san_pham.GetSelection())

        try:
            sp = SanPham('Du_lieu/quan_ly_ban_hang.db')
            n = sp.CapNhatSanPham(Ten, Ma_so, Ky_hieu, Don_gia_nhap, Don_gia_ban, So_luong_ton, Nhom_san_pham)
            if n > 0:
                dlg = wx.MessageDialog(None, "Cập nhật sản phẩm thành công", "Thông báo", wx.OK)
            else:
                dlg = wx.MessageDialog(None, "Cập nhật sản phẩm không thành công", "Thông báo", wx.OK)
        except:
            dlg = wx.MessageDialog(None, "Cập nhật sản phẩm không thành công", "Thông báo", wx.OK)
        finally:
            sp.deConnect()
            dlg.ShowModal()
            self.Close()
    
    def xoa_click( self, event ):
        Ma_so = self.edtMaSo.GetValue()
        if Ma_so != None and Ma_so != "":
            try:
                sp = SanPham('Du_lieu/quan_ly_ban_hang.db')
                n = sp.XoaSanPham(Ma_so)
                if n > 0:
                    dlg = wx.MessageDialog(None, "Xóa sản phẩm thành công", "Thông báo", wx.OK)
                else:
                    dlg = wx.MessageDialog(None, "Xóa sản phẩm không thành công", "Thông báo", wx.OK)
            except:
                dlg = wx.MessageDialog(None, "Xóa sản phẩm không thành công", "Thông báo", wx.OK)
            finally:
                sp.deConnect()
                dlg.ShowModal()
                self.Close()