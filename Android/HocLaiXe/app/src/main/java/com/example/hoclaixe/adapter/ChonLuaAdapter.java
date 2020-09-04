package com.example.hoclaixe.adapter;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.example.hoclaixe.R;
import com.example.hoclaixe.model.ChonLua;

import java.util.List;


public class ChonLuaAdapter extends ArrayAdapter<ChonLua> {
    Context context;
    List<ChonLua> myArray;
    int layoutId;


    public ChonLuaAdapter(Context context, int layoutId, List<ChonLua> arr){
        super(context, layoutId, arr);
        this.context = context;
        this.layoutId = layoutId;
        this.myArray = arr;
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
                LayoutInflater inflator = LayoutInflater.from(context);
                convertView = inflator.inflate(layoutId, null);
                viewHolder = new ViewHolder();
                viewHolder.tvCau = (TextView) convertView.findViewById(R.id.tvCau);
                viewHolder.tvNoi_dung = (TextView) convertView.findViewById(R.id.tvNoi_dung);
                viewHolder.imgDapAn = convertView.findViewById(R.id.imgDapAn);
                convertView.setTag(viewHolder);
                convertView.setTag(R.id.tvCau, viewHolder.tvCau);
                convertView.setTag(R.id.tvNoi_dung, viewHolder.tvNoi_dung);
                convertView.setTag(R.id.imgDapAn, viewHolder.imgDapAn);
            } else {
                viewHolder = (ViewHolder) convertView.getTag();
            }

            viewHolder.tvCau.setText(String.valueOf(myArray.get(position).getCau()));
            viewHolder.tvNoi_dung.setText(myArray.get(position).getNoi_dung());
        } catch (Exception ex) {
            Toast.makeText(context,ex.getMessage(),Toast.LENGTH_SHORT).show();
        }
        return convertView;
    }
}
