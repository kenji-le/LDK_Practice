# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug 23 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import sqlite3

###########################################################################
## Class PanelThongTinCongTy
###########################################################################

class PanelThongTinCongTy ( wx.Panel ):
    
    def __init__( self, parent ):
        wx.Panel.__init__ ( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 600,400 ), style = wx.TAB_TRAVERSAL )
        
        bSizer1 = wx.BoxSizer( wx.VERTICAL )
        self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Hinh_anh/IT.jpg", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 600,150 ), 0 )
        bSizer1.Add( self.m_bitmap1, 0, wx.ALL|wx.EXPAND, 5 )
        
        gbSizer1 = wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
        
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Tên", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        gbSizer1.Add( self.m_staticText1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.mTen = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 500,-1 ), 0 )
        gbSizer1.Add( self.mTen, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Mã số", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        gbSizer1.Add( self.m_staticText2, wx.GBPosition( 1, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.mMaSo = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.mMaSo, wx.GBPosition( 1, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Điện thoại", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        gbSizer1.Add( self.m_staticText3, wx.GBPosition( 2, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.mDienThoai = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.mDienThoai, wx.GBPosition( 2, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Địa chỉ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )
        gbSizer1.Add( self.m_staticText4, wx.GBPosition( 3, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.mDiaChi = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.mDiaChi, wx.GBPosition( 3, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, u"Email", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )
        gbSizer1.Add( self.m_staticText5, wx.GBPosition( 4, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )
        
        self.mEmail = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.mEmail, wx.GBPosition( 4, 1 ), wx.GBSpan( 1, 1 ), wx.ALL|wx.EXPAND, 5 )
        
        self.mCapNhat = wx.Button( self, wx.ID_ANY, u"Cập Nhật", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.mCapNhat, wx.GBPosition( 5, 0 ), wx.GBSpan( 1, 2 ), wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
        
        bSizer1.Add( gbSizer1, 1, wx.EXPAND, 5 )
        
        self.SetSizer( bSizer1 )
        self.Layout()

        # Connect Events
        self.mCapNhat.Bind( wx.EVT_BUTTON, self.mCapNhat_click )
    
    def __del__( self ):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def mCapNhat_click( self, event ):
        conn = sqlite3.connect("Du_lieu/quan_ly_ban_hang.db")
        Ten = self.mTen.GetValue()
        MaSo = self.mMaSo.GetValue()
        DiaChi = self.mDiaChi.GetValue()
        DienThoai = self.mDienThoai.GetValue()
        Email = self.mEmail.GetValue()
        # chuoiSql = "INSERT INTO tblCongTy(Ten, Ma_so, Dien_thoai, Dia_chi, Email) VALUES(?,?,?,?,?)"
        chuoiSql = "UPDATE tblCongTy SET (Ten, Dien_thoai, Dia_chi, Email) = (?,?,?,?) WHERE Ma_so = ?"
        try:
            cursor = conn.execute(chuoiSql, (Ten, DienThoai, DiaChi, Email, MaSo))
            if cursor.rowcount > 0:
                conn.commit()
                wx.MessageBox("Cập nhật thông tin công ty thành công", "Thông báo")
            else:
                wx.MessageBox("Cập nhật thông tin công ty không thành công", "Thông báo")
        except:
            wx.MessageBox("Cập nhật thông tin công ty không thành công", "Thông báo")
        finally:
            conn.close()
            self.Close()