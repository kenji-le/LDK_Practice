package com.example.hoclaixe.activity;

import android.support.v4.view.ViewPager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.Toast;

import com.example.hoclaixe.R;
import com.example.hoclaixe.adapter.HocLyThuyetAdapter;
import com.example.hoclaixe.model.CauHoi;
import com.example.hoclaixe.dao.CauHoiDAO;

import java.util.ArrayList;
import java.util.List;

public class HocLyThuyetActivity extends AppCompatActivity {

    ViewPager viewPager_HocLyThuyet;
    List<CauHoi> lstCauHoi = new ArrayList<CauHoi>();
    HocLyThuyetAdapter hocLyThuyetAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_hoc_ly_thuyet);
        try {
            viewPager_HocLyThuyet = (ViewPager) findViewById(R.id.viewPager_HocLyThuyet);
            CauHoiDAO m_chtn = new CauHoiDAO(getApplicationContext());
            lstCauHoi = m_chtn.DanhSachCauHoi();
            hocLyThuyetAdapter = new HocLyThuyetAdapter(HocLyThuyetActivity.this, R.layout.item_cau_hoi, lstCauHoi);
            viewPager_HocLyThuyet.setAdapter(hocLyThuyetAdapter);
        } catch (Exception ex) {
            Toast.makeText(HocLyThuyetActivity.this,ex.getMessage(),Toast.LENGTH_LONG).show();
        }
    }
}
