package com.example.hoclaixe.dao;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import com.example.hoclaixe.model.CauHoi;
import com.example.hoclaixe.util.Utils;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.ArrayList;


public class CauHoiDAO extends SQLiteOpenHelper {
    private Context mContext;
    private SQLiteDatabase mDatabase;
    
    public CauHoiDAO(Context context) {
        super(context, Utils.DBNAME, null, 1);
        this.mContext = context;
    }
    
    @Override
    public void onCreate(SQLiteDatabase db) {
        
    }
    
    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        
    }
    
    public void openDatabase() {
        String dbPath = mContext.getDatabasePath(Utils.DBNAME).getPath();
        if (mDatabase != null && mDatabase.isOpen()) {
            return;
        }
        mDatabase = SQLiteDatabase.openDatabase(dbPath, null, SQLiteDatabase.OPEN_READWRITE);
    }
    
    public void closeDatabase() {
        if (mDatabase != null) {
            mDatabase.close();
        }
    }
    
    public int addCauHoi(JSONArray ChuoidsCauHoi) {
        try {
            ContentValues contentValues;
            openDatabase();
            int n = ChuoidsCauHoi.length();
            for (int i = 0; i < ChuoidsCauHoi.length(); i++){
                JSONObject objCauHoi = ChuoidsCauHoi.getJSONObject(i);
                contentValues = new ContentValues();

                try {
                    contentValues.put("id", objCauHoi.getInt("id"));
                    contentValues.put("Ma_so", objCauHoi.getString("Ma_so"));
                    contentValues.put("Ten", objCauHoi.getString("Ten"));
                    contentValues.put("Noi_dung", objCauHoi.getString("Noi_dung"));
                    contentValues.put("Co_hinh", objCauHoi.getString("Co_hinh"));
                    contentValues.put("Danh_sach_Chon_lua", objCauHoi.getString("Danh_sach_Chon_lua"));
                    mDatabase.insert("CHTN", null, contentValues);
                } catch (Exception ex) {
                    System.out.print(ex.getMessage());
                }
            }
            closeDatabase();
            return n;
        } catch (Exception e) {
            return 0;
        }
    }
    
    public boolean DeleteAllCauHoi() {
        openDatabase();
        int result = mDatabase.delete("CHTN",  null, null);
        closeDatabase();
        return result != 0;
    }
    
    public ArrayList<CauHoi> DanhSachCauHoi() {
        ArrayList<CauHoi> dsCauHoi = new ArrayList<CauHoi>();
        openDatabase();
        Cursor cursor = mDatabase.rawQuery("select id, Ma_so, Ten, Noi_dung, Co_hinh, Danh_sach_Chon_lua From CHTN where Co_hinh !='' order by id", null);
        cursor.moveToFirst();

        while (!cursor.isAfterLast()) {
            CauHoi chtn = new CauHoi();
            chtn.setId(cursor.getInt(0));
            chtn.setMa_so(cursor.getString(1));
            chtn.setTen(cursor.getString(2));
            chtn.setNoi_dung(cursor.getString(3));
            chtn.setCo_hinh(cursor.getString(4));
            chtn.setDanh_sach_Chon_lua(cursor.getString(5));
            dsCauHoi.add(chtn);
            cursor.moveToNext();
        }

        cursor.close();
        closeDatabase();
        return dsCauHoi;
    }
    
    private boolean CheckNumber(int dsCauHoi[], int number) {
        boolean flag = false;
        for (int i = 0; i < dsCauHoi.length; i++) {
            if (dsCauHoi[i] == number) {
                flag = true;
                break;
            }
        }
        return flag;
    }
    
    public ArrayList<CauHoi> DanhSachCauHoiThiThu(int dsCauHoi[]) {
        ArrayList<CauHoi> dsHoaDon = new ArrayList<CauHoi>();
        openDatabase();
        Cursor cursor = mDatabase.rawQuery("select id, Ma_so, Ten, Noi_dung, Co_hinh, Danh_sach_Chon_lua From CHTN order by id", null);
        cursor.moveToFirst();
        int i = 0;
        while (!cursor.isAfterLast()) {
            if (CheckNumber(dsCauHoi, i)) {
                CauHoi chtn = new CauHoi();
                chtn.setId(cursor.getInt(0));
                chtn.setMa_so(cursor.getString(1));
                chtn.setTen(cursor.getString(2));
                chtn.setNoi_dung(cursor.getString(3));
                chtn.setCo_hinh(cursor.getString(4));
                chtn.setDanh_sach_Chon_lua(cursor.getString(5));
                dsHoaDon.add(chtn);
            }
            i++;
            cursor.moveToNext();
        }
        cursor.close();
        closeDatabase();
        return dsHoaDon;
    }
    
    public int getCauHoiCount() {
        openDatabase();
        Cursor cursor = mDatabase.rawQuery("select count(*) From CHTN", null);
        int count = 0;

        if (null != cursor) {
            if (cursor.getCount() > 0) {
                cursor.moveToFirst();
                count = cursor.getInt(0);
            }
        }

        cursor.close();
        closeDatabase();
        return count;
    }
    
    public boolean DeleteDatabase() {
        closeDatabase();
        return  mContext.deleteDatabase(Utils.DBNAME);
    }
}