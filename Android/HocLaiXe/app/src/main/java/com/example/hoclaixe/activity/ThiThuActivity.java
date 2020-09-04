package com.example.hoclaixe.activity;

import android.support.v4.view.ViewPager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.widget.Toolbar;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import com.example.hoclaixe.R;
import com.example.hoclaixe.adapter.ThiThuAdapter;
import com.example.hoclaixe.model.CauHoi;
import com.example.hoclaixe.dao.CauHoiDAO;
import com.example.hoclaixe.util.Utils;

import java.util.List;
import java.util.Random;

public class ThiThuActivity extends AppCompatActivity {
    int ViTriCauHoi[] = {0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0};
    ViewPager vpThiThu;
    List<CauHoi> lstCauHoi;
    TextView tvCurrent;
    Button btnPrevious, btnNext;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_thi_thu);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        TaoMangNgauNhien();
        ThemDieuKhien();
        ThemSuKien();
        vpThiThu.setCurrentItem(0);
        tvCurrent.setText("1/" + String.valueOf(ViTriCauHoi.length));
    }

    private void ThemDieuKhien() {
        try {
            tvCurrent = findViewById(R.id.tvCurrent);
            btnPrevious = findViewById(R.id.btnPrevious);
            btnNext = findViewById(R.id.btnNext);
            vpThiThu = (ViewPager) findViewById(R.id.vpThiThu);
            CauHoiDAO m_chtn = new CauHoiDAO(getApplicationContext());
            lstCauHoi = m_chtn.DanhSachCauHoiThiThu(this.ViTriCauHoi);
            vpThiThu.setAdapter(new ThiThuAdapter(this, lstCauHoi, 0));
            vpThiThu.addOnPageChangeListener(new ViewPager.OnPageChangeListener() {
                @Override
                public void onPageScrolled(int position, float positionOffset, int positionOffsetPixels) {
                }

                @Override
                public void onPageSelected(int position) {
                    Utils.trangHienHanh=position;
                    tvCurrent.setText(String.valueOf(position+1) + "/" + String.valueOf(ViTriCauHoi.length));
                }

                @Override
                public void onPageScrollStateChanged(int state) {
                }
            });
        } catch (Exception ex) {
            Toast.makeText(ThiThuActivity.this,ex.getMessage(),Toast.LENGTH_LONG).show();
        }
    }

    private boolean CheckNumber(int vitri, int number) {
        boolean flag = false;
        for (int i = 0; i < vitri; i++) {
            if (this.ViTriCauHoi[i] == number) {
                flag = true;
                break;
            }
        }
        return flag;
    }

    private void TaoMangNgauNhien() {
        CauHoiDAO m_chtn = new CauHoiDAO(this);
        int soCauHoi = m_chtn.getCauHoiCount();
        Random r = new Random();
        int vitrihientai = 0;
        while (vitrihientai < 20) {
            int cau = r.nextInt(soCauHoi);
            if (!CheckNumber(vitrihientai,cau)) {
                ViTriCauHoi[vitrihientai] = cau;
                vitrihientai++;
            }
        }
    }

    private void ThemSuKien() {
        btnPrevious.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (Utils.trangHienHanh > 0) {
                    Utils.trangHienHanh--;
                    vpThiThu.setCurrentItem(Utils.trangHienHanh);
                }
            }
        });
        btnNext.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if (Utils.trangHienHanh < ViTriCauHoi.length-1) {
                    Utils.trangHienHanh++;
                    vpThiThu.setCurrentItem(Utils.trangHienHanh);
                }
            }
        });
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_thi, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_nop_bai) {
            vpThiThu.setAdapter(new ThiThuAdapter(this, lstCauHoi,1));
            tvCurrent.setText("1/" + String.valueOf(ViTriCauHoi.length));
            ChamDiemNopBai();
            return true;
        }
        return super.onOptionsItemSelected(item);
    }

    private void ChamDiemNopBai() {
        int soCauDung = 0;
        for(int i = 0; i < Utils.dsCauChonLuaDung.length; i++){
            String cacCauHVChon = Utils.dsCauHVChonTraLoi[i];
            String cacCauDung = Utils.dsCauChonLuaDung[i];
            boolean flag = true;

            if (cacCauHVChon.equals("")) {
                flag = false;
            } else {
                String[] arrCacCauHVChon=cacCauHVChon.split(",");
                for (String chon : arrCacCauHVChon) {
                    if (cacCauDung.indexOf(chon) == -1) {
                        flag = false;
                        break;
                    }
                }
            }
            if (flag == true) {
                soCauDung++;
            }
        }

        if (soCauDung >= 16) {
            Toast.makeText(ThiThuActivity.this,"Bạn chọn đúng " + String.valueOf(soCauDung) + "/" + String.valueOf(Utils.dsCauChonLuaDung.length) + "\nKết quả: ĐẬU",Toast.LENGTH_LONG).show();
        } else {
            Toast.makeText(ThiThuActivity.this,"Bạn chọn đúng " + String.valueOf(soCauDung) + "/" + String.valueOf(Utils.dsCauChonLuaDung.length) + "\nKết quả: RỚT",Toast.LENGTH_LONG).show();
        }
    }
}

