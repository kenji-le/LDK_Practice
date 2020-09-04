package com.example.hoclaixe.model;

public class ChonLua {
    private String Ma_so;
    private int Cau;
    private String Noi_dung;
    private boolean La_dap_an;

    public ChonLua() {

    }

    public String getMa_so() {
        return Ma_so;
    }

    public void setMa_so(String ma_so) {
        Ma_so = ma_so;
    }

    public int getCau() {
        return Cau;
    }

    public void setCau(int cau) {
        Cau = cau;
    }

    public String getNoi_dung() {
        return Noi_dung;
    }

    public void setNoi_dung(String noi_dung) {
        Noi_dung = noi_dung;
    }

    public boolean isLa_dap_an() {
        return La_dap_an;
    }

    public void setLa_dap_an(boolean la_dap_an) {
        La_dap_an = la_dap_an;
    }
}