package com.example.hoclaixe.adapter;

import android.app.Activity;
import android.graphics.Color;
import android.support.v4.view.PagerAdapter;
import android.support.v4.view.ViewPager;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.AdapterView;
import android.widget.ImageView;
import android.widget.ListView;
import android.widget.TextView;

import com.example.hoclaixe.R;
import com.example.hoclaixe.model.CauHoi;
import com.example.hoclaixe.model.ChonLua;

import com.example.hoclaixe.util.Utils;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class ThiThuAdapter extends PagerAdapter {
    public Activity context;
    private List<CauHoi> chtns;
    ChonDapAnThiThuAdapter chonDapAnAdapter;
    int nop_bai;

    public ThiThuAdapter(Activity context, List<CauHoi> chtns, int nop_bai) {
        this.context = context;
        this.chtns = chtns;
        this.nop_bai=nop_bai;
    }

    @Override
    public int getCount() {
        return chtns.size();
    }

    @Override
    public boolean isViewFromObject(View view, Object object) {
        return view == object;
    }

    @Override
    public Object instantiateItem(ViewGroup container, int position) {
        LayoutInflater inflater = LayoutInflater.from(context);
        View view = inflater.inflate(R.layout.item_cau_hoi, null);
        TextView tvNoi_dung = view.findViewById(R.id.tvNoi_dung);
        tvNoi_dung.setText(chtns.get(position).getNoi_dung());
        ImageView imgHinh = view.findViewById(R.id.imgHinh);
        TextView tvDapAnDung = view.findViewById(R.id.tvDapAnDung);
        tvDapAnDung.setText("Câu đúng: ");
        //tvDapAnDung.setText(Utils.dsCauHVChonTraLoi[position]);
        if (nop_bai != 0) {
            tvDapAnDung.setVisibility(View.VISIBLE);
        } else {
            tvDapAnDung.setVisibility(View.GONE);
        }

        if (chtns.get(position).getCo_hinh().length() > 0) {
            imgHinh.setImageBitmap(Utils.getBitmapFromString(this.context.getBaseContext(), chtns.get(position).getMa_so()));
        }

        try {
            //list chon dap an
            final ListView lvChonDapAn = view.findViewById(R.id.lvChonDapAn);;
            final ArrayList<ChonLua> arrayListDapAn = new ArrayList<ChonLua>();
            JSONArray dsChonLua = new JSONArray(chtns.get(position).getDanh_sach_Chon_lua());
            for(int i = 0; i < dsChonLua.length(); i++){
                JSONObject chonlua = dsChonLua.getJSONObject(i);
                ChonLua dapAn = new ChonLua();
                dapAn.setCau(i + 1);
                dapAn.setNoi_dung(chonlua.getString("Noi_dung"));
                if (chonlua.getString("La_dap_an").toLowerCase().equals("true")) {
                    dapAn.setLa_dap_an(true);
                    Utils.dsCauChonLuaDung[position] = Utils.dsCauChonLuaDung[position] + String.valueOf(i + 1) + ",";
                    String cauChon = tvDapAnDung.getText().toString();
                    if (cauChon.equals("Câu đúng: ")) {
                        tvDapAnDung.setText(String.valueOf(i + 1));
                    } else {
                        tvDapAnDung.setText(cauChon + ", " + String.valueOf(i + 1));
                    }
                } else {
                    dapAn.setLa_dap_an(false);
                }
                arrayListDapAn.add(dapAn);
            }
            chonDapAnAdapter = new ChonDapAnThiThuAdapter(this.context, R.layout.item_chon_lua, arrayListDapAn, this.nop_bai, position);
            lvChonDapAn.setAdapter(chonDapAnAdapter);
            lvChonDapAn.setOnItemClickListener(new AdapterView.OnItemClickListener() {
                @Override
                public void onItemClick(AdapterView<?> adapterView, View view, int position, long l) {
                    String noi_dung_tra_loi = Utils.dsCauHVChonTraLoi[Utils.trangHienHanh];
                    int kq = noi_dung_tra_loi.indexOf(String.valueOf(position + 1));
                    if (((ImageView) view.findViewById(R.id.imgDapAn)).getVisibility() == View.GONE) {
                        if (kq == -1) {
                            noi_dung_tra_loi += String.valueOf(position + 1) + ",";
                            Utils.dsCauHVChonTraLoi[Utils.trangHienHanh] = noi_dung_tra_loi;
                        }
                        ((TextView) view.findViewById(R.id.tvCau)).setTextColor(Color.WHITE);
                        ((TextView) view.findViewById(R.id.tvCau)).setBackground(context.getResources().getDrawable(R.drawable.circle_textview_background_green));
                        ((TextView) view.findViewById(R.id.tvNoi_dung)).setTextColor(Color.parseColor("#003300"));
                        ((ImageView) view.findViewById(R.id.imgDapAn)).setVisibility(View.VISIBLE);
                    } else {
                        if (kq != -1) {
                            noi_dung_tra_loi = noi_dung_tra_loi.replace(String.valueOf(position + 1) + ",","");
                            Utils.dsCauHVChonTraLoi[Utils.trangHienHanh] = noi_dung_tra_loi;
                        }
                        ((TextView) view.findViewById(R.id.tvCau)).setTextColor(Color.BLACK);
                        ((TextView) view.findViewById(R.id.tvCau)).setBackground(context.getResources().getDrawable(R.drawable.circle_textview));
                        ((TextView) view.findViewById(R.id.tvNoi_dung)).setTextColor(Color.BLACK);
                        ((ImageView) view.findViewById(R.id.imgDapAn)).setVisibility(View.GONE);
                    }
                }
            });
            //end list chon dap an
        } catch (Exception ex) {
            ex.printStackTrace();
        }
        ViewPager viewPager = (ViewPager) container;
        viewPager.addView(view, 0);
        return view;
    }

    @Override
    public void destroyItem(ViewGroup container, int position, Object object) {
        ViewPager viewPager = (ViewPager) container;
        View view = (View) object;
        viewPager.removeView(view);
    }
}