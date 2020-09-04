package com.example.hoclaixe.activity;

import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import com.example.hoclaixe.R;
import com.example.hoclaixe.custom.CustomDate;
import com.example.hoclaixe.util.Utils;

import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.net.HttpURLConnection;
import java.net.URL;


public class DangKyActivity extends AppCompatActivity {
    EditText edtHoKH, edtTenKH, edtDiaChi, edtDienThoai, edtEmail, edtCMND;
    Button btnDangKy;
    CustomDate cdNgayDangKy;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dang_ky);

        edtHoKH = findViewById(R.id.edtHoKH);
        edtTenKH = findViewById(R.id.edtTenKH);
        edtDiaChi = findViewById(R.id.edtDiaChi);
        edtDienThoai = findViewById(R.id.edtDienThoai);
        edtEmail = findViewById(R.id.edtEmail);
        edtCMND = findViewById(R.id.edtCMND);
        cdNgayDangKy = findViewById(R.id.customDate);
        btnDangKy = findViewById(R.id.btnDangKy);
        btnDangKy.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                new TaskThemThongTinKhachHang().execute();
            }
        });
    }

    public class TaskThemThongTinKhachHang extends AsyncTask<Void,Void, Boolean> {
        @Override
        protected Boolean doInBackground(Void... params) {
            try {
                URL url = new URL(Utils.URL_DANGKY);
                HttpURLConnection connection = (HttpURLConnection) url.openConnection();
                connection.setRequestMethod("POST");
                connection.setRequestProperty("Content-Type", "Application/json;charset=UTF-8");

                JSONObject khach_hang = new JSONObject();
                khach_hang.put("Ho_KH", edtHoKH.getText());
                khach_hang.put("Ten_KH",edtTenKH.getText());
                khach_hang.put("Dia_chi", edtDiaChi.getText());
                khach_hang.put("Dien_thoai", edtDienThoai.getText());
                khach_hang.put("Email", edtEmail.getText());
                khach_hang.put("CMND", edtCMND.getText());
                khach_hang.put("Ngay_dang_ky", cdNgayDangKy.getDate());

                OutputStreamWriter wr = new OutputStreamWriter(connection.getOutputStream());
                wr.write(khach_hang.toString());
                wr.close();

                InputStreamReader inputStreamReader = new InputStreamReader(connection.getInputStream());
                BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
                StringBuffer stringBuffer = new StringBuffer();
                String line = bufferedReader.readLine();

                while (line != null) {
                    stringBuffer.append(line);
                    line = bufferedReader.readLine();
                }

                bufferedReader.close();
                JSONObject jsonObject = new JSONObject(stringBuffer.toString());
                return jsonObject.getInt("KetQua") == 1;
            } catch (Exception e) {
                e.printStackTrace();
                return false;
            }
        }
        @Override
        protected void onPostExecute(Boolean ketqua) {
            super.onPostExecute(ketqua);
            if (ketqua) {
                Toast.makeText(getApplication(), "Đã thêm thông tin khách hàng", Toast.LENGTH_LONG).show();
            } else {
                Toast.makeText(getApplication(), "Thêm không thành công", Toast.LENGTH_LONG).show();
            }
            finish();
        }
    }

}