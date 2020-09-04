# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Aug 23 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from Giao_dien.PanelThongTinCongTy import *
from Giao_dien.PanelDanhSachNhanVien import *
from Giao_dien.PanelThemNhanVien import *
from Giao_dien.PanelCapNhatNhanVien import *
from Giao_dien.PanelNhomSanPham import *
from Giao_dien.PanelDanhSachSanPham import *
from Giao_dien.PanelThemSanPham import *
from Giao_dien.PanelCapNhatSanPham import *

###########################################################################
## Class FrmQuanLyBanHang
###########################################################################

class FrmQuanLyBanHang ( wx.MDIParentFrame ):
    
    def __init__( self ):
        wx.Frame.__init__ ( self, None, id = wx.ID_ANY, title = u"Quản Lý Bán Hàng", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
        
        self.m_menubar_quan_ly_ban_hang = wx.MenuBar( 0 )
        self.m_menu_file = wx.Menu()
        self.m_menuItem_thoat = wx.MenuItem( self.m_menu_file, wx.ID_ANY, u"Thoát", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_file.Append( self.m_menuItem_thoat )
        
        self.m_menubar_quan_ly_ban_hang.Append( self.m_menu_file, u"File" ) 
        
        self.m_menu_cong_ty = wx.Menu()
        self.m_menuItem_thong_tin_cong_ty = wx.MenuItem( self.m_menu_cong_ty, wx.ID_ANY, u"Thông tin công ty", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_cong_ty.Append( self.m_menuItem_thong_tin_cong_ty )
        
        self.m_menubar_quan_ly_ban_hang.Append( self.m_menu_cong_ty, u"Công Ty" ) 
        
        self.m_menu_nhan_vien = wx.Menu()
        self.m_menuItem_danh_sach_nhan_vien = wx.MenuItem( self.m_menu_nhan_vien, wx.ID_ANY, u"Danh sách nhân viên", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_nhan_vien.Append( self.m_menuItem_danh_sach_nhan_vien )
        
        self.m_menuItem_them_nhan_vien = wx.MenuItem( self.m_menu_nhan_vien, wx.ID_ANY, u"Thêm nhân viên", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_nhan_vien.Append( self.m_menuItem_them_nhan_vien )
        
        self.m_menuItem_cap_nhat_nhan_vien = wx.MenuItem( self.m_menu_nhan_vien, wx.ID_ANY, u"Cập nhật nhân viên", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_nhan_vien.Append( self.m_menuItem_cap_nhat_nhan_vien )
        
        self.m_menubar_quan_ly_ban_hang.Append( self.m_menu_nhan_vien, u"Nhân Viên" ) 
        
        self.m_menu_san_pham = wx.Menu()
        self.m_menuItem_nhom_san_pham = wx.MenuItem( self.m_menu_san_pham, wx.ID_ANY, u"Nhóm sản phẩm", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_san_pham.Append( self.m_menuItem_nhom_san_pham )
        
        self.m_menuItem_danh_sach_san_pham = wx.MenuItem( self.m_menu_san_pham, wx.ID_ANY, u"Danh sách sản phẩm", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_san_pham.Append( self.m_menuItem_danh_sach_san_pham )
        
        self.m_menuItem_them_san_pham = wx.MenuItem( self.m_menu_san_pham, wx.ID_ANY, u"Thêm sản phầm", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_san_pham.Append( self.m_menuItem_them_san_pham )
        
        self.m_menuItem_cap_nhat_san_pham = wx.MenuItem( self.m_menu_san_pham, wx.ID_ANY, u"Cập nhật sản phẩm", wx.EmptyString, wx.ITEM_NORMAL )
        self.m_menu_san_pham.Append( self.m_menuItem_cap_nhat_san_pham )
        
        self.m_menubar_quan_ly_ban_hang.Append( self.m_menu_san_pham, u"Sản Phẩm" ) 
        
        self.SetMenuBar( self.m_menubar_quan_ly_ban_hang )
        
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.Bind( wx.EVT_MENU, self.thoat_click, id = self.m_menuItem_thoat.GetId() )
        self.Bind( wx.EVT_MENU, self.thong_tin_cong_ty_click, id = self.m_menuItem_thong_tin_cong_ty.GetId() )
        self.Bind( wx.EVT_MENU, self.danh_sach_nhan_vien_click, id = self.m_menuItem_danh_sach_nhan_vien.GetId() )
        self.Bind( wx.EVT_MENU, self.them_nhan_vien_click, id = self.m_menuItem_them_nhan_vien.GetId() )
        self.Bind( wx.EVT_MENU, self.cap_nhat_nhan_vien_click, id = self.m_menuItem_cap_nhat_nhan_vien.GetId() )
        self.Bind( wx.EVT_MENU, self.nhom_san_pham_click, id = self.m_menuItem_nhom_san_pham.GetId() )
        self.Bind( wx.EVT_MENU, self.danh_sach_san_pham_click, id = self.m_menuItem_danh_sach_san_pham.GetId() )
        self.Bind( wx.EVT_MENU, self.them_san_pham_click, id = self.m_menuItem_them_san_pham.GetId() )
        self.Bind( wx.EVT_MENU, self.cap_nhat_san_pham_click, id = self.m_menuItem_cap_nhat_san_pham.GetId() )
    
    def __del__( self ):
        pass
    
    # Virtual event handlers, overide them in your derived class
    def thoat_click( self, event ):
        self.Close()
    
    def thong_tin_cong_ty_click( self, event ):
        window = wx.MDIChildFrame(self, title="Thông tin công ty", size=(600,400))
        panel = PanelThongTinCongTy(window)

        conn = sqlite3.connect("Du_lieu/quan_ly_ban_hang.db")
        sql = "SELECT Ten, Ma_so, Dien_thoai, Dia_chi, Email FROM tblCongTy"
        cursor = conn.execute(sql)
        congty = cursor.fetchone()
        conn.close()

        if congty != None:
            panel.mTen.SetValue(congty[0])
            panel.mMaSo.SetValue(congty[1])
            panel.mDienThoai.SetValue(congty[2])
            panel.mDiaChi.SetValue(congty[3])
            panel.mEmail.SetValue(congty[4])
        
        window.CenterOnParent(wx.BOTH)
        window.Show(True)
    
    def danh_sach_nhan_vien_click( self, event ):
        window = wx.MDIChildFrame(self, title="Danh sách nhân viên", size=(600,400))
        panel = PanelDanhSachNhanVien(window)
        window.CenterOnParent(wx.BOTH)
        window.Show(True)
    
    def them_nhan_vien_click( self, event ):
        window = wx.MDIChildFrame(self, title="Thêm nhân viên", size=(600,400))
        panel = PanelThemNhanVien(window)

        conn = sqlite3.connect("Du_lieu/quan_ly_ban_hang.db")
        sql = "SELECT Ho_ten, Ma_so, Ten_dang_nhap, Mat_khau FROM tblNhanVien"
        cursor = conn.execute(sql)
        nhanVien = cursor.fetchone()
        conn.close()

        if nhanVien != None:
            panel.edtHoTen.SetValue(nhanVien[0])
            panel.edtMaSo.SetValue(nhanVien[1])
            panel.edtTenDangNhap.SetValue(nhanVien[2])
            panel.edtMatKhau.SetValue(nhanVien[3])
            panel.edtXacNhanMK.SetValue(nhanVien[3])

        window.CenterOnParent(wx.BOTH)
        window.Show(True)
    
    def cap_nhat_nhan_vien_click( self, event ):
        window = wx.MDIChildFrame(self, title="Cập nhật nhân viên", size=(600,400))
        panel = PanelCapNhatNhanVien(window)
        window.CenterOnParent(wx.BOTH)
        window.Show(True)
    
    def nhom_san_pham_click( self, event ):
        window = wx.MDIChildFrame(self, title="Nhóm sản phẩm", size=(600,400))
        panel = PanelNhomSanPham(window)
        window.CenterOnParent(wx.BOTH)
        window.Show(True)

    def danh_sach_san_pham_click( self, event ):
        window = wx.MDIChildFrame(self, title="Danh sách sản phẩm", size=(600,400))
        panel = PanelDanhSachSanPham(window)
        window.CenterOnParent(wx.BOTH)
        window.Show(True)
    
    def them_san_pham_click( self, event ):
        window = wx.MDIChildFrame(self, title="Thông tin sản phẩm", size=(600,400))
        panel = PanelThemSanPham(window)

        nhomSanPham = NhomSanPham('Du_lieu/quan_ly_ban_hang.db')
        lstNhomSanPham  = nhomSanPham.DanhSachNhomSanPham()
        lstTenNhom  = []
        for item in lstNhomSanPham:
            lstTenNhom.append(item['Ten_nhom'])
        nhomSanPham.deConnect()

        panel.choiceNhomSanPham.AppendItems(lstTenNhom)
        panel.choiceNhomSanPham.Select(0)

        window.CenterOnParent(wx.BOTH)
        window.Show(True)
    
    def cap_nhat_san_pham_click( self, event ):
        window = wx.MDIChildFrame(self, title="Cập nhật sản phẩm", size=(600,400))
        panel = PanelCapNhatSanPham(window)

        nhomSanPham = NhomSanPham('Du_lieu/quan_ly_ban_hang.db')
        lstNhomSanPham  = nhomSanPham.DanhSachNhomSanPham()
        lstTenNhom  = []
        for item in lstNhomSanPham:
            lstTenNhom.append(item['Ten_nhom'])
        nhomSanPham.deConnect()

        panel.m_choice_nhom_san_pham.AppendItems(lstTenNhom)
        panel.m_choice_nhom_san_pham.Select(0)

        window.CenterOnParent(wx.BOTH)
        window.Show(True)
    

