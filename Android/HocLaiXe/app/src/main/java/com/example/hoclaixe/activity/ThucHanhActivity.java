package com.example.hoclaixe.activity;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.FrameLayout;
import android.widget.ListView;
import android.widget.Toast;

import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;
import com.example.hoclaixe.R;
import com.example.hoclaixe.adapter.VideoAdapter;
import com.example.hoclaixe.model.Video;
import com.example.hoclaixe.util.Utils;
import com.google.android.youtube.player.YouTubeInitializationResult;
import com.google.android.youtube.player.YouTubePlayer;
import com.google.android.youtube.player.YouTubePlayerSupportFragment;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

public class ThucHanhActivity extends AppCompatActivity {
    ListView lsvPlaylist;
    VideoAdapter videoAdapter;
    ArrayList<Video> lstVideos;
    YouTubePlayerSupportFragment youTubePlayerFragment;
    YouTubePlayer YPlayer;
    String videoId;
    Button btnMinimize;
    FrameLayout frameLayout;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_playlist);

        lsvPlaylist = findViewById(R.id.lsvPlaylist);
        lstVideos = new ArrayList<>();
        videoAdapter = new VideoAdapter(ThucHanhActivity.this, R.layout.item_playlist, lstVideos);
        lsvPlaylist.setAdapter(videoAdapter);
        getYoutubeAPI();

        youTubePlayerFragment = (YouTubePlayerSupportFragment) getSupportFragmentManager().findFragmentById(R.id.youtube_player_fragment);
        frameLayout = findViewById(R.id.frame_mock_player);

        lsvPlaylist.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                if (youTubePlayerFragment != null && YPlayer != null) {
                    videoId = lstVideos.get(position).getId();
                    YPlayer.loadVideo(videoId);
                    frameLayout.setVisibility(View.VISIBLE);
                    PIPActivity.getInstance().finish();
                }
            }
        });

        btnMinimize = findViewById(R.id.btnMinimize);
        btnMinimize.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(ThucHanhActivity.this, PIPActivity.class);
                intent.putExtra("videoId", videoId);
                startActivity(intent);
                frameLayout.setVisibility(View.GONE);
            }
        });
    }

    private void getYoutubeAPI() {
        final RequestQueue requestQueue = Volley.newRequestQueue(ThucHanhActivity.this);
        JsonObjectRequest jsonObjectRequest = new JsonObjectRequest(Utils.URL_PLAYLIST, null, new Response.Listener<JSONObject>() {
            @Override
            public void onResponse(JSONObject response) {
                try {
                    JSONArray jsonArray = response.getJSONArray("items");
                    for (int i=0; i<jsonArray.length(); i++) {
                        JSONObject jsonObject = (JSONObject) jsonArray.get(i);
                        String title = jsonObject.getJSONObject("snippet").getString("title");
                        String image = "";
                        try {
                            image = jsonObject.getJSONObject("snippet").getJSONObject("thumbnails").getJSONObject("medium").getString("url");
                        } catch (JSONException e) {
                            continue;
                        }

                        String videoId = jsonObject.getJSONObject("snippet").getJSONObject("resourceId").getString("videoId");
                        lstVideos.add(new Video(videoId, title, image));
                    }
                    Log.d("LDK", "size=" + lstVideos.size());
                    videoAdapter.notifyDataSetChanged();
                    setUpYoutube(lstVideos.get(0).getId());
                } catch (JSONException e) {
                    e.printStackTrace();
                }
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Toast.makeText(ThucHanhActivity.this, error.toString(), Toast.LENGTH_SHORT).show();
                Log.d("LDK", error.toString());
            }
        });
        requestQueue.add(jsonObjectRequest);
    }

    public void setUpYoutube(final String ID){
        if (youTubePlayerFragment == null) {
            return;
        }

        youTubePlayerFragment.initialize(Utils.YOUTUBE_API_KEY, new YouTubePlayer.OnInitializedListener() {
            @Override
            public void onInitializationSuccess(YouTubePlayer.Provider provider, YouTubePlayer youTubePlayer, boolean b) {
                if (!b) {
                    YPlayer = youTubePlayer;
                    //cue the 1st video by default
                    YPlayer.cueVideo(ID);
                }
            }

            @Override
            public void onInitializationFailure(YouTubePlayer.Provider provider, YouTubeInitializationResult youTubeInitializationResult) {
                Toast.makeText(ThucHanhActivity.this, youTubeInitializationResult.toString(), Toast.LENGTH_SHORT).show();
            }
        });
    }

}
