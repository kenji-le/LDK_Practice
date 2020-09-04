import json
from Xu_ly.Xu_ly_Database import *

class SanPham(Database):
    def __init__(self, file_db):
        Database.__init__(self, file_db)

    def DanhSachSanPham(self):
        chuoiSQL = 'select Ten, Ma_so, Ky_hieu, Don_gia_nhap, Don_gia_ban, So_luong_ton, Nhom_san_pham from tblSanPham'
        ds = Database.getAll(self, chuoiSQL)
        lstSanPham = []
        if ds != None:
            for item in ds:
                sp = {'Ten': item[0], 'Ma_so': item[1],'Ky_hieu': item[2],'Don_gia_nhap': item[3],'Don_gia_ban': item[4],'So_luong_ton': item[5],'Nhom_san_pham': item[6]}
                lstSanPham.append(sp)
        return lstSanPham

    def SanPhamTheoMaSo(self, Ma_so):
        chuoiSQL = 'select Ten, Ky_hieu, Don_gia_nhap, Don_gia_ban, So_luong_ton, Nhom_san_pham from tblSanPham where Ma_so = ?'
        item = Database.getOne(self, chuoiSQL, (Ma_so,))
        return {'Ten': item[0],'Ky_hieu': item[1], 'Don_gia_nhap': item[2], 'Don_gia_ban': item[3], 'So_luong_ton': item[4], 'Nhom_san_pham': item[5]}

    def ThemSanPham(self, Ten, Ma_so, Ky_hieu, Don_gia_ban, Don_gia_nhap, So_luong_ton, Nhom_san_pham):
        chuoiSQL = 'insert into tblSanPham(Ten, Ma_so, Ky_hieu, Don_gia_ban, Don_gia_nhap, So_luong_ton, Nhom_san_pham) values(?,?,?,?,?,?,?)'
        return Database.execute(self, chuoiSQL,(Ten, Ma_so, Ky_hieu, Don_gia_ban, Don_gia_nhap, So_luong_ton, Nhom_san_pham))

    def CapNhatSanPham(self, Ten, Ma_so, Ky_hieu, Don_gia_nhap, Don_gia_ban, So_luong_ton, Nhom_san_pham):
        chuoiSQL = 'update tblSanPham set Ten = ? , Ky_hieu = ?, Don_gia_nhap = ?, Don_gia_ban = ?, So_luong_ton = ?, Nhom_san_pham = ? where Ma_so = ?'
        return Database.execute(self, chuoiSQL,(Ten, Ky_hieu, Don_gia_nhap, Don_gia_ban, So_luong_ton, Nhom_san_pham, Ma_so))

    def XoaSanPham(self, Ma_so):
        chuoiSQL = 'delete from tblSanPham where Ma_so = ?'
        return Database.execute(self, chuoiSQL,(Ma_so,))