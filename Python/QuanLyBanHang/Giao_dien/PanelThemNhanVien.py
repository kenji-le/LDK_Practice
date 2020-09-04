import wx
import wx.xrc
from Xu_ly.Xu_ly_NhanVien import *

class PanelThemNhanVien ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.TAB_TRAVERSAL )
        
        gbSizer2 = wx.GridBagSizer( 0, 0 )
        gbSizer2.SetFlexibleDirection( wx.BOTH )
        gbSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Thông tin nhân viên", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTRE )
        self.m_staticText8.Wrap( -1 )
        self.m_staticText8.SetFont( wx.Font( 14, 70, 90, 92, False, "Lucida Grande" ) )
        
        gbSizer2.Add( self.m_staticText8, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Họ tên", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText9.Wrap( -1 )
        gbSizer2.Add( self.m_staticText9, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.edtHoTen = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
        gbSizer2.Add( self.edtHoTen, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.errHoTen = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.errHoTen.Wrap( -1 )
        self.errHoTen.SetForegroundColour( wx.Colour( 251, 1, 6 ) )
        
        gbSizer2.Add( self.errHoTen, wx.GBPosition( 1, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.errMaSo = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.errMaSo.Wrap( -1 )
        self.errMaSo.SetForegroundColour( wx.Colour( 251, 1, 6 ) )
        
        gbSizer2.Add( self.errMaSo, wx.GBPosition( 2, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.errTenDangNhap = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.errTenDangNhap.Wrap( -1 )
        self.errTenDangNhap.SetForegroundColour( wx.Colour( 251, 1, 6 ) )
        
        gbSizer2.Add( self.errTenDangNhap, wx.GBPosition( 3, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.errMatKhau = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.errMatKhau.Wrap( -1 )
        self.errMatKhau.SetForegroundColour( wx.Colour( 251, 1, 6 ) )
        
        gbSizer2.Add( self.errMatKhau, wx.GBPosition( 4, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.errXacNhanMK = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        self.errXacNhanMK.Wrap( -1 )
        self.errXacNhanMK.SetForegroundColour( wx.Colour( 251, 1, 6 ) )
        
        gbSizer2.Add( self.errXacNhanMK, wx.GBPosition( 5, 2 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Mã số", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )
        gbSizer2.Add( self.m_staticText10, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.edtMaSo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.edtMaSo, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, u"Tên đăng nhập", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )
        gbSizer2.Add( self.m_staticText11, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.edtTenDangNhap = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.edtTenDangNhap, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"Mật khẩu", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText12.Wrap( -1 )
        gbSizer2.Add( self.m_staticText12, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.edtMatKhau = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        gbSizer2.Add( self.edtMatKhau, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText13 = wx.StaticText( self, wx.ID_ANY, u"Xác nhận mật khẩu", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText13.Wrap( -1 )
        gbSizer2.Add( self.m_staticText13, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.edtXacNhanMK = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
        gbSizer2.Add( self.edtXacNhanMK, wx.GBPosition( 5, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.btnThem = wx.Button( self, wx.ID_ANY, u"Thêm", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer2.Add( self.btnThem, wx.GBPosition( 6, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.EXPAND, 5 )
        
        
        self.SetSizer( gbSizer2 )
        self.Layout()
        
        # Connect Events
        self.btnThem.Bind( wx.EVT_BUTTON, self.btnThem_click )
    
    def __del__( self ):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def btnThem_click( self, event ):
        Ho_ten = self.edtHoTen.GetValue()
        Ma_so = self.edtMaSo.GetValue()
        Ten_dang_nhap = self.edtTenDangNhap.GetValue()
        Mat_khau = self.edtMatKhau.GetValue()
        Xac_nhan_MK = self.edtXacNhanMK.GetValue()

        Hop_le = True
        if Ho_ten == None or len(Ho_ten) == 0:
            self.errHoTen.SetLabel('*')
            Hop_le = False
        else:
            self.errHoTen.SetLabel('')

        if Ma_so == None or len(Ma_so) == 0:
            self.errMaSo.SetLabel('*')
            Hop_le = False
        else:
            self.errMaSo.SetLabel('')

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
                n = nv.ThemNhanVien(Ho_ten, Ma_so, Ten_dang_nhap, Mat_khau)
                if n > 0:
                    dlg = wx.MessageDialog(None, "Thêm nhân viên thành công", "Thông báo", wx.OK)
                else:
                    dlg = wx.MessageDialog(None, "Thêm nhân viên không thành công", "Thông báo", wx.OK)
            except:
                dlg = wx.MessageDialog(None, "Thêm nhân viên không thành công", "Thông báo", wx.OK)
            finally:
                nv.deConnect()
                dlg.ShowModal()
                self.Close()
            