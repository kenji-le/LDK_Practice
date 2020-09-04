package com.example.hoclaixe.activity;

import android.app.Activity;
import android.app.PictureInPictureParams;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Rational;
import android.widget.Toast;

import com.example.hoclaixe.R;
import com.google.android.youtube.player.YouTubeInitializationResult;
import com.google.android.youtube.player.YouTubePlayer;
import com.google.android.youtube.player.YouTubePlayerSupportFragment;

public class PIPActivity extends AppCompatActivity {
    YouTubePlayerSupportFragment youTubePlayerFragment;
    private static Activity pipActivity;

    public static Activity getInstance() {
        return pipActivity;
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_pip);

        pipActivity = this;
        youTubePlayerFragment = (YouTubePlayerSupportFragment) getSupportFragmentManager().findFragmentById(R.id.youtube_player_fragment);

        if (android.os.Build.VERSION.SDK_INT >= 26) {
            //Trigger PiP mode
            try {
                Rational rational = new Rational(50, 25);
                PictureInPictureParams mParams = new PictureInPictureParams.Builder()
                        .setAspectRatio(rational)
                        .build();
                enterPictureInPictureMode(mParams);

                Intent intent = getIntent();
                setUpYoutube(intent.getStringExtra("videoId"));
            } catch (IllegalStateException e) {
                e.printStackTrace();
            }
        } else {
            Toast.makeText(PIPActivity.this, "API 26 needed to perform PiP", Toast.LENGTH_SHORT).show();
        }

    }

    public void setUpYoutube(final String ID) {
        if (youTubePlayerFragment == null) {
            return;
        }

        youTubePlayerFragment.initialize("AIzaSyAkXrLhbrccZ1XL0TpONctYGhDOH5Qow2k", new YouTubePlayer.OnInitializedListener() {
        //youTubePlayerFragment.initialize(Utils.YOUTUBE_API_KEY, new YouTubePlayer.OnInitializedListener() {

            @Override
            public void onInitializationSuccess(YouTubePlayer.Provider provider, YouTubePlayer youTubePlayer, boolean b) {
                if (!b) {
                    //cue the 1st video by default
                    youTubePlayer.loadVideo(ID);
                    //youTubePlayer.cueVideo(ID);
                }
            }

            @Override
            public void onInitializationFailure(YouTubePlayer.Provider provider, YouTubeInitializationResult youTubeInitializationResult) {

            }
        });
    }
}
