import json
from Xu_ly.Xu_ly_Database import *

class NhanVien(Database):
    def __init__(self, file_db):
        Database.__init__(self, file_db)

    def DanhSachNhanVien(self):
        chuoiSQL='select Ho_ten, Ma_so, Ten_dang_nhap from tblNhanVien'
        ds = Database.getAll(self, chuoiSQL)
        lstNhanVien = []
        if ds != None:
            for item in ds:
                nv = {'Ho_ten': item[0], 'Ma_so': item[1], 'Ten_dang_nhap': item[2]}
                lstNhanVien.append(nv)
        return lstNhanVien

    def NhanVienTheoMaSo(self, Ma_so):
        chuoiSQL = 'select Ho_ten, Ma_so, Ten_dang_nhap from tblNhanVien where Ma_so = ?'
        nv = Database.getOne(self, chuoiSQL,(Ma_so,))
        return {'Ho_ten': nv[0], 'Ma_so': nv[1], 'Ten_dang_nhap': nv[2]}

    def ThemNhanVien(self, Ho_ten, Ma_so, Ten_dang_nhap, Mat_khau):
        chuoiSQL = 'insert into tblNhanVien(Ho_ten, Ma_so, Ten_dang_nhap, Mat_khau) values(?,?,?,?)'
        return Database.execute(self, chuoiSQL, (Ho_ten, Ma_so, Ten_dang_nhap, Mat_khau))

    def CapNhatNhanVien(self, Ho_ten, Ma_so, Ten_dang_nhap):
        chuoiSQL = 'update tblNhanVien set Ho_ten = ?, Ten_dang_nhap = ? where Ma_so = ?'
        return Database.execute(self, chuoiSQL, (Ho_ten, Ten_dang_nhap, Ma_so))

    def XoaNhanVien(self, Ma_so):
        chuoiSQL = 'delete from tblNhanVien where Ma_so = ?'
        return Database.execute(self, chuoiSQL,(Ma_so,))