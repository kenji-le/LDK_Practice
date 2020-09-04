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
## Class PanelCapNhatNhanVien
###########################################################################

class PanelCapNhatNhanVien ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
        
        gbSizer5 = wx.GridBagSizer( 0, 0 )
        gbSizer5.SetFlexibleDirection( wx.BOTH )
        gbSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText37 = wx.StaticText( self, wx.ID_ANY, u"Nhập mã số", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText37.Wrap( -1 )
        gbSizer5.Add( self.m_staticText37, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.edtMaSo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        gbSizer5.Add( self.edtMaSo, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.btnTimNhanVien = wx.Button( self, wx.ID_ANY, u"Tìm", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer5.Add( self.btnTimNhanVien, wx.GBPosition( 0, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_staticText38 = wx.StaticText( self, wx.ID_ANY, u"Họ tên", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText38.Wrap( -1 )
        gbSizer5.Add( self.m_staticText38, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.edtHoTen = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 200,-1 ), 0 )
        gbSizer5.Add( self.edtHoTen, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.errHoTen = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.errHoTen.Wrap( -1 )
        self.errHoTen.SetForegroundColour( wx.Colour( 251, 1, 6 ) )
        
        gbSizer5.Add( self.errHoTen, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.errTenDangNhap = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.errTenDangNhap.Wrap( -1 )
        self.errTenDangNhap.SetForegroundColour( wx.Colour( 251, 1, 6 ) )
        
        gbSizer5.Add( self.errTenDangNhap, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.errMatKhau = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.errMatKhau.Wrap( -1 )
        self.errMatKhau.SetForegroundColour( wx.Colour( 251, 1, 6 ) )
        
        gbSizer5.Add( self.errMatKhau, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.errXacNhanMK = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.errXacNhanMK.Wrap( -1 )
        self.errXacNhanMK.SetForegroundColour( wx.Colour( 251, 1, 6 ) )
        
        gbSizer5.Add( self.errXacNhanMK, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"Tên đăng nhập", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText41.Wrap( -1 )
        gbSizer5.Add( self.m_staticText41, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.edtTenDangNhap = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer5.Add( self.edtTenDangNhap, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText42 = wx.StaticText( self, wx.ID_ANY, u"Mật khẩu", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText42.Wrap( -1 )
        gbSizer5.Add( self.m_staticText42, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.edtMatKhau = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        gbSizer5.Add( self.edtMatKhau, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText43 = wx.StaticText( self, wx.ID_ANY, u"Xác nhận mật khẩu", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText43.Wrap( -1 )
        gbSizer5.Add( self.m_staticText43, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.edtXacNhanMK = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        gbSizer5.Add( self.edtXacNhanMK, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.btnCapNhap = wx.Button( self, wx.ID_ANY, u"Cập Nhật", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer5.Add( self.btnCapNhap, wx.GBPosition( 7, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
        
        self.btnXoaNhanVien = wx.Button( self, wx.ID_ANY, u"Xóa", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer5.Add( self.btnXoaNhanVien, wx.GBPosition( 8, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
        
        
        self.SetSizer( gbSizer5 )
        self.Layout()
        
        # Connect Events
        self.btnTimNhanVien.Bind( wx.EVT_BUTTON, self.tim_click )
        self.btnCapNhap.Bind( wx.EVT_BUTTON, self.cap_nhat_click )
        self.btnXoaNhanVien.Bind( wx.EVT_BUTTON, self.xoa_click )
    
    def __del__( self ):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def tim_click( self, event ):
        Ma_so = self.edtMaSo.GetValue()
        nhanVien = NhanVien('Du_lieu/quan_ly_ban_hang.db')
        nv = nhanVien.NhanVienTheoMaSo(Ma_so)
        self.edtHoTen.SetLabel(nv['Ho_ten'])
        self.edtTenDangNhap.SetLabel(nv['Ten_dang_nhap'])

    def cap_nhat_click( self, event ):
        Ma_so = self.edtMaSo.GetValue()
        Ho_ten = self.edtHoTen.GetValue()
        Ten_dang_nhap = self.edtTenDangNhap.GetValue()
        Mat_khau = self.edtMatKhau.GetValue()
        Xac_nhan_MK = self.edtXacNhanMK.GetValue()

        Hop_le = True
        if Ho_ten == None or len(Ho_ten) == 0:
            self.errHoTen.SetLabel('*')
            Hop_le = False
        else:
            self.errHoTen.SetLabel('')

        if Ten_dang_nhap == None or len(Ten_dang_nhap) == 0:
            self.errTenDangNhap.SetLabel('*')
            Hop_le = False
        else:
            self.errTenDangNhap.SetLabel('')

        if Mat_khau == None or len(Mat_khau) == 0:
            self.errMatKhau.SetLabel('*')
            Hop_le = False
        else:
            self.errMatKhau.SetLabel('')

        if Xac_nhan_MK != Mat_khau:
            self.errXacNhanMK.SetLabel('*')
            Hop_le = False
        else:
            self.errXacNhanMK.SetLabel('')

        if Hop_le:
            try:
                nv = NhanVien('Du_lieu/quan_ly_ban_hang.db')
                n = nv.CapNhatNhanVien(Ho_ten, Ma_so, Ten_dang_nhap)
                if n > 0:
                    dlg = wx.MessageDialog(None, "Cập nhật nhân viên thành công", "Thông báo", wx.OK)
                else:
                    dlg = wx.MessageDialog(None, "Cập nhật nhân viên không thành công", "Thông báo", wx.OK)
            except:
                dlg = wx.MessageDialog(None, "Cập nhật nhân viên không thành công", "Thông báo", wx.OK)
            finally:
                nv.deConnect()
                dlg.ShowModal()
                self.Close()

    def xoa_click( self, event ):
        Ma_so = self.edtMaSo.GetValue()
        if Ma_so != None and Ma_so != "":
            try:
                nv = NhanVien('Du_lieu/quan_ly_ban_hang.db')
                n = nv.XoaNhanVien(Ma_so)
                if n > 0:
                    dlg = wx.MessageDialog(None, "Xóa nhân viên thành công", "Thông báo", wx.OK)
                else:
                    dlg = wx.MessageDialog(None, "Xóa nhân viên không thành công", "Thông báo", wx.OK)
            except:
                dlg = wx.MessageDialog(None, "Xóa nhân viên không thành công", "Thông báo", wx.OK)
            finally:
                nv.deConnect()
                dlg.ShowModal()
                self.Close()