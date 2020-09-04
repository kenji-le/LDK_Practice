package com.example.hoclaixe.model;

public class Hinh {
    private int id;
    private String Ma_so;
    private String Hinh;

    public Hinh() {
    }

    public Hinh(int id, String ma_so, String hinh) {
        this.id = id;
        Ma_so = ma_so;
        Hinh = hinh;
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

    public String getHinh() {
        return Hinh;
    }

    public void setHinh(String hinh) {
        Hinh = hinh;
    }
}
