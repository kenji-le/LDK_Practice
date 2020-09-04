package com.example.hoclaixe.activity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Toast;

import com.example.hoclaixe.R;
import com.example.hoclaixe.model.Video;
import com.example.hoclaixe.util.Utils;
import com.google.android.youtube.player.YouTubeBaseActivity;
import com.google.android.youtube.player.YouTubeInitializationResult;
import com.google.android.youtube.player.YouTubePlayer;
import com.google.android.youtube.player.YouTubePlayerView;

public class PlayVideoActivity extends YouTubeBaseActivity {
    YouTubePlayerView youTubePlayerView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_play_video);

        Intent intent = getIntent();
        final Video video = (Video) intent.getSerializableExtra("Video");

        youTubePlayerView = findViewById(R.id.PlayVideo);
        youTubePlayerView.initialize(Utils.YOUTUBE_API_KEY, new YouTubePlayer.OnInitializedListener() {
            @Override
            public void onInitializationSuccess(YouTubePlayer.Provider provider, YouTubePlayer youTubePlayer, boolean b) {
                if (!b) {
                    youTubePlayer.loadVideo(video.getId());
                }
            }

            @Override
            public void onInitializationFailure(YouTubePlayer.Provider provider, YouTubeInitializationResult youTubeInitializationResult) {
                Toast.makeText(PlayVideoActivity.this, youTubeInitializationResult.toString(), Toast.LENGTH_SHORT).show();
            }
        });

    }
}

