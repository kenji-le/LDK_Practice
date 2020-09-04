package com.example.hoclaixe.dao;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

import com.example.hoclaixe.model.Hinh;
import com.example.hoclaixe.util.Utils;

import java.util.ArrayList;


public class HinhDAO extends SQLiteOpenHelper {
    private Context mContext;
    private SQLiteDatabase mDatabase;

    public HinhDAO(Context context) {
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
        if(mDatabase!=null) {
            mDatabase.close();
        }
    }

    public int addHinh(String Ma_so, String Hinh) {
        try {
            ContentValues contentValues;
            openDatabase();
            contentValues = new ContentValues();
            try {
                contentValues.put("Ma_so",Ma_so);
                contentValues.put("Hinh",Hinh);
                mDatabase.insert("tblHinh", null, contentValues);
            } catch (Exception ex) {
                System.out.print(ex.getMessage());
            }
            closeDatabase();
            return 1;
        } catch (Exception e) {
            return 0;
        }
    }

    public boolean DeleteAllHinh() {
        openDatabase();
        int result = mDatabase.delete("tblHinh",  null, null);
        closeDatabase();
        return result !=0;
    }

    public ArrayList<Hinh> DanhSachHinh() {
        ArrayList<Hinh> dsHinh = new ArrayList<Hinh>();
        openDatabase();
        Cursor cursor = mDatabase.rawQuery("select id, Ma_so, Hinh From tblHinh order by id", null);
        cursor.moveToFirst();

        while (!cursor.isAfterLast()) {
            Hinh hinh=new Hinh();
            hinh.setId(cursor.getInt(0));
            hinh.setMa_so(cursor.getString(1));
            hinh.setHinh(cursor.getString(2));
            dsHinh.add(hinh);
            cursor.moveToNext();
        }

        cursor.close();
        closeDatabase();
        return dsHinh;
    }

    public Hinh DocHinh(String Ma_so) {
        Hinh hinh = new Hinh();
        openDatabase();
        String[] columns = {"id", "Ma_so", "Hinh"};
        Cursor cursor = mDatabase.query("tblHinh",columns,"Ma_so=?", new String[] { Ma_so }, null, null, null);
        cursor.moveToFirst();

        while (!cursor.isAfterLast()) {
            hinh.setId(cursor.getInt(0));
            hinh.setMa_so(cursor.getString(1));
            hinh.setHinh(cursor.getString(2));
            break;
        }

        cursor.close();
        closeDatabase();
        return hinh;
    }

    public boolean DeleteDatabase() {
        closeDatabase();
        return  mContext.deleteDatabase(Utils.DBNAME);
    }
}

