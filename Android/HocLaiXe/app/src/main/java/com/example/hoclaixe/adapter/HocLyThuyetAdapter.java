package com.example.hoclaixe.adapter;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.Color;
import android.support.annotation.NonNull;
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

public class HocLyThuyetAdapter extends PagerAdapter {
    Context context;
    int layout;
    List<CauHoi> lstCauHoi;
    ChonLuaAdapter chonLuaAdapter;
    int trangThai = 0;

    public HocLyThuyetAdapter(Context context, int resource, List<CauHoi> objects) {
        super();
        this.context = context;
        this.layout = resource;
        this.lstCauHoi = objects;
    }

    @Override
    public int getCount() {
        return lstCauHoi.size();
    }

    @Override
    public boolean isViewFromObject(@NonNull View view, @NonNull Object o) {
        return view == o;
    }

    @NonNull
    @Override
    public Object instantiateItem(@NonNull ViewGroup container, int position) {
        LayoutInflater layoutInflater = LayoutInflater.from(context);
        View view = layoutInflater.inflate(layout, null);

        CauHoi cauHoi = lstCauHoi.get(position);
        TextView tvNoiDung = view.findViewById(R.id.tvNoi_dung);
        tvNoiDung.setText(cauHoi.getNoi_dung());

        if (cauHoi.getCo_hinh().length() > 0) {
            ImageView imgHinh = view.findViewById(R.id.imgHinh);
            Bitmap bitmap = Utils.getBitmapFromString(this.context, lstCauHoi.get(position).getMa_so());
            imgHinh.setImageBitmap(bitmap);
        }

        addListChonDapAn(view, position);

        ViewPager viewPager = (ViewPager) container;
        viewPager.addView(view, 0);
        return view;
    }



    private void addListChonDapAn(View view, int position) {
        try {
            final ListView lvChonDapAn = (ListView) view.findViewById(R.id.lvChonDapAn);
            final ArrayList<ChonLua> arrayListChonLua = new ArrayList<ChonLua>();
            JSONArray dsChonLua = new JSONArray(lstCauHoi.get(position).getDanh_sach_Chon_lua());

            for (int i = 0; i < dsChonLua.length(); i++) {
                JSONObject chonlua = dsChonLua.getJSONObject(i);
                ChonLua chonLua = new ChonLua();
                chonLua.setCau(i + 1);
                chonLua.setNoi_dung(chonlua.getString("Noi_dung"));

                if (chonlua.getString("La_dap_an").toLowerCase().equals("true")) {
                    chonLua.setLa_dap_an(true);
                } else {
                    chonLua.setLa_dap_an(false);
                }

                arrayListChonLua.add(chonLua);
            }

            chonLuaAdapter = new ChonLuaAdapter(context, R.layout.item_chon_lua, arrayListChonLua);
            lvChonDapAn.setAdapter(chonLuaAdapter);
            lvChonDapAn.setOnItemClickListener(new AdapterView.OnItemClickListener() {
                @Override
                public void onItemClick(AdapterView<?> adapterView, View view, int position, long l) {
                    if (trangThai == 0) {
                        if (arrayListChonLua.get(position).isLa_dap_an()) {
                            ((TextView) view.findViewById(R.id.tvCau)).setTextColor(Color.WHITE);
                            ((TextView) view.findViewById(R.id.tvCau)).setBackground(context.getResources().getDrawable(R.drawable.circle_textview_background_green));
                            ((TextView) view.findViewById(R.id.tvNoi_dung)).setTextColor(Color.parseColor("#003300"));
                            ((ImageView) view.findViewById(R.id.imgDapAn)).setImageDrawable(context.getResources().getDrawable(R.drawable.dap_an_dung));
                        } else {
                            ((TextView) view.findViewById(R.id.tvCau)).setTextColor(Color.WHITE);
                            ((TextView) view.findViewById(R.id.tvCau)).setBackground(context.getResources().getDrawable(R.drawable.circle_textview_background_red));
                            ((TextView) view.findViewById(R.id.tvNoi_dung)).setTextColor(Color.parseColor("#9b0029"));
                            ((ImageView) view.findViewById(R.id.imgDapAn)).setImageDrawable(context.getResources().getDrawable(R.drawable.dap_an_sai));
                        }
                        trangThai = 1;
                    } else {
                        trangThai = 0;
                        ((TextView) view.findViewById(R.id.tvCau)).setTextColor(Color.BLACK);
                        ((TextView) view.findViewById(R.id.tvCau)).setBackground(context.getResources().getDrawable(R.drawable.circle_textview));
                        ((TextView) view.findViewById(R.id.tvNoi_dung)).setTextColor(Color.BLACK);
                        ((ImageView) view.findViewById(R.id.imgDapAn)).setImageDrawable(null);
                    }
                }
            });
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Override
    public void destroyItem(ViewGroup container, int position, Object object) {
        ViewPager viewPager = (ViewPager) container;
        View view = (View) object;
        viewPager.removeView(view);
    }
}
