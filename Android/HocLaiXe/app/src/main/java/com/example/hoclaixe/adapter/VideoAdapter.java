package com.example.hoclaixe.adapter;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.ImageView;
import android.widget.TextView;

import com.example.hoclaixe.R;
import com.example.hoclaixe.model.Video;
import com.squareup.picasso.Picasso;

import java.util.ArrayList;
import java.util.List;

public class VideoAdapter extends ArrayAdapter<Video> {
    Context context;
    int layout;
    ArrayList<Video> lstVideos;

    public VideoAdapter(Context context, int resource, List<Video> objects) {
        super(context, resource, objects);
        this.context = context;
        this.layout = resource;
        this.lstVideos = (ArrayList<Video>) objects;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        LayoutInflater layoutInflater = LayoutInflater.from(context);
        convertView = layoutInflater.inflate(layout, null);

        ImageView imgThumbnail = convertView.findViewById(R.id.imgThumbnail);
        TextView tvTitle = convertView.findViewById(R.id.tvTitle);

        Video video = lstVideos.get(position);
        String title = video.getTitle();
        String image = video.getImage();

        if (image != "") {
            Picasso.with(context).load(image).into(imgThumbnail);
        }

        tvTitle.setText(title);
        return convertView;
    }
}