package com.example.hoclaixe.model;

public class CauHoi {
    int id;
    String Ma_so;
    String Ten;
    String Noi_dung;
    String Co_hinh;
    String Danh_sach_Chon_lua;

    public CauHoi() {

    }

    public CauHoi(int id, String ma_so, String ten, String noi_dung, String co_hinh, String danh_sach_Chon_lua) {
        this.id = id;
        Ma_so = ma_so;
        Ten = ten;
        Noi_dung = noi_dung;
        Co_hinh = co_hinh;
        Danh_sach_Chon_lua = danh_sach_Chon_lua;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getMa_so() {
        return Ma_so;
    }

    public void setMa_so(String ma_so) {
        Ma_so = ma_so;
    }

    public String getTen() {
        return Ten;
    }

    public void setTen(String ten) {
        Ten = ten;
    }

    public String getNoi_dung() {
        return Noi_dung;
    }

    public void setNoi_dung(String noi_dung) {
        Noi_dung = noi_dung;
    }

    public String getCo_hinh() {
        return Co_hinh;
    }

    public void setCo_hinh(String co_hinh) {
        Co_hinh = co_hinh;
    }

    public String getDanh_sach_Chon_lua() {
        return Danh_sach_Chon_lua;
    }

    public void setDanh_sach_Chon_lua(String danh_sach_Chon_lua) {
        Danh_sach_Chon_lua = danh_sach_Chon_lua;
    }
}