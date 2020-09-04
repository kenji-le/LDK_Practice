package com.example.hoclaixe.adapter;

import android.app.Activity;
import android.graphics.Color;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.example.hoclaixe.R;
import com.example.hoclaixe.model.ChonLua;
import com.example.hoclaixe.util.Utils;

import java.util.List;


public class ChonDapAnThiThuAdapter extends ArrayAdapter<ChonLua> {
    Activity context;
    List<ChonLua> lstChonLua;
    int layoutId;
    int nop_bai;
    int cau;

    public ChonDapAnThiThuAdapter(Activity context, int layoutId, List<ChonLua> arr, int nop_bai, int cau){
        super(context, layoutId, arr);
        this.context = context;
        this.layoutId = layoutId;
        this.lstChonLua = arr;
        this.nop_bai = nop_bai;
        this.cau = cau;
    }
    static class ViewHolder {
        protected TextView tvCau;
        protected TextView tvNoi_dung;
        protected ImageView imgDapAn;
    }
    @Override
    public View getView(final int position, View convertView, ViewGroup parent) {
        try {
            final ViewHolder viewHolder;
            if (convertView == null) {
                LayoutInflater inflator = context.getLayoutInflater();
                convertView = inflator.inflate(layoutId, null);
                viewHolder = new ViewHolder();
                viewHolder.tvCau = convertView.findViewById(R.id.tvCau);
                viewHolder.tvNoi_dung = convertView.findViewById(R.id.tvNoi_dung);
                viewHolder.imgDapAn = convertView.findViewById(R.id.imgDapAn);
                convertView.setTag(viewHolder);
                convertView.setTag(R.id.tvCau, viewHolder.tvCau);
                convertView.setTag(R.id.tvNoi_dung, viewHolder.tvNoi_dung);
                convertView.setTag(R.id.imgDapAn, viewHolder.imgDapAn);
            } else {
                viewHolder = (ViewHolder) convertView.getTag();
            }

            viewHolder.tvCau.setText(String.valueOf(lstChonLua.get(position).getCau()));
            viewHolder.tvNoi_dung.setText(lstChonLua.get(position).getNoi_dung());
            viewHolder.imgDapAn.setImageDrawable(context.getResources().getDrawable(R.drawable.dap_an_dung));
            viewHolder.imgDapAn.setVisibility(View.GONE);

            if (this.nop_bai == 1) {
                String cauHienHanh = String.valueOf(lstChonLua.get(position).getCau());
                if (Utils.dsCauHVChonTraLoi[this.cau].indexOf(cauHienHanh) != -1) {
                    viewHolder.tvCau.setBackground(context.getResources().getDrawable(R.drawable.circle_textview_background_green));
                    viewHolder.tvCau.setTextColor(Color.WHITE);
                    viewHolder.imgDapAn.setVisibility(View.VISIBLE);
                } else {
                    viewHolder.tvCau.setTextColor(Color.BLACK);
                    viewHolder.tvCau.setBackground(context.getResources().getDrawable(R.drawable.circle_textview));
                }
            }
        } catch (Exception ex) {
            Toast.makeText(context, ex.getMessage(), Toast.LENGTH_SHORT).show();
        }
        return convertView;
    }
}