import json
from Xu_ly.Xu_ly_Database import *
from Giao_dien.PanelNhomSanPham import *

class NhomSanPham(Database):
    def __init__(self, file_db):
        Database.__init__(self, file_db)

    def DanhSachNhomSanPham(self):
        chuoiSQL='select Ma_nhom, Ten_nhom from tblNhomSanPham'
        ds = Database.getAll(self, chuoiSQL)
        lstNhomSanPham = []
        if ds != None:
            for item in ds:
                sp = {'Ma_nhom': item[0], 'Ten_nhom': item[1]}
                lstNhomSanPham.append(sp)
        return lstNhomSanPham

    def ThemNhomSanPham(self, Ma_nhom, Ten_nhom):
        chuoiSQL='INSERT INTO tblNhomSanPham(Ma_nhom, Ten_nhom) VALUES(?,?)'
        return Database.execute(self, chuoiSQL, (Ma_nhom, Ten_nhom))